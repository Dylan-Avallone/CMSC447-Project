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

INSERT INTO Printer (printer_name, curr_status)
VALUES
	('Printer 1', 'available'),
	('Printer 2', 'available'),
	('Printer 3', 'available'),
	('Printer 4', 'available'),
	('Printer 5', 'available');

INSERT INTO PrinterUsage (pages_printed, print_time)
VALUES
    (3, datetime('03/18/2026 23:59:48.990')),
    (10, datetime('3/17/2026 6:26:37:.847'));
    
    

