module Tutorial4 where

import Data.Char
import Data.List
import Test.QuickCheck
import Data.Ratio


-- 1. doubles
-- a.
doublesComp :: [Int] -> [Int]
doublesComp xs =  [ x*2 | x <- xs ]

-- b.
doublesRec :: [Int] -> [Int]
doublesRec [] = []
doublesRec (x:xs) =  x*2 : doublesRec xs

-- c.
doublesHO :: [Int] -> [Int]
doublesHO xs = map (*2) xs

-- d.
prop_doubles :: [Int] -> Bool
prop_doubles xs = doublesComp xs == doublesRec xs && doublesComp xs == doublesHO xs

-- 2. aboves
-- a.
abovesComp :: Int -> [Int] -> [Int]
abovesComp k xs = [ x | x <- xs, x > k ]

-- b.
abovesRec :: Int -> [Int] -> [Int]
abovesRec k [] = []
abovesRec k (x:xs) = if x > k
                     then x : abovesRec k xs
                     else abovesRec k xs

-- c.
abovesHO :: Int -> [Int] -> [Int]
abovesHO k xs = filter (>k) xs

-- d.
prop_aboves :: Int -> [Int] -> Bool
prop_aboves k xs = abovesComp k xs == abovesRec k xs && abovesComp k xs == abovesHO k xs

-- 3. parity
-- a.
xor :: Bool -> Bool -> Bool
xor True False = True
xor False True = True
xor _ _ = False

-- b.
parityRec :: [Bool] -> Bool
parityRec [] = True
parityRec (x:xs) = xor x (parityRec xs)

-- c.
parityHO :: [Bool] -> Bool
parityHO xs = foldr xor True xs

-- d.
prop_parity :: [Bool] -> Bool
prop_parity xs = parityRec xs == parityHO xs

-- 4. allcaps
-- a.
allcapsComp :: String -> Bool
allcapsComp xs = and [ isUpper x | x <- xs, isAlpha x ]

-- b.
allcapsRec :: String -> Bool
allcapsRec [] = True
allcapsRec (x:xs) = if isAlpha x
                    then isUpper x && allcapsRec xs
                    else allcapsRec xs

-- c.
allcapsHO :: String -> Bool
allcapsHO xs = foldr (&&) True (map (isUpper) (filter (isAlpha) xs))

-- d.
prop_allcaps :: String -> Bool
prop_allcaps xs = allcapsComp xs == allcapsRec xs && allcapsComp xs == allcapsHO xs


-- ** Optional material
-- Matrix manipulation

type Matrix = [[Rational]]

-- 5
-- a.
uniform :: [Int] -> Bool
uniform [] = True
uniform (x:xs) = all (==x) xs

-- all :: Foldable t => (a -> Bool) -> t a -> Bool
-- all f xs = foldr f True xs

-- b.
valid :: Matrix -> Bool
valid [] = False
valid xs = uniform (map (length) xs)

-- 6.
width :: Matrix -> Int
width [] = error "Invalid Matrix"
width (x:xs) = if valid (x:xs)
          then length x
          else error "Invalid Matrix"

height :: Matrix -> Int
height m = if valid m
           then length m
           else error "Invalid Matrix"
           
plusRow :: [Rational] -> [Rational] -> [Rational]
plusRow m n = zipWith (+) m n

plusM :: Matrix -> Matrix -> Matrix
plusM m n = if width m == width n && height m == height n
            then zipWith plusRow m n
            else error "Invalid Addition"

-- 7.
dot :: [Rational] -> [Rational] -> Rational
dot m n = sum (zipWith (*) m n)

timesM :: Matrix -> Matrix -> Matrix
timesM [] _ = []
timesM (x:xs) n = if width (x:xs) == height n
                  then ([ dot x y | y <- n' ] : timesM xs n)
                  else error "Invalid Multiplication"
                    where n' = transpose n

-- ** Challenge

-- 8.
-- Mapping functions
mapMatrix :: (a -> b) -> [[a]] -> [[b]]
mapMatrix f m = [ map f x | x <- m ]

zipMatrix :: (a -> b -> c) -> [[a]] -> [[b]] -> [[c]]
zipMatrix f a b = [ zipWith f x y | (x,y) <- zip a b ]

-- All ways of deleting a single element from a list
removeRow :: Int -> [[a]] -> [[a]]     
removeRow k m = [ xs | (xs, y) <- zip m [1..], y/=k ]

removeColumn :: Int -> [[a]] -> [[a]]
removeColumn k m = transpose (removeRow k (transpose m))

-- Produce a matrix of minors from a given matrix
minors :: Matrix -> Matrix
minors m = undefined

-- A matrix where element a_ij = (-1)^(i + j)
signMatrix :: Int -> Int -> Matrix
signMatrix w 0 = []
signMatrix w h = signMatrix w (h-1) ++ [[ toRational (-1)^(x+h) | x <- [1..w] ]]
        
determinant :: Matrix -> Rational
determinant [[x]] = x
determinant m = if width m == height m
                then sum [ (determinant (removeRow 1 (removeColumn y m)))*x | (x, y) <- zip (head n) [1..] ]
                else error "Invalid Matrix"
                  where n = zipMatrix (*) m (signMatrix (width m) (height m))

splitEachk :: Int -> [a] -> [[a]]
splitEachk k [] = []
splitEachk k xs = take k xs : splitEachk k (drop k xs)

cofactors :: Matrix -> Matrix
cofactors [[x]] = [[1]]
cofactors m = if width m == height m
              then splitEachk (width m) [ determinant (removeColumn y x) | x <- [ removeRow x n | x <- [1..(height m)] ], y <- [1..(width m)] ]
              else error "Invalid Matrix"
                where n = zipMatrix (*) m (signMatrix (width m) (height m))
                
scaleMatrix :: Rational -> Matrix -> Matrix
scaleMatrix k = undefined

inverse :: Matrix -> Matrix
inverse m = if determinant m /= 0 && width m == height m
            then mapMatrix (/(determinant m)) (transpose (cofactors m))
            else error "No inverse"

-- Tests
identity :: Int -> Matrix
identity n = splitEachk n [ if x==y then 1 else 0 | x <- [1..n], y <- [1..n] ]

prop_inverse1 :: Rational -> Property
prop_inverse1 a = a/=0 ==> timesM [[a]] (inverse [[a]]) == identity 1

prop_inverse2 :: Rational -> Rational -> Rational 
                -> Rational -> Property
prop_inverse2 a b c d = determinant m /= 0 ==> timesM m (inverse m) == identity 2
                          where m = [[a,b],[c,d]]

type Triple a = (a,a,a)

changeToList :: Triple a -> [a]
changeToList (x,y,z) = [x,y,z]
        
prop_inverse3 :: Triple Rational -> 
                 Triple Rational -> 
                 Triple Rational ->
                 Property
prop_inverse3 r1 r2 r3 = determinant m /= 0 ==> timesM m (inverse m) == identity 3
                           where m = [changeToList r1, changeToList r2, changeToList r3]
