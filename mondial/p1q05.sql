SELECT distinct  island
from locatedOn 
WHERE NOT EXISTS
(SELECT * 
FROM located
WHERE locatedOn.city = located.city and located.country = locatedOn.country);
