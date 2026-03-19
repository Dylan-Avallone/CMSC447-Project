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
    
INSERT INTO Room (room_name, is_available)
VALUES
('Room 1', 'available'),
('Room 2', 'available'),
('Room 3', 'available'),
('Room 4', 'available'),
('Room 5', 'available');

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
    
    

