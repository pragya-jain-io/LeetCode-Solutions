/* Write your T-SQL query statement below */
select d.name as Department, e1.name as Employee, e1.salary as Salary
from employee e1 
join department d on e1.departmentid = d.id 
where e1.salary in 
    (select distinct TOP 3 e.salary 
        from employee e 
        where e.departmentid = e1.departmentid 
        group by e.departmentid, e.salary 
        order by e.salary desc)
order by d.name, e1.salary desc
