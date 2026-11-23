SELECT person_name
FROM (
SELECT
    person_name,
    weight,
    turn,
    SUM(weight) OVER (ORDER BY turn) AS total_weight
    FROM Queue)t
    where total_weight<=1000

order by turn desc 
 limit 1;