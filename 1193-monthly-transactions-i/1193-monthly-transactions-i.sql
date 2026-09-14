select DATE_FORMAT(trans_date, '%Y-%m') AS month,
country, count(state) as trans_count,SUM(amount) as trans_total_amount,
SUM(
    CASE
        WHEN state = 'approved' THEN amount
        ELSE 0
    END
) as approved_total_amount,
SUM(CASE
        WHEN state = 'approved' THEN 1
        ELSE 0
    END) as approved_count
    from transactions
    group by country,DATE_FORMAT(trans_date, '%Y-%m')