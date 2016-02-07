-- Query 1: Show the total sales (quantity sold and
-- dollar value) for each customer

SELECT c.customer_id, c.customer_name, sum(s.quantity) quantity_sold , sum(s.price) dollar_value
FROM sales.sale s JOIN sales.customer c ON s.customer_id = c.customer_id
GROUP BY c.customer_id, c.customer_name
ORDER BY dollar_value DESC;


-- Query 2: Show the total sales for each state.
SELECT st.state_name, sum(s.quantity) quantity_sold, sum(s.price) dollar_value
FROM sales.sale s 
JOIN sales.customer c ON s.customer_id = c.customer_id
JOIN sales.state st ON st.state_id = c.state_id
GROUP BY st.state_name;

-- Query 3: Show the total sales for each product, for a given customer. Only products that were actually
-- bought by the given customer. Order by dollar value.

SELECT cusProTot.customer_id, cusProTot.product_id, stotal, dollar_value, p.product_name, c.customer_name
FROM     
(
	SELECT c.customer_id,p.product_id,SUM(s.quantity) sTotal,SUM(s.price) dollar_value
	FROM sales.customer c
	JOIN sales.sale s
	ON  s.customer_id = c.customer_id
	JOIN sales.product p
	ON  s.product_id = p.product_id
	WHERE c.customer_name = 'Stefanie Alexander'
	GROUP BY c.customer_id, p.product_id
) cusProTot
JOIN sales.customer c
ON  cusProTot.customer_id = c.customer_id
JOIN sales.product p
ON  p.product_id = cusProTot.product_id
ORDER BY dollar_value DESC;

-- Query 4: Show the total sales for each product and customer. Order by dollar value.

SELECT c.customer_id, c.customer_name, p.product_name, sum(price) as dollar_value
FROM sales.sale s JOIN sales.customer c ON s.customer_id = c.customer_id
JOIN sales.product p ON p.product_id = s.product_id
GROUP BY c.customer_id, c.customer_name, p.product_name
ORDER by dollar_value DESC;

-- Query 5: Show the total sales for each product category and state.
SELECT cu.state_id, c.category_id, SUM(s.price) total_sales
FROM sales.sale s, sales.category c, sales.product p, sales.customer cu
WHERE s.product_id = p.product_id 	
AND p.category_id = c.category_id 
AND s.customer_id = cu.customer_id
GROUP BY cu.state_id, c.category_id;


-- Query 6: For each one of the top 20 product categories and top 20 customers, it returns a tuple (top
-- product, top customer, quantity sold, dollar value)

with top_20_categories as 
(
	select c.category_id, c.category_name, sum(s.quantity) quantity_sold, sum(s.price) dollar_value
	from sales.sale as s
	join sales.product as p on s.product_id = p.product_id
	join sales.category as c on p.category_id = c.category_id
	group by c.category_id, c.category_name
	order by dollar_value DESC
	limit 20
),
top_20_customers as 
(
	select CUS.customer_id, CUS.customer_name, sum(s.quantity) as quantity_sold, sum(s.price) dollar_value
	from sales.sale as s
	join sales.customer as CUS on s.customer_id=CUS.customer_id
	group by CUS.customer_id, CUS.customer_name
	order by dollar_value DESC
	limit 20
)
select tcat.category_name as top_category, tc.customer_name as top_customer, sum(s.quantity) quantity_sold, sum(s.price) dollar_value
from sales.sale s
join sales.product as p on s.product_id=p.product_id
join top_20_categories as tcat on p.category_id=tcat.category_id
join top_20_customers as tc on s.customer_id=tc.customer_id
group by tcat.category_name, tc.customer_name
order by dollar_value DESC;