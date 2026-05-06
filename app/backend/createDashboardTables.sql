CREATE TABLE IF NOT EXISTS Users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_name VARCHAR(100) NOT NULL,
    user_email VARCHAR(100) UNIQUE,
    user_password VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS Departments (
    department_id INTEGER PRIMARY KEY AUTOINCREMENT,
    department_name VARCHAR(100) NOT NULL,
    department_code VARCHAR(20) UNIQUE,
    faculty_head VARCHAR(100),
    office_location VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS Room (
    room_id INTEGER PRIMARY KEY AUTOINCREMENT,
    room_name VARCHAR(50) NOT NULL,
    room_location VARCHAR(100),
    capacity INT,
    room_type VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS RoomReservations (
    reservation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    room_id INT NOT NULL,
    user_id INT NOT NULL,
    purpose VARCHAR(255) NOT NULL,
    reservation_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    status VARCHAR(20) DEFAULT 'Approved',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    notes VARCHAR(500),
    FOREIGN KEY (room_id) REFERENCES Room(room_id),
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

CREATE TABLE IF NOT EXISTS BookLocator (
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(500) NOT NULL,
    author VARCHAR(100),
    isbn VARCHAR(20) UNIQUE,
    shelf_location VARCHAR(50),
    availability_status VARCHAR(20) DEFAULT 'available'
);



CREATE TABLE IF NOT EXISTS Printer (
    printer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    printer_name VARCHAR(50) NOT NULL,
    printer_location VARCHAR(100),
    printer_model VARCHAR(100),
    curr_status VARCHAR(30) DEFAULT 'Available',
    toner_level INT,
    paper_level INT,
    last_maintenance DATE
);

CREATE TABLE IF NOT EXISTS PrinterUsage (
    usage_id INTEGER PRIMARY KEY AUTOINCREMENT,
    pages_printed INT NOT NULL,
    print_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    job_status VARCHAR(30) DEFAULT 'Completed',
    printer_id INT NOT NULL,
    FOREIGN KEY (printer_id) REFERENCES Printer(printer_id)
);

CREATE TABLE IF NOT EXISTS LibraryEntryLog (
    entry_id INTEGER PRIMARY KEY AUTOINCREMENT,
    entry_time DATETIME NOT NULL,
    entry_count INT NOT NULL
);

CREATE TABLE IF NOT EXISTS FeedbackForms (
    form_id INTEGER PRIMARY KEY AUTOINCREMENT,
    form_type VARCHAR(30) DEFAULT 'bug report',
    form_content VARCHAR(1000) NOT NULL,
    submission_time DATETIME DEFAULT CURRENT_TIMESTAMP
  
);