SELECT code,count(length)
from Country FULL OUTER JOIN symmetric_borders
on country.code = symmetric_borders.country1
group by code;
/*group by code,country1;*/
