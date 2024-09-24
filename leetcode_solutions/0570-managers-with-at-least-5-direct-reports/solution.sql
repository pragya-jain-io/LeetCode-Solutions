# Write your MySQL query statement below
select e1.name from employee e1 where e1.id in (select e2.managerId from employee e2 group by e2.managerid having count(e2.managerid)>=5)
