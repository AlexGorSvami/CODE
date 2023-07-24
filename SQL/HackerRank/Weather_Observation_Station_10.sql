select distinct city from station where not (city like '%a' or city like '%e' or city like '%o' or city like '%u' or city like '%i') order by city;
