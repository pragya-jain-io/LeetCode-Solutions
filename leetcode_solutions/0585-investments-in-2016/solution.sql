# Write your MySQL query statement below
select round(sum(i1.tiv_2016),2) as tiv_2016 from Insurance i1
where i1.tiv_2015 in (select i2.tiv_2015 from insurance i2 group by i2.tiv_2015 having count(i2.tiv_2015)>1) and
(select count( case when i3.lat = i1.lat and i3.lon=i1.lon then 1 else null end) from insurance i3 ) = 1;
