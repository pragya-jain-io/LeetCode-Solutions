# Write your MySQL query statement below
select user_id , concat(Upper(SUBSTRING(Name, 1, 1)),lower(SUBSTRING(Name, 2 ))) as name from users order by user_id
