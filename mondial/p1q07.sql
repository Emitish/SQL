/*SELECT O1.country, O1.name,
(SELECT count(*)
FROM organization O2
WHERE O2.name = O1.name
GROUP BY O1.country, O2.name)
FROM organization O1;*/

select distinct A.code, B.code
from country A, country B
where A.code < B.code
and not exists
((( select organization
	from ismember
	where country = A.code )
except
(select organization
from ismember
where country = B.code)
)
union

((select organization
from ismember
where country = B.code)
except
(select organization
from ismember
where country = A.code)
))

order by A.code, B.code;
