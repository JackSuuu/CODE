import Test.QuickCheck

odds :: [Int] -> [Int]
odds xs = [x | x<-xs, odd x]

oddsRec :: [Int] -> [Int]
oddsRec []                  =  []
oddsRec (x:xs) | odd x      =  x : oddsRec xs
                | otherwise  =  oddsRec xs
prop_odds :: [Int] -> Bool
prop_odds xs  =  odds xs == oddsRec xs
