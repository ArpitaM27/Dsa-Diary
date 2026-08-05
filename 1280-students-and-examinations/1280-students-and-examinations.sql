SELECT
    S.student_id,
    S.student_name,
    S.subject_name,
    COUNT(E.student_id) AS attended_exams
FROM
(
    SELECT *
    FROM Students
    CROSS JOIN Subjects
) S
LEFT JOIN Examinations E
ON S.student_id = E.student_id
AND S.subject_name = E.subject_name
GROUP BY
    S.student_id,
    S.student_name,
    S.subject_name
ORDER BY
    S.student_id,
    S.subject_name;