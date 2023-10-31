SELECT subjects.name AS subject, ROUND(AVG(grades.grade), 2) AS average_grade
FROM subjects
JOIN grades ON subjects.id = grades.subject_id
WHERE subjects.teacher_id = 2  -- id викладача
GROUP BY subjects.name