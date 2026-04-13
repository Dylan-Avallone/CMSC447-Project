INSERT INTO Users (user_name, user_email, user_password)
VALUES
    ('Ryan', 'ryano3@umbc.edu', 'password'),
    ('Ava Johnson', 'avaj@umbc.edu', 'password'),
    ('Marcus Lee', 'mlee2@umbc.edu', 'password'),
    ('Sophia Patel', 'spatel4@umbc.edu', 'password'),
    ('Daniel Kim', 'dkim7@umbc.edu', 'password');

INSERT INTO Departments (department_name, department_code, faculty_head, office_location)
VALUES
    ('Computer Science', 'CS', 'Dr. Mohamed Younis', 'ITE 325'),
    ('Chemistry', 'CHEM', 'Dr. Brian Cullum', 'MEYR 243B'),
    ('Physics', 'PHYS', 'Dr. Matthew Pelton', 'Physics 218'),
	('Mathematics & Statistics', 'MATH', 'Dr. Andrei Draganescu', 'MP 406'),
	('Biological Sciences', 'BIOL', 'Dr. Kevin Omland', 'BS 425'),
	('Philosophy', 'PHIL', 'Dr. Jessica Pfeifer', 'PAHB 452'),
	('Mechanical Engineering', 'MECH', 'Dr. Ruey-Hung Chen', 'ENG 210B'),
	('Information Systems', 'IS', 'Dr. Zhiyuan Chen', 'ITE 404G'),
	('Chemical, Biochemical & Environmental Engineering', 'CBEE', 'Dr. Mark R. Marten', 'ENG 314'),
	('History', 'HIST', 'Dr. Amy Froide', 'PAHB 217'),
	('Psychology', 'PSYC', 'Dr. Lira Yoon', 'MP 312'),
	('Sociology, Anthropology, and Public Health', 'SAPH', 'Dr. Andrea Kalfoglou', 'PUP 233');
    
INSERT INTO Room (room_name, room_location, capacity, room_type)
VALUES
    ('Library Study Room A', 'First Floor - East Wing', 4, 'Study Room'),
    ('Library Study Room B', 'First Floor - East Wing', 6, 'Study Room'),
    ('Library Collaboration Room 1', 'Second Floor - North Wing', 8, 'Collaboration Room'),
    ('Library Collaboration Room 2', 'Second Floor - North Wing', 10, 'Collaboration Room'),
    ('Library Conference Room', 'Third Floor - Admin Area', 12, 'Conference Room'),
    ('Digital Media Lab', 'Second Floor - Technology Center', 16, 'Lab');

INSERT INTO RoomReservations
(room_id, user_id, purpose, reservation_date, start_time, end_time, status, notes)
VALUES
    (1, 1, 'Faculty research meeting', '2026-03-28', '09:00:00', '10:30:00', 'Completed', 'Weekly coordination meeting'),
    (2, 2, 'Student study group', '2026-03-29', '13:00:00', '15:00:00', 'Completed', 'CMSC exam review'),
    (3, 3, 'Department planning session', '2026-03-31', '10:00:00', '11:30:00', 'Approved', 'Quarterly planning discussion'),
    (4, 4, 'Capstone team meeting', '2026-03-31', '14:00:00', '16:00:00', 'Approved', 'Sprint planning'),
    (1, 5, 'Workshop preparation', '2026-04-01', '08:30:00', '10:00:00', 'Approved', 'Prepare event materials'),
    (5, 2, 'Interview session', '2026-04-01', '11:00:00', '12:00:00', 'Pending', 'Candidate interview'),
    (5, 2, 'Interview prep session', '2026-05-01', '10:00:00', '12:00:00', 'Pending', 'Mock interview'),
    (5, 2, 'Student club mmeeting', '2026-05-07', '08:00:00', '12:00:00', 'Pending', 'Project creation meeting'),
    (2, 1, 'Faculty office hours overflow', '2026-04-02', '15:00:00', '17:00:00', 'Approved', 'Overflow seating'),
    (3, 4, 'Student organization meeting', '2026-04-03', '18:00:00', '19:30:00', 'Pending', 'Club transition meeting'),
    (4, 3, 'Library orientation session', '2026-04-05', '09:30:00', '11:00:00', 'Approved', 'Orientation for new workers'),
    (6, 5, 'Digital tools workshop', '2026-04-06', '13:30:00', '15:00:00', 'Approved', 'Workshop on media tools');

INSERT INTO BookLocator (title, author, isbn, shelf_location, availability_status)
VALUES
	('The Great Gatsby', 'F. Scott Fitzgerald', '9780743273565', 'FIC-FITZ-001', 'Available'),
	('A Brief History of Time', 'Stephen Hawking', '9780553380163', 'SCI-HAWK-502', 'Checked Out'),
	('Thinking, Fast and Slow', 'Daniel Kahneman', '9780374275631', 'PSY-KAHN-212', 'Available'),
	('The Immortal Life of Henrietta Lacks', 'Rebecca Skloot', '9781400052189', 'BIO-SKLO-109', 'Available'),
	('The 7 Habits of Highly Effective People', 'Stephen R. Covey', '9781982137274', 'SELF-COVE-881', 'Available'),
	('Educated', 'Tara Westover', '9780399590504', 'MEM-WEST-304', 'Checked Out'),
	('The Silent Patient', 'Alex Michaelides', '9781250301697', 'MYS-MICH-442', 'Available'),
	('Atomic Habits', 'James Clear', '9780735211292', 'SELF-CLEA-773', 'Available'),
	('The Overstory', 'Richard Powers', '9780393356687', 'FIC-POWE-115', 'Available'),
	('Sapiens: A Brief History of Humankind', 'Yuval Noah Harari', '9780062316097', 'HIST-HARA-601', 'Checked Out'),
	('Project Hail Mary', 'Andy Weir', '9780593135204', 'SCI-WEIR-902', 'Available'),
	('Killers of the Flower Moon', 'David Grann', '9780385534246', 'NF-GRAN-127', 'Available'),
	('The Body Keeps the Score', 'Bessel van der Kolk', '9780143127741', 'MED-KOLK-554', 'Available'),
	('Circe', 'Madeline Miller', '9780316556347', 'MYTH-MILL-219', 'Checked Out'),
	('Quiet: The Power of Introverts', 'Susan Cain', '9780307352156', 'PSY-CAIN-332', 'Available');

INSERT INTO Printer (printer_name, printer_location, printer_model, curr_status, toner_level, paper_level, last_maintenance)
VALUES
    ('Printer A', 'First Floor - Lobby', 'HP LaserJet Pro 4001', 'Available', 82, 76, '2026-03-15'),
    ('Printer B', 'First Floor - Study Area', 'Canon imageCLASS MF455dw', 'Busy', 64, 52, '2026-03-10'),
    ('Printer C', 'Second Floor - Computer Lab', 'Brother HL-L6415DW', 'Available', 91, 88, '2026-03-20'),
    ('Printer D', 'Second Floor - Quiet Zone', 'Xerox B315', 'Maintenance', 20, 34, '2026-03-28'),
    ('Printer E', 'Third Floor - Admin Office', 'Lexmark MS431dn', 'Offline', 48, 15, '2026-03-05');

INSERT INTO PrinterUsage (pages_printed, print_time, job_status, printer_id)
VALUES
    (3,  '2026-03-30 09:15:00', 'Completed', 1),
    (12, '2026-03-30 10:05:00', 'Completed', 2),
    (7,  '2026-03-30 11:20:00', 'Completed', 3),
    (20, '2026-03-30 13:45:00', 'Completed', 1),
    (5,  '2026-03-30 15:10:00', 'Completed', 2),
    (18, '2026-03-31 08:30:00', 'Completed', 3),
    (9,  '2026-03-31 09:40:00', 'Completed', 1),
    (15, '2026-03-31 11:00:00', 'Completed', 2),
    (4,  '2026-03-31 12:25:00', 'Completed', 3),
    (11, '2026-03-31 14:50:00', 'Queued', 4),
    (6,  '2026-03-31 16:05:00', 'Failed', 5),
    (14, '2026-03-31 17:40:00', 'Completed', 1);


INSERT INTO LibraryEntryLog (entry_time, entry_count)
VALUES
    
    ('2026-04-07 08:00:00', 18),
    ('2026-04-07 09:00:00', 34),
    ('2026-04-07 10:00:00', 41),
    ('2026-04-07 11:00:00', 52),
    ('2026-04-07 12:00:00', 44),
    ('2026-04-07 13:00:00', 39),
    ('2026-04-07 14:00:00', 31),
    ('2026-04-07 15:00:00', 29),
    ('2026-04-07 16:00:00', 37),
    ('2026-04-07 17:00:00', 34),
    ('2026-04-07 18:00:00', 27),
    ('2026-04-07 19:00:00', 22),

    
    ('2026-04-08 08:00:00', 15),
    ('2026-04-08 09:00:00', 28),
    ('2026-04-08 10:00:00', 36),
    ('2026-04-08 11:00:00', 46),
    ('2026-04-08 12:00:00', 53),
    ('2026-04-08 13:00:00', 49),
    ('2026-04-08 14:00:00', 33),
    ('2026-04-08 15:00:00', 26),
    ('2026-04-08 16:00:00', 30),
    ('2026-04-08 17:00:00', 32),
    ('2026-04-08 18:00:00', 24),
    ('2026-04-08 19:00:00', 18),

    
    ('2026-04-09 08:00:00', 20),
    ('2026-04-09 09:00:00', 39),
    ('2026-04-09 10:00:00', 48),
    ('2026-04-09 11:00:00', 57),
    ('2026-04-09 12:00:00', 61),
    ('2026-04-09 13:00:00', 55),
    ('2026-04-09 14:00:00', 38),
    ('2026-04-09 15:00:00', 32),
    ('2026-04-09 16:00:00', 36),
    ('2026-04-09 17:00:00', 43),
    ('2026-04-09 18:00:00', 31),
    ('2026-04-09 19:00:00', 26),

    
    ('2026-04-10 08:00:00', 17),
    ('2026-04-10 09:00:00', 31),
    ('2026-04-10 10:00:00', 40),
    ('2026-04-10 11:00:00', 49),
    ('2026-04-10 12:00:00', 56),
    ('2026-04-10 13:00:00', 51),
    ('2026-04-10 14:00:00', 35),
    ('2026-04-10 15:00:00', 28),
    ('2026-04-10 16:00:00', 34),
    ('2026-04-10 17:00:00', 37),
    ('2026-04-10 18:00:00', 29),
    ('2026-04-10 19:00:00', 21),

    
    ('2026-04-11 08:00:00', 16),
    ('2026-04-11 09:00:00', 29),
    ('2026-04-11 10:00:00', 37),
    ('2026-04-11 11:00:00', 45),
    ('2026-04-11 12:00:00', 50),
    ('2026-04-11 13:00:00', 43),
    ('2026-04-11 14:00:00', 30),
    ('2026-04-11 15:00:00', 24),
    ('2026-04-11 16:00:00', 26),
    ('2026-04-11 17:00:00', 28),
    ('2026-04-11 18:00:00', 19),
    ('2026-04-11 19:00:00', 14),

    
    ('2026-04-12 08:00:00', 8),
    ('2026-04-12 09:00:00', 14),
    ('2026-04-12 10:00:00', 21),
    ('2026-04-12 11:00:00', 29),
    ('2026-04-12 12:00:00', 37),
    ('2026-04-12 13:00:00', 42),
    ('2026-04-12 14:00:00', 35),
    ('2026-04-12 15:00:00', 28),
    ('2026-04-12 16:00:00', 22),
    ('2026-04-12 17:00:00', 19),
    ('2026-04-12 18:00:00', 15),
    ('2026-04-12 19:00:00', 11);