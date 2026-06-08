
-- lists comprehensions
numbers :: [Int]
numbers = [x | x <- [1..10], even x]

-- show numbers print the whole list out in Str way
factorial :: Int -> Int
factorial n = product [1..n]
-- factorial 4 
-- > 24

squares :: [Int] -> [Int] squaresxs = [ x*x | x<-xs ]

odds :: [Int] -> [Int]
oddsxs = [ x| x< - xs, oddx]

sumSqOdd :: [Int] -> Int
sumSqOdd xs = sum [ x*x | x <- xs, odd x]
