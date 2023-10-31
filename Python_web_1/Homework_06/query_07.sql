SELECT students.fullname, grades.grade
FROM students
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.id
WHERE students.group_id = 2 -- Ідентифікатор групи
  AND subjects.id = 1;  -- Ідентифікатор предмета