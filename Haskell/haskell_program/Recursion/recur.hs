oddsRec :: [Int] -> [Int]
oddsRec []                   = []
oddsRec (x:xs)  | odd x      =  x : oddsRec xs
                | otherwise  =  oddsRec xs


getRid :: [Int] -> [Int]
getRid (x:xs) = xs

factorial :: Int -> Int
factorial 0 = 1
factorial x = x * factorial (x-1)

