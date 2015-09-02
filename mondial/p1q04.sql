SELECT code, population, total
FROM ( SELECT country1, sum(country.population) AS  total
FROM  country, symmetric_borders
WHERE country.code = country2
GROUP BY country1)
AS secondCountry, country 
WHERE secondCountry.country1 = country.code
UNION
(SELECT code, population, NULL
FROM country
WHERE code NOT IN (SELECT country1 FROM symmetric_borders));
