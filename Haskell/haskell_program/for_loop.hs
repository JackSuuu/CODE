

printNumbers :: Int -> IO ()
printNumbers 6 = return ()
printNumbers n = do
  putStrLn (show n)
  printNumbers (n + 1)
