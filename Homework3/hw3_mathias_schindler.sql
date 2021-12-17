
-- Problem set week 3 number 2.

-- Please load music-store database

-- Please add the proper SQL query to follow the instructions below


------------------------------------------------
use musicstore;
------------------------------------------------

-- 1.Show the Number of tracks whose composer is F. Baltes
-- (Note: there can be more than one composers for each track)
SELECT COUNT(*) 
FROM Track 
WHERE Composer LIKE "%F. Baltes%";


-- 2.Show the Number of invoices, and the number of invoices with a total amount =0.99 in the same query
-- (Hint: you can use CASE WHEN)
SELECT COUNT(*), 
SUM(CASE WHEN Total =0.99 THEN 1 ELSE 0 END) 
FROM Invoice;


-- 3.Show the album title and artist name of the first five albums sorted alphabetically
SELECT Album.Title, Artist.Name 
FROM Album 
LEFT JOIN Artist ON Album.ArtistID = Artist.ArtistID
ORDER BY Title
LIMIT 5;


-- 4.Show the Id, first name, and last name of the 10 first customers 
-- alphabetically ordered. Include the id, first name and last name 
-- of their support representative (employee)
SELECT Customer.CustomerId, Customer.LastName, Customer.FirstName, Customer.SupportRepId, 
Employee.FirstName, Employee.LastName
FROM Customer
LEFT JOIN Employee ON Customer.SupportRepId = Employee.EmployeeId
ORDER BY Customer.LastName
LIMIT 10;


-- 5.Show the Track name, duration, album title, artist name,
--  media name, and genre name for the five longest tracks
SELECT Track.Name, Track.Milliseconds, Album.Title, Artist.Name, MediaType.Name, Genre.Name
FROM Track
LEFT JOIN Album ON Track.AlbumId = Album.AlbumId
LEFT JOIN Artist ON Album.ArtistID = Artist.ArtistID
LEFT JOIN Genre ON Track.GenreId= Genre.GenreId
LEFT JOIN MediaType ON Track.MediaTypeID = MediaType.MediaTypeId
ORDER BY Milliseconds DESC
LIMIT 5;


-- 6.Show Employees' first name and last name
-- together with their supervisor's first name and last name
-- Sort the result by employee last name
SELECT A.LastName, A.FirstName, B.LastName AS SuperLastName, B.FirstName AS SuperFirstName
FROM Employee A, Employee B
WHERE A.ReportsTo = B.EmployeeId
ORDER BY A.LastName;


-- 7.Show the Five most expensive albums
--  (Those with the highest cumulated unit price)
--  together with the average price per track
SELECT Album.Title, Artist.Name, B.AlbumPrice, B.AvgUnitPrice 
FROM Album
LEFT JOIN (
	SELECT AlbumId, SUM(UnitPrice) AS AlbumPrice, AVG(UnitPrice) AS AvgUnitPrice
	FROM Track GROUP BY AlbumId) AS B 
ON Album.AlbumId = B.AlbumId
LEFT JOIN Artist ON Artist.ArtistId = Album.ArtistId
ORDER BY AlbumPrice DESC
LIMIT 5;


-- 8. Show the Five most expensive albums
--  (Those with the highest cumulated unit price)
-- but only if the average price per track is above 1
SELECT Album.Title, Artist.Name, B.AlbumPrice, B.AvgUnitPrice 
FROM Album
LEFT JOIN (
	SELECT AlbumId, SUM(UnitPrice) AS AlbumPrice, AVG(UnitPrice) AS AvgUnitPrice
	FROM Track GROUP BY AlbumId) AS B 
ON Album.AlbumId = B.AlbumId
LEFT JOIN Artist ON Artist.ArtistId = Album.ArtistId
HAVING AvgUnitPrice>1
ORDER BY AlbumPrice DESC
LIMIT 5;


-- 9.Show the album Id and number of different genres
-- for those albums with more than one genre
-- (tracks contained in an album must be from at least two different genres)
-- Show the result sorted by the number of different genres from the most to the least eclectic 
SELECT AlbumId, COUNT(DISTINCT GenreId) AS DifferentGenre
FROM Track 
GROUP BY AlbumId
HAVING DifferentGenre >1
ORDER BY DifferentGenre DESC;


-- 10.Show the total number of albums that you get from the previous result (hint: use a nested query)
SELECT COUNT(*) 
FROM (
	SELECT AlbumId, COUNT(DISTINCT GenreId) AS DifferentGenre
	FROM Track 
	GROUP BY AlbumId
	HAVING DifferentGenre >1
	ORDER BY DifferentGenre
) AS B;


-- 11.Show the	number of tracks that were ever in some invoice
SELECT COUNT(DISTINCT Track.TrackId) 
FROM Track
INNER JOIN InvoiceLine ON Track.TrackId = InvoiceLine.TrackId
ORDER BY Track.TrackId;


-- 12.Show the Customer id and total amount of money billed to the five best customers 
-- (Those with the highest cumulated billed imports)
SELECT CustomerId, SUM(Total) AS Cum_Invoice
FROM Invoice 
GROUP BY CustomerId 
ORDER BY Cum_Invoice DESC 
LIMIT 5;


-- 13.Add the customer's first name and last name to the previous result
-- (hint:use a nested query)
SELECT A.CustomerId, FirstName, LastName, B.Cum_Inv 
FROM Customer AS A
RIGHT JOIN (
	SELECT CustomerId, SUM(Total) AS Cum_Inv 
	FROM Invoice 
	GROUP BY CustomerId 
	ORDER BY Cum_Inv DESC 
    LIMIT 5
) AS B
ON A.CustomerId = B.CustomerId;


-- 14.Check that the total amount of money in each invoice
-- is equal to the sum of unit price x quantity
-- of its invoice lines.
SELECT InvoiceId, Total, SUM(PriceCheck) AS Cum_Pcheck 
FROM (
	SELECT B.InvoiceId, B.Total, UnitPrice * Quantity AS PriceCheck FROM InvoiceLine AS PriceCheckTable
	LEFT JOIN Invoice AS B ON PriceCheckTable.InvoiceId = B.InvoiceId
    ) AS B 
GROUP BY InvoiceId
HAVING Cum_Pcheck <> Total;
-- They all seem to match


-- 15.We are interested in those employees whose customers have generated 
-- the highest amount of invoices 
-- Show first_name, last_name, and total amount generated 

-- NB; With "amount of invoices" I assume we should count the number instead of doing highest sum of money generated
SELECT Emp.FirstName, Emp.LastName, COUNT(DISTINCT Inv.InvoiceId) AS No_Invoice 
FROM Employee AS Emp
LEFT JOIN Customer AS Cust ON Cust.SupportRepId = Emp.EmployeeId 
LEFT JOIN Invoice AS Inv ON Cust.CustomerId = Inv.CustomerId
GROUP BY EmployeeId
HAVING No_Invoice>0
ORDER BY No_Invoice DESC;


-- 16.Show the following values: Average expense per customer, average expense per invoice, 
-- and average invoices per customer.
-- Consider just active customers (customers that generated at least one invoice)

-- Average expenser pr. customer, average invoices pr. customer 
-- NB: Every customer has >0 invoices
SELECT AVG(avg_no_invoice_pr_cust) AS avg_inv_cust, AVG(avg_exp_pr_cust) AS avg_exp_pr_cust
FROM (
	SELECT COUNT(DISTINCT InvoiceId) AS avg_no_invoice_pr_cust, AVG(Total) AS avg_exp_pr_cust
	FROM INVOICE
	GROUP BY CustomerId
) AS hey;

-- Average expense per invoice
SELECT AVG(Total) AS avg_tot_overall FROM Invoice;


-- 17.We want to know the number of customers that are above the average expense level per customer. (how many?)
SELECT COUNT(*) FROM (
	SELECT CustomerId, AVG(Total) AS avg_pr_cust 
	FROM Invoice 
	GROUP BY CustomerId
    HAVING avg_pr_cust > (
		SELECT AVG(Total) AS avg_total FROM Invoice
    )
) AS Whatever 
;
-- 23 Customers above average expense level


-- 18.We want to know who is the most purchased artist (considering the number of purchased tracks), 
-- who is the most profitable artist (considering the total amount of money generated).
-- and who is the most listened artist (considering purchased song minutes).
-- Show the results in 3 rows in the following format: 
-- ArtistName, Concept('Total Quantity','Total Amount','Total Time (in seconds)'), Value
-- (hint:use the UNION statement)

CREATE TABLE purchase(
SELECT Artist, "Total Quantity:" AS Concept, Count(*) AS Value 
FROM (
	SELECT A.TrackId, A.UnitPrice, Quantity, B.AlbumId, B.Milliseconds AS dur, C.ArtistId, D.Name AS Artist 
	FROM InvoiceLine AS A
	LEFT JOIN Track AS B ON A.TrackId = B.TrackId
	LEFT JOIN Album AS C ON C.AlbumId=B.AlbumId
	LEFT JOIN Artist AS D ON D.ArtistId=C.ArtistId
) AS Whatevs
GROUP BY ArtistId
ORDER BY Value DESC
LIMIT 1
);

CREATE TABLE profit(
SELECT  Artist, "Total Amount:" AS Concept, SUM(UnitPrice) AS Value 
FROM (
SELECT A.TrackId, A.UnitPrice, Quantity, B.AlbumId, C.ArtistId, D.Name AS Artist 
FROM InvoiceLine AS A
LEFT JOIN Track AS B ON A.TrackId = B.TrackId
LEFT JOIN Album AS C ON C.AlbumId=B.AlbumId
LEFT JOIN Artist AS D ON D.ArtistId=C.ArtistId
) AS Hello
GROUP BY Artist
ORDER BY Value DESC
LIMIT 1
);

CREATE TABLE listen(
SELECT Artist, "Total Time (in seconds):" AS Concept, SUM(dur) as Value 
FROM (
	SELECT A.TrackId, A.UnitPrice, Quantity, B.AlbumId, B.Milliseconds AS dur, C.ArtistId, D.Name AS Artist 
	FROM InvoiceLine AS A
	LEFT JOIN Track AS B ON A.TrackId = B.TrackId
	LEFT JOIN Album AS C ON C.AlbumId=B.AlbumId
	LEFT JOIN Artist AS D ON D.ArtistId=C.ArtistId
) AS Whatevs
GROUP BY ArtistId
ORDER BY Value DESC
LIMIT 1
);

SELECT * FROM purchase
UNION 
SELECT * FROM profit
UNION 
SELECT * FROM listen;

-- DROP TABLE purchase;
-- DROP TABLE profit;
-- DROP TABLE listen;
