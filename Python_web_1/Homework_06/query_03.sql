SELECT groups.name, subjects.name AS subject, ROUND(AVG(grades.grade), 2) AS average_grade
FROM students
JOIN groups ON students.id = groups.id
JOIN grades ON students.id = grades.id
JOIN subjects ON grades.id = subjects.id
WHERE subjects.id = 2  -- {id} ідентифікатор редмету
GROUP BY groups.name, subjects.name;