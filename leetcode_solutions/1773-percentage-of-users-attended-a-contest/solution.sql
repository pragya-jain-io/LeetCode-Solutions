# Write your MySQL query statement below
select r.contest_id, round((count(distinct r.user_id)/(select count(u.user_id) from users u))*100,2) as percentage
from register r group by r.contest_id order by percentage desc, contest_id asc
