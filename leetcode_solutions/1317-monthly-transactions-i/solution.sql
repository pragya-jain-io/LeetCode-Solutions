# Write your MySQL query statement below
select DATE_FORMAT(trans_date, '%Y-%m') as month,
country,
count(*) as trans_count,
count(case when state = 'approved' then 1 else null end) as approved_count,
coalesce(sum(amount),0) as trans_total_amount,
coalesce(sum(case when state = 'approved' then amount else null end),0) as approved_total_amount
from transactions group by month, country
