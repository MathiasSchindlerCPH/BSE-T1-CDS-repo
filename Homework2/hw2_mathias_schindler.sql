-- Please add the proper SQL query to follow the instructions below  

-- 1) Select ecommerce as your default database 
USE ecommerce;


-- 2) Show the PK, name, and quantity per unit from all products
SELECT ProductID, ProductName, QuantityPerUnit
FROM products;


-- 3) Show the number of products ever on sale in our stores
SELECT COUNT(DISTINCT ProductName) 
FROM products;
-- 77 products


-- 4) Show the number of products in stock (available right now) in our store
SELECT SUM(DISTINCT unitsinstock) 
FROM products;
-- 2,526 products in stock


--  5) Show the number of products with more orders than stock
SELECT COUNT(DISTINCT ProductName) 
FROM products 
WHERE unitsonorder > unitsinstock ;
-- 14 products


-- 6) List all products available in the store and order them alphabetically from a to z 
-- Show just the first ten products
SELECT * FROM products 
WHERE unitsinstock > 0 
ORDER BY productname 
LIMIT 10; 


--  7) Create a new table called scustomers with all the customers from a country that starts with the letter S
CREATE TABLE scustomers 
SELECT * FROM customers 
WHERE country 
LIKE "S%";


--  8) Delete the previously created table
DROP TABLE scustomers;


--  9) Show how many customer the store has from Mexico
SELECT COUNT(*) 
FROM customers 
WHERE Country = "Mexico";
-- 5 customers from Mexico


-- 10) Show how many different countries our customers come from
SELECT COUNT(DISTINCT Country) 
FROM customers;
-- 21 unique countries


--  11) Show how many customers are from Mexico, Argentina, or Brazil 
--  whose contact title is  Sales Representative or a Sales Manager
SELECT COUNT(DISTINCT CustomerID) FROM customers 
WHERE Country = "Mexico" OR Country = "Argentina" OR Country = "BraziL"
AND ContactTitle = "Sales Represenatative" OR ContactTitle = "Sales Manager";
-- 19 customers are Mexico, Argentina, or Brazil  with title Sales Representative or a Sales Manager


--  12) Show the number of employees that were 50 years old or more 
--  as at 2014-10-06 (you will probably need to use the DATE_FORMAT function) 
SELECT COUNT(EmployeeID) FROM employees 
WHERE DATEDIFF("2014-10-06", BirthDate)/365 > 50;
-- 7 employees 50 or older at 2014-10-06


--  13) Show the age of the oldest employee of the company
--  (hint: use the YEAR and DATE_FORMAT functions)
SELECT MAX(DATEDIFF("2014-10-06", BirthDate)/365) 
FROM employees ;
-- 62 years old


--  14) Show the number of products whose quantity per unit is measured in bottles
SELECT COUNT(DISTINCT ProductName) FROM Products 
WHERE QuantityPerUnit LIKE "%bottle%";
-- 12 products measured in bottles


-- 15) Show the number of customers with a Spanish or British common surname
--  (a surname that ends with -on or -ez)
SELECT COUNT(DISTINCT CustomerID) 
FROM customers 
WHERE ContactName LIKE "%on" 
OR ContactName LIKE "%ez"; 
-- 11 customers w. Spanish or British common surname


--  16) Show how many distinct countries our 
--  customers with a Spanish or British common surname come from
--  (a surname that ends with -on or -ez)
SELECT COUNT(DISTINCT Country)
FROM customers 
WHERE ContactName LIKE "%on" 
OR ContactName LIKE "%ez"; 
-- They come from 7 diiferent countries, which are ARG, UK, SWE, POR, VNZ, US, MEX.


--  17) Show the number of products whose names do not contain the letter 'a'
--  (Note: patterns are not case sensitive)
SELECT COUNT(DISTINCT ProductID)  FROM  products 
WHERE ProductName NOT LIKE "%a%";
-- 19 products do not contain the letter 'a'


--  18) Get the total number of items sold ever.
SELECT SUM(Quantity) FROM order_details;
-- 51,317 items ever sold


--  19) Get the id of all products sold at least one time
SELECT DISTINCT(ProductID) FROM order_details 
WHERE Quantity>0;


--  20) Is there any product that was never sold? Which ones?
SELECT products.productname, order_details.quantity
FROM products 
LEFT JOIN order_details ON products.ProductID = order_details.ProductID
ORDER BY quantity DESC;
-- There do not seem to be any products that were never sold as they are all in order_details
