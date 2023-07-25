-- Query the list of CITY names from STATION that do not start with vowels and do not end with vowels. Your result cannot contain duplicates.
select distinct city from station where lower(substr(city,1,1)) not in ('a','i','e','u','o') and lower(substr(city, length(city),1)) not in ('a','e','i','o','u');

