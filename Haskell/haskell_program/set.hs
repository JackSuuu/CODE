module ListAbs
(Set,empty,insert,set,element,equal) where import Test.QuickCheck

data Set a = MkSet [a]

empty :: Set a empty = MkSet []
insert :: a -> Set a -> Set a insert x (MkSet xs) = MkSet (x:xs)
set :: [a] -> Set a set xs = MkSet xs
