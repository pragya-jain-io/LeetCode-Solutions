# Write your MySQL query statement below

select sell_date, num_sold, products from 
(select sell_date, count(distinct product) as num_sold, group_concat(distinct product) as products 
    from Activities group by sell_date order by product asc) 
as temp order by sell_date asc;
