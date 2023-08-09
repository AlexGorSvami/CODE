factorial n = if n == 0 then 1 else n * factorial (n - 1)

factorial' 0 = 1
factorial' n = n * factorial' (n - 1)

doubleFact :: Integer -> Integer
doubleFact 0 = 0
doubleFact 1 = 1
doubleFact 2 = 2
doubleFact n = n * doubleFact (n - 2)

doubleFact' n = if n > 2 then n else n * doubleFact' (n - 2)

factorial'' 0 = 1
factorial'' n = if n < 0 then error "n must be >= 0" else n * factorial'' (n - 1)

factorial''' 0 = 1
factorial''' n = if n < 0 then undefined else n * factorial''' (n - 1)

-----------------------Охранные выражения ---------------------
factorialO 0 = 1
factorialO n | n < 0 = error "arg must be >= 0"
             | n > 0 = n * factorialO (n - 1)

factorial1 :: Integer -> Integer
factorial1 n | n == 0 = 1
             | n > 0  = n * factorial1 (n - 1)
             | otherwise = error "arg must be >= 0"

---Fibonachi
neg_fibonachi n | n > 1 = neg_fibonachi(n - 1) + neg_fibonachi(n - 2)
                | n < 0 = neg_fibonachi (n + 2) + neg_fibonachi( n + 1)
                | otherwise = n

fibonacci' :: Integer -> Integer
fibonacci' 0 = 0
fibonacci' 1 = 1
fibonacci' (-1) = 1
fibonacci' (-2) = (-1)
fibonacci' n = if n >= 0 then fibonacci' (n - 1) + fibonacci' (n - 2) else fibonacci' (n + 2) - fibonacci' (n + 1)
