select * from complaints;

--Top 10 Companies by Complaint Count
select  Company, count(*) as no_of_complaints 
from complaints 
group by Company 
order by no_of_complaints desc  
limit 10 ;

--Top 10 States
select  State, count(*) as no_of_complaints 
from complaints 
group by State 
order by no_of_complaints desc  
limit 10 ;

--top products
--Top 10 States
select  Product, count(*) as no_of_complaints 
from complaints 
group by Product  
order by no_of_complaints desc  
limit 10 ;

--Timely Response Rate
select "Timely response?" , count(*) as total 
from complaints 
group by "Timely response?"
order by total;

--Which companies receive the most Credit Card complaints?

select Company , count(*) as total_complaints
from complaints 
where Product like '%credit%'
group by Company 
order by total_complaints desc
limit 10  ;
--you cant put product filter in having because its after grouping and u want it to filoter before grp 



--Which states have the highest percentage of untimely responses
SELECT
    State,
    COUNT(*) AS Total_Complaints,
    SUM(
        CASE
            WHEN "Timely response?" = 'No' THEN 1
            ELSE 0
        END
    ) AS Untimely_Responses,
    ROUND(
        100.0 *
        SUM(
            CASE
                WHEN "Timely response?" = 'No' THEN 1
                ELSE 0
            END
        ) / COUNT(*),
        2
    ) AS Untimely_Percentage
FROM complaints
GROUP BY State
ORDER BY Untimely_Percentage DESC
LIMIT 10;

--Which companies have the highest complaint rate in each product?
with no_complaints as (select Product, Company , count(*) as total_Complaints,
dense_rank() over ( partition by Product order by count(*) desc ) as rank
from complaints
group by Product , Company)

select *
from no_complaints 
where rank <= 5
order by Product, rank ;

--Complaint Trend by Year
select strftime('%Y', "Date received") as Year,  --remember if u forgot "" and '' for Y  then wrong ans
count(*) as Complaints 
from complaints 
group by Year
order by Year asc ;



select strftime('%Y', "Date received") as Year,  --remember if u forgot "" and '' for Y  then wrong ans
Product
, count(*) as Complaints 
from complaints 
group by Year , Product 
order by Year, Complaints asc ;


SELECT
    Company,
    COUNT(*) AS Total_Complaints,
    COUNT(DISTINCT Product) AS Products_Involved
FROM complaints
GROUP BY Company
HAVING COUNT(*) > 1000
ORDER BY Products_Involved DESC, Total_Complaints DESC
LIMIT 15;