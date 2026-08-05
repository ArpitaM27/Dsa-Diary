SELECT name, unique_id
FROM Employees E
LEFT JOIN EmployeeUNI U
ON E.id = U.id;