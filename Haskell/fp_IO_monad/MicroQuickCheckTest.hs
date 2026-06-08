module MicroQuickCheckTest where
import MicroQuickCheck
import Control.Monad
import Proposition

-- defined in Proposition
-- data  Proposition  =   Var String
-- 		      |   F
--		      |   T
--		      |   Not Proposition
--		      |   Proposition :|: Proposition
--		      |   Proposition :&: Proposition
--		      deriving (Eq, Ord)

-- defined in Control.Monad

-- liftM :: Monad m => (a -> b) -> m a -> m b
-- liftM f m  =  do { x <- m; return (f x) }

-- liftM2 :: Monad m => (a -> b -> c) -> m a -> m b -> m c
-- liftM2 f m n  =  do { x <- m; y <- n; return (f x y) }

instance Arbitrary Proposition where
  arbitrary = sized expr
    where
      expr 0 =
        oneof [return F,
               return T,
               liftM Var (elements ["p", "q", "r", "s", "t"])]
      expr n | n > 0 =
        oneof [return F,
               return T,
               liftM Var (elements ["p", "q", "r", "s", "t"]),
               liftM Not (expr (n-1)),
               liftM2 (:&:) (expr (n `div` 2)) (expr (n `div` 2)),
               liftM2 (:|:) (expr (n `div` 2)) (expr (n `div` 2))]

prop_parse :: Proposition -> Bool
prop_parse p  =  read (show p) == p

main =
  quickCheck prop_parse
