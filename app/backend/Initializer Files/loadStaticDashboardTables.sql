-- Allowed values for status fields in room, printer, book, and type fields in room and feedback
INSERT INTO Status
VALUES
    ('available'),
    ('reserved'),
    ('closed');

INSERT INTO Room_Type
VALUES
    ('individual'),
    ('group');

INSERT INTO Feedback_Type
VALUES
    ('bug report'),
    ('feature request');

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
    
INSERT INTO Room (room_name, room_location, type, capacity)
VALUES
('Group Study Room 1', '210', 'group', 2),
('Group Study Room 2', '211', 'group', 2),
('Group Study Room 3', '212', 'group', 2),
('Group Study Room 4', '213', 'group', 2),
('Group Study Room 5', '369', 'group', 2),
('Group Study Room 6', '370', 'group', 2),
('Group Study Room 7', '371', 'group', 2),
('Group Study Room 8', '372', 'group', 2),
('Group Study Room 9', '373', 'group', 2),
('Group Study Room 10', '374', 'group', 2),
('Group Study Room 11', '453', 'group', 4),
('Group Study Room 12', '454', 'group', 4),
('Group Study Room 13', '456', 'group', 4),
('Group Study Room 14', '457', 'group', 4),
('Individual Study Room 1', '204', 'individual', 1),

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
    
    

