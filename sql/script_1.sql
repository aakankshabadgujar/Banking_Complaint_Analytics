select * from complaints;
--retreieve the DATA

--Show Only Product and Company
select Product , Company from complaints;

--limit rows 
select * from complaints limit 10;

--Only Credit Card Complaints
select * from complaints where Product like '%credit%';

--Show Only California Complaints
select * from complaints where State like '%CA%';

SELECT *
FROM complaints
WHERE Product = 'Credit card'
AND State = 'CA';
