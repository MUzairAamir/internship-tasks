--  Create Database
CREATE DATABASE UniversityDB;

--  Select Database
USE UniversityDB;
-- Create Students table
CREATE TABLE Students (
    student_id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    department VARCHAR(100)
);

-- Create Courses table
CREATE TABLE Courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100),
    credit_hours INT,
    grade VARCHAR(5)
);

-- Create Enrollments table
CREATE TABLE Enrollments (
    enrollment_id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    enrollment_date DATE,

    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);


-- Insert Students
INSERT INTO Students VALUES
(1, 'Ali', 'ali@gmail.com', 'CS'),
(2, 'Uzair', 'uzair@gmail.com', 'CS'),
(3, 'Ahmed', 'ahmed@gmail.com', 'SE'),
(4, 'Hassan', 'hassan@gmail.com', 'CS');


-- Insert Courses
INSERT INTO Courses VALUES
(101, 'Database Systems', 3, 'A'),
(102, 'Programming Fundamentals', 3, 'B'),
(103, 'Computer Networks', 3, 'A'),
(104, 'Artificial Intelligence', 3, 'A');


-- Insert Enrollments
INSERT INTO Enrollments VALUES
(1, 1, 101, '2026-09-01'),
(2, 2, 101, '2026-09-01'),
(3, 3, 102, '2026-09-02'),
(4, 4, 101, '2026-09-03'),
(5, 1, 102, '2026-09-02');


--  List students in a given course
SELECT s.student_id, s.name, s.email
FROM Students s
JOIN Enrollments e
    ON s.student_id = e.student_id
JOIN Courses c
    ON e.course_id = c.course_id
WHERE c.course_name = 'Database Systems';


--  Count students per course
SELECT c.course_id,
       c.course_name,
       COUNT(e.student_id) AS student_count
FROM Courses c
LEFT JOIN Enrollments e
    ON c.course_id = e.course_id
GROUP BY c.course_id, c.course_name;


--  Find courses with zero enrollments
SELECT c.course_id,
       c.course_name
FROM Courses c
LEFT JOIN Enrollments e
    ON c.course_id = e.course_id
WHERE e.enrollment_id IS NULL;