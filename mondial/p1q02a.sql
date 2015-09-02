SELECT country1,count(country1)
from symmetric_borders
group by country1;
