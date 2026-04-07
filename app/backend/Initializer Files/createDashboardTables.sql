CREATE TABLE IF NOT EXISTS Users (
	user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_name VARCHAR(100) NOT NULL,
    user_email VARCHAR(100) UNIQUE,
    user_role TEXT
);

CREATE TABLE IF NOT EXISTS Departments (
    department_id INTEGER PRIMARY KEY AUTOINCREMENT,
    department_name VARCHAR(100) NOT NULL,
    department_code VARCHAR(20) UNIQUE,
    faculty_head VARCHAR(100),
    office_location VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS RoomReservation (
    reservation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    purpose TEXT,
    reservation_date DATE DEFAULT CURRENT_DATE,
    start_time TIME DEFAULT CURRENT_TIME,
    end_time TIME DEFAULT CURRENT_TIME,
    notes TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    user_id INT,
    room_location TEXT,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (room_location) REFERENCES Room(room_location),
    UNIQUE(reservation_date, start_time, end_time, room_location)
);

CREATE TABLE IF NOT EXISTS Room (
    room_id INTEGER PRIMARY KEY AUTOINCREMENT,
    room_name VARCHAR(30) NOT NULL,
    room_location VARCHAR(30) UNIQUE NOT NULL,
    type TEXT,
    capacity INT,
    status TEXT
);

CREATE TABLE IF NOT EXISTS BookLocator (
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(500) NOT NULL,
    author VARCHAR(100),
    isbn TEXT UNIQUE CHECK(length(isbn) == 13),
    shelf_location VARCHAR(50),
    status TEXT
);

CREATE TABLE IF NOT EXISTS Printer(
	printer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    printer_name VARCHAR(50) NOT NULL,
    status TEXT,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

CREATE TABLE IF NOT EXISTS PrinterUsage (
    pages_printed INT,
    print_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    user_id INT,
    printer_id INT,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (printer_id) REFERENCES Printer(printer_id)
);

CREATE TABLE IF NOT EXISTS FeedbackForms (
    form_id INTEGER PRIMARY KEY AUTOINCREMENT,
    form_type TEXT,
    form_content VARCHAR(1000) NOT NULL,
    submission_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);