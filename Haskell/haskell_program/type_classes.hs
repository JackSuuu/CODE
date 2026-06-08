-- Element

elem :: Eq a => a -> [a] -> Bool

-- higher-order
elem x ys = foldr (||) False (map (x ==) ys)

-- comprehension
elemxys = or[x==y|y<-ys]

-- recursion
elem x [] = False
elem x(y:ys) = x==y || elem x ys