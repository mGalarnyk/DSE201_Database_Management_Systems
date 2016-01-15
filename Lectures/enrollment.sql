-- Create tables for classes, students and enrollment
CREATE TABLE classes (
    id          SERIAL PRIMARY KEY,
    name        TEXT,
    number      TEXT,
    date_code   TEXT,
    start_time  TIME,
    end_time    TIME
);
CREATE TABLE students (
    id          SERIAL PRIMARY KEY,
    pid         TEXT,
    first_name  TEXT,
    last_name   TEXT
);
CREATE TABLE enrollment (
    id          SERIAL PRIMARY KEY,
    class       INTEGER REFERENCES classes (id) NOT NULL,
    student     INTEGER REFERENCES students (id) NOT NULL,
    credits     INTEGER DEFAULT 4
);

-- Insert data into tables
INSERT INTO classes (name, number, date_code, start_time, end_time) VALUES ('Web Stuff', 'MAS201', 'TuTh', '2:00', '3:20');
INSERT INTO classes (name, number, date_code, start_time, end_time) VALUES ('Databases', 'CSE132A', 'TuTh', '3:30', '4:50');
INSERT INTO classes (name, number, date_code, start_time, end_time) VALUES ('Compilers', 'CSE131', 'F', '9:30', '10:50');
INSERT INTO classes (name, number, date_code, start_time, end_time) VALUES ('VLSI', 'CSE121', 'F', '11:00', '12:00');

INSERT INTO students (pid, first_name, last_name) VALUES ('8888888', 'John', 'Smith');
INSERT INTO students (pid, first_name, last_name) VALUES ('1111111', 'Mary', 'Doe');
INSERT INTO students (pid, first_name, last_name) VALUES ('2222222', 'Jay', 'Chen');

INSERT INTO enrollment (class, student, credits) VALUES (1, 1, 4);
INSERT INTO enrollment (class, student, credits) VALUES (1, 2, 3);
INSERT INTO enrollment (class, student, credits) VALUES (4, 3, 4);
INSERT INTO enrollment (class, student, credits) VALUES (1, 3, 3);

-- There is no class with id 3
DELETE FROM classes WHERE id = 3;

-- Verify that data has been inserted correctly
SELECT * FROM classes;
SELECT * FROM students;
SELECT * FROM enrollment;

-- Find first names and last names of all students
SELECT  first_name, last_name
FROM    students;

-- Find all students whose first name is John
SELECT  *
FROM    students
WHERE   first_name = 'John';

-- Find the pid, name and MAS201 credits of students registered for MAS201
SELECT  students.pid, students.first_name, students.last_name, enrollment.credits
FROM    students, enrollment, classes
WHERE   number = 'MAS201'
        AND students.id = student
        AND class = classes.id;

-- Find the other classes taken by MAS201 students
SELECT  c_others.name, first_name, last_name
FROM    classes AS c_201, enrollment AS e_201, students, enrollment AS e_others, classes AS c_others
WHERE   c_201.number = 'MAS201'
        AND c_201.id = e_201.class
        AND e_201.student = students.id
        AND students.id = e_others.student
        AND e_others.class = c_others.id
        AND NOT (c_others.number = 'MAS201')


-- Find the other classes taken by students who take MAS201 (just the classes)
SELECT  DISTINCT c_others.name
FROM    classes AS c_201, enrollment AS e_201, enrollment AS e_others, classes AS c_others
WHERE   c_201.number = 'MAS201'
        AND c_201.id = e_201.class
        AND e_201.student = e_others.student
        AND e_others.class = c_others.id
        AND NOT (c_others.number = 'MAS201')

-- Find the MAS201 students who take a Friday 11:00am class
SELECT  first_name, last_name
FROM    students, enrollment, classes
WHERE   students.id = student
        AND class = classes.id
        AND number = 'MAS201'
        AND students.id IN 
        (
            SELECT  student
            FROM    enrollment, classes
            WHERE   classes.id = class
            AND     date_code = 'F'
            AND     start_time = '11:00' 
        )   

-- Find the enrolled students and total credits for which they have registered
SELECT   students.id, first_name, last_name, SUM(credits)
FROM     students, enrollment
WHERE    students.id = enrollment.student
GROUP BY students.id, first_name, last_name

-- Find all students and total credits for which they have registered
SELECT   students.id, first_name, last_name, SUM(credits)
FROM     students LEFT OUTER JOIN enrollment ON students.id = enrollment.student 
GROUP BY students.id, first_name, last_name

-- Find students that take every class that John Smith takes
SELECT  s.first_name, s.last_name
FROM    students AS s
WHERE   NOT EXISTS 
    (
        SELECT  * 
        FROM    classes AS c
        WHERE   EXISTS 
            (
                SELECT  *
                FROM    enrollment AS ej, students AS j
                WHERE   ej.class = c.id
                        AND ej.student = j.id
                        AND j.first_name = 'John'
                        AND j.last_name = 'Smith'
            )
                AND s.id NOT IN
            (
                SELECT  es.student
                FROM    enrollment AS es
                WHERE   es.class = c.id
            )
    )

-- Drop all tables
DROP TABLE enrollment CASCADE;
DROP TABLE classes CASCADE;
DROP TABLE students CASCADE;
