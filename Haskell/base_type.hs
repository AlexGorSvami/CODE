-- :type 'c'  -- char
-- :type '\n' -- char 
-- :type True --bool
-- :t Flase --bool
-- :t 3 -- 3 :: Num a => a
-- x = 3 :: Int
-- x -- :t x --Int
-- y = 3 :: Double
-- y -- 3.0
-- :t y -- Double
-- z = y + 17
-- :t Double
-- :t 3.5 -- Fractional a => a
-- 123455555555555555555 :: Integer
-- :t 1234555555555555555 --Integer
module Demo  where
import Data.Char

test = isDigit '7'

import  Data.Char
twoDigits2Int ::   Char ->  Char  -> Int
twoDigits2Int x y = if (&&) (isDigit x) (isDigit y) then $ $ digitToInt x * 10 + digitToInt y else 100
