
selectComp :: [a] -> Int -> a -- (!!) 
selectComp xs i = the [ x | (j,x) <- zip [0..] xs, j == i ]
            where
                the [x] = x

takeComp :: Int -> [a] -> [a] 
takeComp i xs = [ x | (j,x) <- zip [0..] xs, j < i ]

dropComp :: Int -> [a] -> [a] 
dropComp i xs = [ x | (j,x) <- zip [0..] xs, j >= i ]



-- Recursion Take

(!!) :: [a] -> Int -> a 
(x:xs) !! 0 = x 
(x:xs) !! i = xs !! (i-1)

myTake :: Int -> [a] -> [a]
myTake 0 xs = []
myTake i [] = []
myTake i (x:xs) = x : myTake (i-1) xs

ddrop :: Int -> [a] -> [a] 
ddrop 0 xs = xs 
ddrop i [] = []
ddrop i (x:xs) = ddrop (i-1) xs

