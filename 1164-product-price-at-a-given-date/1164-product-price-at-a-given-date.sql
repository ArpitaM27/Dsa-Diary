SELECT p.product_id, p.new_price as price
FROM Products p
JOIN (
    SELECT product_id, MAX(change_date) AS latest_date
    FROM Products
    WHERE change_date <= '2019-08-16'
    GROUP BY product_id
) s
ON p.product_id = s.product_id
AND p.change_date = s.latest_date
UNION
    SELECT product_id, 10 AS price
FROM Products
WHERE product_id NOT IN (
    SELECT product_id
    FROM Products
    WHERE change_date <= '2019-08-16'
);