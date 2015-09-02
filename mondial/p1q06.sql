SELECT religion.name, round(sum((population * percentage)/
(SELECT sum(population) FROM country)), 2)
FROM country,religion
WHERE religion.country = code
GROUP BY religion.name;


 

