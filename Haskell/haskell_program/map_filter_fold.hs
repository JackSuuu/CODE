
-- Part 1: Map
-- Function takes function as argument (nested)
-- map :: (a -> b) -> [a] -> [b] 
-- map f xs = [ f x | x <- xs ]

-- mymap :: (a -> b) -> [a] -> [b] 
-- mymap f [] = [] 
-- mymap f (x:xs) = f x : mymap f xs

-- Square by using HHF
squares :: [Int] -> [Int]
squares = map sqr
    where
    sqr x = x * x

-- Part 2: Filter
-- filter :: (a -> Bool) -> [a] -> [a] 
-- filter p xs = [ x | x <- xs, p x ]

myfilter :: (a -> Bool) -> [a] -> [a]
myfilter p [] = []
myfilter p (x:xs)   | p x        = x : myfilter p xs
                    | otherwise  =  myfilter p xs


-- Part3: Fold
-- ffoldr :: (a -> a -> a) -> a -> [a] -> a 
-- ffoldr f v [] = v
-- ffoldr f v (x:xs) = f x (ffoldr f v xs)
