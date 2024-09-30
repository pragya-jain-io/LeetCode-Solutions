# Write your MySQL query statement below
select p.product_name, sum(o.unit) as unit from products p
join orders o on o.product_id = p.product_id
where o.order_date between '2020-02-01' AND '2020-02-29' 
group by p.product_id having unit >=100
