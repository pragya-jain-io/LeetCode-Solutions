# Write your MySQL query statement below
select e.employee_id from employees e where e.salary<30000 and e.manager_id not in (select g.employee_id from employees g) order by e.employee_id
