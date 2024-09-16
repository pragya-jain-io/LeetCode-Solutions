select a.id
from weather a inner join weather b
on date_add(a.recorddate, interval -1 day) = b.recorddate
where a.temperature>b.temperature
