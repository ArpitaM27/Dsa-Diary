Select name
From Employee
where id in(
    SELECT managerId
FROM Employee
GROUP BY managerId
HAVING COUNT(*) >= 5
)