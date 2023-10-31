SELECT subjects.name AS course
FROM students
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.id
WHERE students.id = 25 -- id студента
  AND subjects.teacher_id = 3; -- id викладача