
-- This is a line of comment
linearSearch :: (Eq a) => [a] -> a -> Maybe Int
linearSearch [] _ = Nothing  -- The element is not found in an empty list.
linearSearch (x:xs) target
    | x == target = Just 0  -- Element found at index 0.
    | otherwise = case linearSearch xs target of
                    Just index -> Just (index + 1)  -- Increment the index for subsequent elements.
                    Nothing -> Nothing  -- Element not found in the srest of the list.

-- Example usage:
main :: IO ()
main = do
    let myList = [4, 2, 9, 5, 1]
    let targetElement = 0
    case linearSearch myList targetElement of
        Just index -> putStrLn ("Element " ++ show targetElement ++ " found at index " ++ show index)
        Nothing -> putStrLn ("Element " ++ show targetElement ++ " not found in the list.")
