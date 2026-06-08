
enumFromto :: Int -> Int -> [Int]
enumFromto m n  | m > n    =  []
                | m <= n   =  m : enumFromto (m + 1) n


factorialRec :: Int -> Int
factorialRec n  =  fact 1 n
    where
        fact :: Int -> Int -> Int
        fact m n | m > n    =  1
                 | m <= n   =  m * fact (m + 1) n

myZip :: [a] -> [b] -> [(a,b)]
myZip [] ys = []
myZip xs [] = []
myZip (x:xs) (y:ys) = (x,y) : myZip xs ys

-- Upright
zipHarsh :: [a] -> [b] -> [(a,b)]
zipHarsh [] []          =  []
zipHarsh (x:xs) (y:ys)  =  (x,y) : zipHarsh xs ys

-- Comprehensions Search
search :: Eq a => [a] -> a -> [Int]
search xs y = [ i | (i,x) <- zip [0..] xs, x==y ]

-- Recursion
searchRec :: Eq a => [a] -> a -> [Int] 
searchRec xs y = srch xs y 0
    where
        srch :: Eq a => [a] -> a -> Int -> [Int]
        srch [] y i = []
        srch (x:xs) y i
            | x == y    = i : srch xs y (i+1)
            | otherwise = srch xs y (i+1)
