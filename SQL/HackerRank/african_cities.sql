-- Given the CITY and COUNTRY tables, query the names of all cities where the CONTINENT is 'Africa'.
-- Note: CITY.CountryCode and COUNTRY.Code are matching key columns.v

select   city.name  from city, country where city.CountryCode = country.code and continent = 'Africa';
