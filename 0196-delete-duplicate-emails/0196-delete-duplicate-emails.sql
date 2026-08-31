DELETE p
FROM Person p
JOIN Person e
ON p.email = e.email
AND p.id > e.id;