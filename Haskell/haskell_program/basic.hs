
-- A function to test if the number is greater than 10
isGreaterThan10 :: Int -> String
isGreaterThan10 x
    | x > 10 = "x is greater than 10"
    | otherwise = "x is not greater than 10"


-- A function to add two numbers together
add :: Int -> Int -> Int
add x y = x + y

main :: IO ()
main = do
    -- You can change the input value as needed
    let result = isGreaterThan10 9
    putStrLn result
    let final = add 2 3
    

