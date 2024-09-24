# Write your MySQL query statement below
select s.user_id, 
coalesce(round(count(case when c.action = 'confirmed' then 1 else null end)
/nullif(count(c.action),0),2),0.00) as confirmation_rate
from signups s 
left join confirmations c on c.user_id = s.user_id
group by s.user_id 
