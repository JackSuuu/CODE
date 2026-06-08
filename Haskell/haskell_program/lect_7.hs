import Test.QuickCheck

-- add :: Int -> (Int -> Int)
-- (add x) y = x + y


add :: Int -> (Int -> Int) 
add x = g
    where
        g :: Int -> Int 
        g y = x + y

flip :: (a -> (b -> c)) -> (b -> (a -> c))
flip f x y = f y x

-- curry :: ((a, b) -> c) -> (a -> (b -> c))
-- curry f x y = f x y


(.) :: (b -> c) -> (a -> b) -> (a -> c) 
(f.g)x = f (g x)


