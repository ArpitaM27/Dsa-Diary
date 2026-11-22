SELECT ROUND(
    COUNT(*) * 1.0 /
    (SELECT COUNT(DISTINCT player_id) FROM Activity),
    2
) AS fraction
FROM (
    SELECT player_id, MIN(event_date) AS first_login
    FROM Activity
    GROUP BY player_id
) first
WHERE EXISTS (
    SELECT 1
    FROM Activity a2
    WHERE a2.player_id = first.player_id
      AND a2.event_date = DATE_ADD(first.first_login, INTERVAL 1 DAY)
);