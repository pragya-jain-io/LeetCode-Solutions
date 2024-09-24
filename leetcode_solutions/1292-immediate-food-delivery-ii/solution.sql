# Write your MySQL query statement below
select round((count(case when order_date = customer_pref_delivery_date then 1 else null end)/(count(distinct customer_id)))*100,2) as immediate_percentage 
from delivery
where (customer_id,order_date) in (select customer_id,min(order_date) from delivery group by customer_id)
