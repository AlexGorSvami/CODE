select sum(city.population)
from country
inner join city
    on country.code = city.countrycode
where continent = 'Asia';

