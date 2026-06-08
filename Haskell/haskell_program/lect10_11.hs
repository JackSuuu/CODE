
-- Expression
data Exp = Lit Int
    | Add Exp Exp
    | Mul Exp Exp 
    deriving Eq


e0, e1 :: Exp
e0 = Add (Lit 2) (Mul (Lit 3) (Lit 3))
e1 = Mul (Add (Lit 2) (Lit 3)) (Lit 3)

par :: String -> String
par s = "(" ++ s ++ ")"

showExp :: Exp -> String
showExp (Lit n) = show n
showExp (Add e f) = par (showExp e ++ "+" ++ showExp f) 
showExp (Mul e f) = par (showExp e ++ "*" ++ showExp f)

-- Proposition 

type Name = String 
data Prop = Var Name
        |F
        |T
        | Not Prop
        | Prop :||: Prop | Prop :&&: Prop deriving Eq


type Valn = Name -> Bool 

evalProp :: Valn -> Prop -> Bool
evalProp vn (Var x) = vn x
evalProp vn F =  False
evalProp vn T = True
evalProp vn (Not p) = not (evalProp vn p)
evalProp vn (p :||: q) = evalProp vn p || evalProp vn q
evalProp vn (p :&&: q) = evalProp vn p && evalProp vn q

-- Example
p0 :: Prop
p0 =  Var "a" :&&: Not (Var "a")

valn :: Valn
valn "a" = True
valn "b" = True
valn "c" = False
valn "d" = True

