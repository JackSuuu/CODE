module Exp where

import Control.Monad
import Parser

data Exp = Lit Int
         | Exp :+: Exp
         | Exp :*: Exp
         deriving (Eq,Show)

evalExp :: Exp -> Int
evalExp (Lit n)    =  n
evalExp (e :+: f)  =  evalExp e + evalExp f
evalExp (e :*: f)  =  evalExp e * evalExp f

parseExp :: Parser Exp
parseExp  =  parseLit `mplus` parseAdd `mplus` parseMul
  where
  parseLit = do { n <- parseInt;
                  return (Lit n) }

  parseAdd = do { token '(';
                  d <- parseExp;
                  token '+';
                  e <- parseExp;
                  token ')';
                  return (d :+: e) }

  parseMul = do { token '(';
                  d <- parseExp;
                  token '*';
                  e <- parseExp;
                  token ')';
                  return (d :*: e) }

eval :: String -> Int
eval = evalExp . parse parseExp

test  :: Bool
test  =
  parse parseExp "(1+(2*3))" == (Lit 1 :+: (Lit 2 :*: Lit 3)) &&
  parse parseExp "((1+2)*3)" == ((Lit 1 :+: Lit 2) :*: Lit 3) &&
  eval "(1+(2*3))" == 7 &&
  eval "((1+2)*3)" == 9
  
           
