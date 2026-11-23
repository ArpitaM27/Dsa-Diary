SELECT department, employee, salary
FROM (
    SELECT 
        e.name AS employee,
        e.salary AS salary,
        d.name AS department,
        DENSE_RANK() OVER (
            PARTITION BY d.name
            ORDER BY salary DESC
        ) AS rnk
    FROM Employee e
    JOIN Department d
        ON e.departmentId = d.id
) t
WHERE rnk <= 3;