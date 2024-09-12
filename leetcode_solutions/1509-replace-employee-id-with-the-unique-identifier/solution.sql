# Write your MySQL query statement below
select u.unique_id, i.name from employees i
left join EmployeeUNI u on u.id=i.id;
