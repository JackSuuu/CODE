

nums  :: [Int]
nums  =  [1,2,3]

chars  :: [Char]
chars = ['I','n','f','1','A']
   
-- or, equivalently
str  :: String
str  =  "Inf1A"

-- 2D lists
numss  ::  [[Int]]
numss  =   [[1],[2,4,2],[],[3,5]]

-- List of two functions of the same type   
-- funs  :: [Picture -> Picture]
-- funs  =  [invert,flipV]

-- type error!
-- oops  =  [1,"Inf1A",[2,3]]  -- MISTAKE
   
count  :: [Int]
count  =  [1..10]

head :: [a] -> 'A'
head (x : xs) = x