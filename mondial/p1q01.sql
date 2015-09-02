SELECT country,province,name
FROM CITY 
WHERE (country,population) IN
	(SELECT country,max(population)
	FROM CITY
	GROUP BY country);
