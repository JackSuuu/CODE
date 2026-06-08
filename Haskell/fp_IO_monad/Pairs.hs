module Pairs where
import Control.Monad

pairs :: Int -> [(Int,Int)]
pairs n  =  [ (i,j) | i <- [1..n], j <- [(i+1)..n] ]

pairs' :: Int -> [(Int,Int)]
pairs' n  =  do { i <- [1..n];
                  j <- [(i+1)..n];
                  return (i,j) }

pairs'' :: Int -> [(Int, Int)]
pairs'' n  =  [ (i,j) | i <- [1..n], j <- [1..n], i < j ]

pairs''' :: Int -> [(Int, Int)]
pairs''' n  =  do {
                 i <- [1..n];
                 j <- [1..n];
                 guard (i < j);
                 return (i,j)
               }

test =
  pairs 5 == pairs' 5 &&
  pairs' 5 == pairs'' 5 &&
  pairs'' 5 == pairs''' 5
