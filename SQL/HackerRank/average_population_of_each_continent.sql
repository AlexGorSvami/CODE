/* Given the CITY and COUNTRY tables, query the names of all the continents (COUNTRY.Continent) and their respective average city populations (CITY.Population) rounded down to the nearest integer */
-- Note: CITY.CountryCode and COUNTRY.Code are matching key columns.


select country.continent, floor(avg(city.population))
from city, country
where country.code = city.countrycode
group by country.continent;
