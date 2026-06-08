module MicroQuickCheck(Gen,sized,choose,oneof,elements,
  Arbitrary(arbitrary),Testable(check),quickCheck) where
import System.Random

type    Size   =  Int
newtype Gen a  =  MkGen (StdGen -> Size -> (a, StdGen))

apply :: Gen a -> StdGen -> Size -> (a, StdGen)
apply (MkGen g) r s  =  g r s

run :: Gen a -> Size -> IO a
run g s  =  do { r0 <- getStdGen;
                 let { (x,r1) = apply g r0 s } ;
                 setStdGen r1;
                 return x }

instance Monad Gen where
  return x =
    MkGen (\ r s -> (x, r))
  m >>= k =
    MkGen (\ r0 s ->
      let (x, r1)  =  apply m r0 s
          (y, r2)  =  apply (k x) r1 s
       in (y, r2))

sized :: (Int -> Gen a) -> Gen a
sized k =
  MkGen (\r s -> apply (k s) r s)

choose :: Random a => (a,a) -> Gen a
choose rng =
  MkGen (\r _ -> randomR rng r)

oneof :: [Gen a] -> Gen a
oneof [] = error "oneof used with empty list"
oneof gs = do { i <- choose (0, length gs - 1);
                gs !! i }

elements :: [a] -> Gen a
elements xs  =  oneof (map return xs)

class Arbitrary a where
  arbitrary :: Gen a

scale :: Size -> (Int,Int)
scale s  =  let n = toInteger (31 * s `div` 100) in
                (fromInteger (-2^n), fromInteger (2^n - 1))

instance Arbitrary Bool where
  arbitrary = elements [False, True]

instance Arbitrary Int where
  arbitrary = sized (\ s -> choose (scale s))

instance (Arbitrary a, Arbitrary b) =>
  Arbitrary (a,b) where
    arbitrary = do { x <- arbitrary;
                     y <- arbitrary;
                     return (x,y) }

instance Arbitrary a => Arbitrary [a] where
  arbitrary = sized (\s ->
    do { n <- choose (0,s);
         sequence (replicate n arbitrary) })

class Testable a where
  check :: a -> Gen Bool

instance Testable Bool where
  check y  =  return y

instance (Arbitrary a, Testable b) => Testable (a -> b) where
  check f  =  do { x <- arbitrary;
                   check (f x) }

quickCheck :: Testable a => (a -> IO ())
quickCheck f  =
  do { results <- sequence [ run (check f) s | s <- [1..100] ];
       if and results then
         putStrLn "+++ OK, passed 100 tests."
       else
         putStrLn "*** Failed!" }

prop_assoc :: Int -> Int -> Int -> Bool
prop_assoc x y z  =  (x + y) + z  ==  x + (y + z)

prop_sqr :: Int -> Bool
prop_sqr x  =  x * x >= 0

prop_wrong :: Bool -> Int -> Bool
prop_wrong b x  =  b || even x

main =
  quickCheck prop_assoc >>   -- OK
  quickCheck prop_sqr >>     -- fails for large int (wraparound)
  quickCheck prop_wrong      -- fails given false and odd value
