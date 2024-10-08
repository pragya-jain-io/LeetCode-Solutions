# Write your MySQL query statement below
select s.id, coalesce(case when s.id%2=0 then (select s2.student from seat s2 where s2.id = s.id-1) else (select s2.student from seat s2 where s2.id = s.id+1) end,s.student) as student from seat s order by s.id
