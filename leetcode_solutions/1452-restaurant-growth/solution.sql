# Write your MySQL query statement below
select distinct c1.visited_on, 
(select sum(c2.amount) from customer c2 where c2.visited_on between c1.visited_on- interval 6 day and c1.visited_on) as amount , 
round((select sum(c2.amount) from customer c2 where c2.visited_on between c1.visited_on- interval 6 day  and c1.visited_on)/7,2) as average_amount 
from customer c1 
where c1.visited_on-6 >= (select min(c3.visited_on) from customer c3)
