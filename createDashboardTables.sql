CREATE TABLE Users (
	user_id INT AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(100) NOT NULL,
    user_email VARCHAR(100) UNIQUE
    );

CREATE TABLE Students (
    studentId VARCHAR(100) PRIMARY KEY
);

CREATE TABLE GateEvents (
    eventId INT AUTO_INCREMENT PRIMARY KEY,
    frontgateid VARCHAR(100),
    studentId VARCHAR(100),
    eventType ENUM('ENTER', 'EXIT'),
    eventTime DATETIME NOT NULL,
    FOREIGN KEY (studentId) REFERENCES Students(studentId),
    INDEX (eventTime)
);

CREATE TABLE Departments (
    department_id INT AUTO_INCREMENT PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL,
    department_code VARCHAR(20) UNIQUE,
    faculty_head VARCHAR(100),
    office_location VARCHAR(100)
);

CREATE TABLE Room (
    reservation_id INT AUTO_INCREMENT PRIMARY KEY,
    room_name VARCHAR(30),
    is_available VARCHAR(30) DEFAULT 'available',
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

CREATE TABLE RoomReserved (
    reservation_id INT AUTO_INCREMENT PRIMARY KEY,
    room_id INT,
    reservation_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (room_id) REFERENCES Room(reservation_id)
);

CREATE TABLE BookLocator (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(500) NOT NULL,
    author VARCHAR(100),
    isbn VARCHAR(20) UNIQUE,
    shelf_location VARCHAR(50),
    availability_status VARCHAR(20) DEFAULT 'available'
);

CREATE TABLE Printer(
	printer_id INT AUTO_INCREMENT PRIMARY KEY,
    printer_name VARCHAR(50) NOT NULL,
    curr_status VARCHAR(30) DEFAULT 'available',
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
    );

CREATE TABLE PrinterUsage (
    usage_id INT AUTO_INCREMENT PRIMARY KEY,
    pages_printed INT,
    print_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    user_id INT,
    printer_id INT,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (printer_id) REFERENCES Printer(printer_id)
);
