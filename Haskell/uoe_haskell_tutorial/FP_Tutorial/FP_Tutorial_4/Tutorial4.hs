{-# OPTIONS_GHC -Wno-unrecognised-pragmas #-}
{-# HLINT ignore "Use map" #-}
{-# HLINT ignore "Eta reduce" #-}
{-# HLINT ignore "Use foldr" #-}
{-# HLINT ignore "Fuse foldr/map" #-}
{-# HLINT ignore "Use and" #-}
module Tutorial4 where

import Data.Char
import Data.List
import Test.QuickCheck
import Data.Ratio
import GHC.Parser.Lexer (xset)


-- 1. doubles
-- a.
doublesComp :: [Int] -> [Int]
doublesComp xs = [x + x | x <- xs]

-- b.
doublesRec :: [Int] -> [Int]
doublesRec [] = []
doublesRec (x:xs) = (x + x) : doublesRec xs

-- c.
doublesHO :: [Int] -> [Int]
doublesHO lis = map (\x -> x + x) lis

-- d.
prop_doubles :: [Int] -> Bool
prop_doubles lis = (doublesComp lis == doublesRec lis) && (doublesRec lis == doublesHO lis) && (doublesComp lis == doublesHO lis)

-- 2. aboves
-- a.
abovesComp :: Int -> [Int] -> [Int]
abovesComp num lis = [x | x <- lis, x > num]

-- b.
abovesRec :: Int -> [Int] -> [Int]
abovesRec num [] = []
abovesRec num (x:xs)| x > num = x : abovesRec num xs
                    | otherwise = abovesRec num xs

-- c.
abovesHO :: Int -> [Int] -> [Int]
abovesHO num lis = filter (> num) lis

-- d.
prop_aboves :: Int -> [Int] -> Bool
prop_aboves num lis = (abovesComp num lis == abovesRec num lis) && (abovesComp num lis == abovesHO num lis) && (abovesRec num lis == abovesHO num lis)

-- 3. parity
-- a.
xor :: Bool -> Bool -> Bool
xor a b | a == b = False
        | otherwise = True

-- b.
parityRec :: [Bool] -> Bool
parityRec [] = True
parityRec (x:xs) = x `xor` parityRec xs

-- c.
parityHO :: [Bool] -> Bool
parityHO bool_list = foldr xor True bool_list

-- d.
prop_parity :: [Bool] -> Bool
prop_parity bool_list =  parityRec bool_list == parityHO bool_list

-- 4. allcaps
-- a.
allcapsComp :: String -> Bool
allcapsComp char_list = and [isUpper x | x <- char_list, isAlpha x]

-- b.
allcapsRec :: String -> Bool
allcapsRec [] = True
allcapsRec (x:xs)
        | isAlpha x = isUpper x && allcapsRec xs
        | otherwise = allcapsRec xs

-- c. Map + Filter + &&
allcapsHO :: String -> Bool
allcapsHO char_list = foldr (&&) True (map isUpper (filter isAlpha char_list))

-- d.
prop_allcaps :: String -> Bool
prop_allcaps char_list = (allcapsComp char_list == allcapsRec char_list) && (allcapsComp char_list == allcapsHO char_list) && (allcapsRec char_list == allcapsHO char_list)


-- ** Optional material
-- Matrix manipulation

type Matrix = [[Rational]]

myMatrix :: Matrix
myMatrix = [[1%2, 4, 9], [2, 5, 7]]

-- 5
-- a.
uniform :: [Int] -> Bool
uniform (x:xs) = all (== x) xs && x /= 0

-- b.
valid :: Matrix -> Bool
valid matrix = uniform [length row | row <- matrix]


-- 6.
width :: Matrix -> Int
width m = length (head m)

height :: Matrix -> Int
height m = length m

plusRow :: [Rational] -> [Rational] -> [Rational]
plusRow row_1 row_2 = zipWith (+) row_1 row_2

plusM :: Matrix -> Matrix -> Matrix
plusM m_1 m_2 
        | valid m_1 && valid m_2 = [plusRow r_1 r_2 | (r_1, r_2) <- zip m_1 m_2]
        | otherwise = error "[ERROR] - The Matrix input is not valid"

-- 7.
-- [[1,2,3],[4,5,6]] [[7,8],[9,10],[11,12]]
timesRow :: [Rational] -> [Rational] -> [Rational]
timesRow row_1 row_2 = zipWith (*) row_1 row_2

dot :: [Rational] -> [Rational] -> Rational
dot row_1 row_2 = sum (timesRow row_1 row_2)

timesM :: Matrix -> Matrix -> Either String Matrix
timesM [] _ = Right []  -- Multiplying by an empty matrix is valid
timesM (r:rs) m2
    | valid (r:rs) && valid m2 = case timesM rs m2 of
        Right result -> Right ([dot r r2 | r2 <- transpose m2] : result)
        Left errMsg -> Left errMsg
    | otherwise = Left "[ERROR] - The Matrix input is not valid"


-- ** Challenge

-- 8.
-- Mapping functions
mapMatrix :: (a -> b) -> [[a]] -> [[b]]
mapMatrix f = undefined

zipMatrix :: (a -> b -> c) -> [[a]] -> [[b]] -> [[c]]
zipMatrix f = undefined

-- All ways of deleting a single element from a list
removes :: [a] -> [[a]]
removes = undefined

-- Produce a matrix of minors from a given matrix
minors :: Matrix -> [[Matrix]]
minors m = undefined

-- A matrix where element a_ij = (-1)^(i + j)
signMatrix :: Int -> Int -> Matrix
signMatrix w h = undefined

determinant :: Matrix -> Rational
determinant = undefined

cofactors :: Matrix -> Matrix
cofactors m = undefined

scaleMatrix :: Rational -> Matrix -> Matrix
scaleMatrix k = undefined

inverse :: Matrix -> Matrix
inverse m = undefined

-- Tests
identity :: Int -> Matrix
identity n = undefined

prop_inverse1 :: Rational -> Property
prop_inverse1 a = undefined

prop_inverse2 :: Rational -> Rational -> Rational
                -> Rational -> Property
prop_inverse2 a b c d = undefined

type Triple a = (a,a,a)

prop_inverse3 :: Triple Rational ->
                 Triple Rational ->
                 Triple Rational ->
                 Property
prop_inverse3 r1 r2 r3 = undefined
