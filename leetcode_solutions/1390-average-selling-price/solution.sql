# Write your MySQL query statement below
select p.product_id , coalesce (round(sum(p.price*u.units)/sum(u.units),2),0) average_price 
from prices p
left join unitssold u 
on u.product_id = p.product_id and purchase_date between start_date and end_date
group by p.product_id
