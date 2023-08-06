-- P(R) represents a pattern drawn by Julia in R rows. The following pattern represents P(5):
--
-- * * * * * 
-- * * * * 
-- * * * 
-- * * 
-- *
--

set @n = 20;
with RECURSIVE seq as(
  select 1 as val
  union all
  select val + 1
  from seq
  where val+1 <= @n
)
select REPEAT('* ', val)
from seq
order by val desc;
