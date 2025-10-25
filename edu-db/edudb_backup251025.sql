--
-- PostgreSQL database dump
--

-- Dumped from database version 16.4
-- Dumped by pg_dump version 16.4

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: edudb; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA edudb;


ALTER SCHEMA edudb OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: assignments; Type: TABLE; Schema: edudb; Owner: postgres
--

CREATE TABLE edudb.assignments (
    assignment_id integer NOT NULL,
    lesson_id integer NOT NULL,
    student_id integer,
    submission_text text,
    submission_file_path character varying(255),
    submission_date timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    status character varying(20) DEFAULT 'not_submitted'::character varying,
    auto_check_result jsonb,
    teacher_feedback text,
    teacher_score numeric(5,2),
    checked_by integer,
    check_date timestamp without time zone,
    max_score integer DEFAULT 100
);


ALTER TABLE edudb.assignments OWNER TO postgres;

--
-- Name: assignments_assignment_id_seq; Type: SEQUENCE; Schema: edudb; Owner: postgres
--

CREATE SEQUENCE edudb.assignments_assignment_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE edudb.assignments_assignment_id_seq OWNER TO postgres;

--
-- Name: assignments_assignment_id_seq; Type: SEQUENCE OWNED BY; Schema: edudb; Owner: postgres
--

ALTER SEQUENCE edudb.assignments_assignment_id_seq OWNED BY edudb.assignments.assignment_id;


--
-- Name: groups; Type: TABLE; Schema: edudb; Owner: postgres
--

CREATE TABLE edudb.groups (
    group_id integer NOT NULL,
    group_name character varying(100) NOT NULL
);


ALTER TABLE edudb.groups OWNER TO postgres;

--
-- Name: groups_group_id_seq; Type: SEQUENCE; Schema: edudb; Owner: postgres
--

CREATE SEQUENCE edudb.groups_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE edudb.groups_group_id_seq OWNER TO postgres;

--
-- Name: groups_group_id_seq; Type: SEQUENCE OWNED BY; Schema: edudb; Owner: postgres
--

ALTER SEQUENCE edudb.groups_group_id_seq OWNED BY edudb.groups.group_id;


--
-- Name: lessons; Type: TABLE; Schema: edudb; Owner: postgres
--

CREATE TABLE edudb.lessons (
    lesson_id integer NOT NULL,
    lesson_date date NOT NULL,
    lesson_time time without time zone NOT NULL,
    assignment_number character varying(50) NOT NULL,
    assignment_description text,
    attachment_path character varying(255),
    assignment_deadline date,
    group_id integer,
    subject_id integer
);


ALTER TABLE edudb.lessons OWNER TO postgres;

--
-- Name: lessons_lesson_id_seq; Type: SEQUENCE; Schema: edudb; Owner: postgres
--

CREATE SEQUENCE edudb.lessons_lesson_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE edudb.lessons_lesson_id_seq OWNER TO postgres;

--
-- Name: lessons_lesson_id_seq; Type: SEQUENCE OWNED BY; Schema: edudb; Owner: postgres
--

ALTER SEQUENCE edudb.lessons_lesson_id_seq OWNED BY edudb.lessons.lesson_id;


--
-- Name: students; Type: TABLE; Schema: edudb; Owner: postgres
--

CREATE TABLE edudb.students (
    student_id integer NOT NULL,
    full_name character varying(255) NOT NULL,
    group_id integer
);


ALTER TABLE edudb.students OWNER TO postgres;

--
-- Name: students_student_id_seq; Type: SEQUENCE; Schema: edudb; Owner: postgres
--

CREATE SEQUENCE edudb.students_student_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE edudb.students_student_id_seq OWNER TO postgres;

--
-- Name: students_student_id_seq; Type: SEQUENCE OWNED BY; Schema: edudb; Owner: postgres
--

ALTER SEQUENCE edudb.students_student_id_seq OWNED BY edudb.students.student_id;


--
-- Name: subjects; Type: TABLE; Schema: edudb; Owner: postgres
--

CREATE TABLE edudb.subjects (
    subject_id integer NOT NULL,
    subject_name character varying(100) NOT NULL,
    teacher_id integer
);


ALTER TABLE edudb.subjects OWNER TO postgres;

--
-- Name: subjects_subject_id_seq; Type: SEQUENCE; Schema: edudb; Owner: postgres
--

CREATE SEQUENCE edudb.subjects_subject_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE edudb.subjects_subject_id_seq OWNER TO postgres;

--
-- Name: subjects_subject_id_seq; Type: SEQUENCE OWNED BY; Schema: edudb; Owner: postgres
--

ALTER SEQUENCE edudb.subjects_subject_id_seq OWNED BY edudb.subjects.subject_id;


--
-- Name: teachers; Type: TABLE; Schema: edudb; Owner: postgres
--

CREATE TABLE edudb.teachers (
    teacher_id integer NOT NULL,
    full_name character varying(255) NOT NULL
);


ALTER TABLE edudb.teachers OWNER TO postgres;

--
-- Name: teachers_teacher_id_seq; Type: SEQUENCE; Schema: edudb; Owner: postgres
--

CREATE SEQUENCE edudb.teachers_teacher_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE edudb.teachers_teacher_id_seq OWNER TO postgres;

--
-- Name: teachers_teacher_id_seq; Type: SEQUENCE OWNED BY; Schema: edudb; Owner: postgres
--

ALTER SEQUENCE edudb.teachers_teacher_id_seq OWNED BY edudb.teachers.teacher_id;


--
-- Name: assignments assignment_id; Type: DEFAULT; Schema: edudb; Owner: postgres
--

ALTER TABLE ONLY edudb.assignments ALTER COLUMN assignment_id SET DEFAULT nextval('edudb.assignments_assignment_id_seq'::regclass);


--
-- Name: groups group_id; Type: DEFAULT; Schema: edudb; Owner: postgres
--

ALTER TABLE ONLY edudb.groups ALTER COLUMN group_id SET DEFAULT nextval('edudb.groups_group_id_seq'::regclass);


--
-- Name: lessons lesson_id; Type: DEFAULT; Schema: edudb; Owner: postgres
--

ALTER TABLE ONLY edudb.lessons ALTER COLUMN lesson_id SET DEFAULT nextval('edudb.lessons_lesson_id_seq'::regclass);


--
-- Name: students student_id; Type: DEFAULT; Schema: edudb; Owner: postgres
--

ALTER TABLE ONLY edudb.students ALTER COLUMN student_id SET DEFAULT nextval('edudb.students_student_id_seq'::regclass);


--
-- Name: subjects subject_id; Type: DEFAULT; Schema: edudb; Owner: postgres
--

ALTER TABLE ONLY edudb.subjects ALTER COLUMN subject_id SET DEFAULT nextval('edudb.subjects_subject_id_seq'::regclass);


--
-- Name: teachers teacher_id; Type: DEFAULT; Schema: edudb; Owner: postgres
--

ALTER TABLE ONLY edudb.teachers ALTER COLUMN teacher_id SET DEFAULT nextval('edudb.teachers_teacher_id_seq'::regclass);


--
-- Data for Name: assignments; Type: TABLE DATA; Schema: edudb; Owner: postgres
--

COPY edudb.assignments (assignment_id, lesson_id, student_id, submission_text, submission_file_path, submission_date, status, auto_check_result, teacher_feedback, teacher_score, checked_by, check_date, max_score) FROM stdin;
\.


--
-- Data for Name: groups; Type: TABLE DATA; Schema: edudb; Owner: postgres
--

COPY edudb.groups (group_id, group_name) FROM stdin;
1	ФКТ-224
2	ФКТ-224зао
\.


--
-- Data for Name: lessons; Type: TABLE DATA; Schema: edudb; Owner: postgres
--

COPY edudb.lessons (lesson_id, lesson_date, lesson_time, assignment_number, assignment_description, attachment_path, assignment_deadline, group_id, subject_id) FROM stdin;
1	2025-09-20	10:10:00	1	Задание 1: Ввод, вывод данных. Калькулятор веса	\N	\N	1	1
2	2025-09-27	10:10:00	2	Задание 2: Квадратное уравнение	\N	\N	1	1
3	2025-10-04	10:10:00	3	Задание 3: Перегрузка методов	\N	\N	1	1
4	2025-10-11	10:10:00	4	Задание 4: Расстояние от точки до отрезка	\N	\N	1	1
\.


--
-- Data for Name: students; Type: TABLE DATA; Schema: edudb; Owner: postgres
--

COPY edudb.students (student_id, full_name, group_id) FROM stdin;
1	Гусятников Павел Иванович	1
2	Дмитриева Дарья Александровна	1
3	Зайкова Ксения Евгеньевна	1
4	Калганов Василий Александрович	1
5	Куклина Мария Анатольевна	1
6	Патласов Николай Дмитриевич	1
7	Пискунова Карина Николаевна	1
8	Подкорытов Тихомир Алексеевич	1
9	Рыбников Андрей Александрович	1
10	Снегирёв Владислав Сергеевич	1
11	Соколов Степан Константинович	1
12	Солохин Марк Сергеевич	1
13	Ушатов Игорь Олегович	1
14	Шкарбун Дмитрий Сергеевич	1
15	Щеглов Николай Сергеевич	1
16	Юсупов Егор Эльмарович	1
\.


--
-- Data for Name: subjects; Type: TABLE DATA; Schema: edudb; Owner: postgres
--

COPY edudb.subjects (subject_id, subject_name, teacher_id) FROM stdin;
1	Алгоритмизация и программирование	3
2	Вычислительные системы, сети и телекоммуникации	3
\.


--
-- Data for Name: teachers; Type: TABLE DATA; Schema: edudb; Owner: postgres
--

COPY edudb.teachers (teacher_id, full_name) FROM stdin;
1	Агеносов Александр Васильевич
2	Хмелькова Наталья Владимировна
3	Чернильцев Андрей Германович
\.


--
-- Name: assignments_assignment_id_seq; Type: SEQUENCE SET; Schema: edudb; Owner: postgres
--

SELECT pg_catalog.setval('edudb.assignments_assignment_id_seq', 1, false);


--
-- Name: groups_group_id_seq; Type: SEQUENCE SET; Schema: edudb; Owner: postgres
--

SELECT pg_catalog.setval('edudb.groups_group_id_seq', 2, true);


--
-- Name: lessons_lesson_id_seq; Type: SEQUENCE SET; Schema: edudb; Owner: postgres
--

SELECT pg_catalog.setval('edudb.lessons_lesson_id_seq', 4, true);


--
-- Name: students_student_id_seq; Type: SEQUENCE SET; Schema: edudb; Owner: postgres
--

SELECT pg_catalog.setval('edudb.students_student_id_seq', 16, true);


--
-- Name: subjects_subject_id_seq; Type: SEQUENCE SET; Schema: edudb; Owner: postgres
--

SELECT pg_catalog.setval('edudb.subjects_subject_id_seq', 2, true);


--
-- Name: teachers_teacher_id_seq; Type: SEQUENCE SET; Schema: edudb; Owner: postgres
--

SELECT pg_catalog.setval('edudb.teachers_teacher_id_seq', 3, true);


--
-- Name: assignments assignments_pkey; Type: CONSTRAINT; Schema: edudb; Owner: postgres
--

ALTER TABLE ONLY edudb.assignments
    ADD CONSTRAINT assignments_pkey PRIMARY KEY (assignment_id);


--
-- Name: groups groups_pkey; Type: CONSTRAINT; Schema: edudb; Owner: postgres
--

ALTER TABLE ONLY edudb.groups
    ADD CONSTRAINT groups_pkey PRIMARY KEY (group_id);


--
-- Name: lessons lessons_assignment_number_key; Type: CONSTRAINT; Schema: edudb; Owner: postgres
--

ALTER TABLE ONLY edudb.lessons
    ADD CONSTRAINT lessons_assignment_number_key UNIQUE (assignment_number);


--
-- Name: lessons lessons_pkey; Type: CONSTRAINT; Schema: edudb; Owner: postgres
--

ALTER TABLE ONLY edudb.lessons
    ADD CONSTRAINT lessons_pkey PRIMARY KEY (lesson_id);


--
-- Name: students students_pkey; Type: CONSTRAINT; Schema: edudb; Owner: postgres
--

ALTER TABLE ONLY edudb.students
    ADD CONSTRAINT students_pkey PRIMARY KEY (student_id);


--
-- Name: subjects subjects_pkey; Type: CONSTRAINT; Schema: edudb; Owner: postgres
--

ALTER TABLE ONLY edudb.subjects
    ADD CONSTRAINT subjects_pkey PRIMARY KEY (subject_id);


--
-- Name: teachers teachers_pkey; Type: CONSTRAINT; Schema: edudb; Owner: postgres
--

ALTER TABLE ONLY edudb.teachers
    ADD CONSTRAINT teachers_pkey PRIMARY KEY (teacher_id);


--
-- Name: assignments assignments_checked_by_fkey; Type: FK CONSTRAINT; Schema: edudb; Owner: postgres
--

ALTER TABLE ONLY edudb.assignments
    ADD CONSTRAINT assignments_checked_by_fkey FOREIGN KEY (checked_by) REFERENCES edudb.teachers(teacher_id) ON DELETE SET NULL;


--
-- Name: assignments assignments_lesson_id_fkey; Type: FK CONSTRAINT; Schema: edudb; Owner: postgres
--

ALTER TABLE ONLY edudb.assignments
    ADD CONSTRAINT assignments_lesson_id_fkey FOREIGN KEY (lesson_id) REFERENCES edudb.lessons(lesson_id) ON DELETE CASCADE;


--
-- Name: assignments assignments_student_id_fkey; Type: FK CONSTRAINT; Schema: edudb; Owner: postgres
--

ALTER TABLE ONLY edudb.assignments
    ADD CONSTRAINT assignments_student_id_fkey FOREIGN KEY (student_id) REFERENCES edudb.students(student_id) ON DELETE CASCADE;


--
-- Name: lessons lessons_group_id_fkey; Type: FK CONSTRAINT; Schema: edudb; Owner: postgres
--

ALTER TABLE ONLY edudb.lessons
    ADD CONSTRAINT lessons_group_id_fkey FOREIGN KEY (group_id) REFERENCES edudb.groups(group_id) ON DELETE CASCADE;


--
-- Name: lessons lessons_subject_id_fkey; Type: FK CONSTRAINT; Schema: edudb; Owner: postgres
--

ALTER TABLE ONLY edudb.lessons
    ADD CONSTRAINT lessons_subject_id_fkey FOREIGN KEY (subject_id) REFERENCES edudb.subjects(subject_id) ON DELETE CASCADE;


--
-- Name: students students_group_id_fkey; Type: FK CONSTRAINT; Schema: edudb; Owner: postgres
--

ALTER TABLE ONLY edudb.students
    ADD CONSTRAINT students_group_id_fkey FOREIGN KEY (group_id) REFERENCES edudb.groups(group_id) ON DELETE SET NULL;


--
-- Name: subjects subjects_teacher_id_fkey; Type: FK CONSTRAINT; Schema: edudb; Owner: postgres
--

ALTER TABLE ONLY edudb.subjects
    ADD CONSTRAINT subjects_teacher_id_fkey FOREIGN KEY (teacher_id) REFERENCES edudb.teachers(teacher_id) ON DELETE SET NULL;


--
-- PostgreSQL database dump complete
--

