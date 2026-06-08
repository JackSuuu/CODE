df_traverse :: Tree a -> [a] 
df_traverse Nil = [] 
df_traverse (Node t1 x t2) = x : (df_traverse t1) ++ (df_traverse t2)


depthFirst’ :: Eq a => (a -> Bool) -> Tree a -> Maybe a 
depthFirst’ p t = head( [Just x | x <- df_traverse t, p x] ++ [Nothing] )
