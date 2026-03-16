CREATE TABLE IF NOT EXISTS Users (
	user_id INT AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(100) NOT NULL,
    user_email VARCHAR(100) UNIQUE
    );

CREATE TABLE IF NOT EXISTS Departments (
    department_id INT AUTO_INCREMENT PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL,
    department_code VARCHAR(20) UNIQUE,
    faculty_head VARCHAR(100),
    office_location VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS Room (
    reservation_id INT AUTO_INCREMENT PRIMARY KEY,
    room_name VARCHAR(30),
    is_available VARCHAR(30) DEFAULT 'available',
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

CREATE TABLE IF NOT EXISTS RoomReserved (
    reservation_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

CREATE TABLE IF NOT EXISTS BookLocator (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(500) NOT NULL,
    author VARCHAR(100),
    isbn VARCHAR(20) UNIQUE,
    shelf_location VARCHAR(50),
    availability_status VARCHAR(20) DEFAULT 'available'
);

CREATE TABLE IF NOT EXISTS Printer(
	printer_id INT AUTO_INCREMENT PRIMARY KEY,
    printer_name VARCHAR(50) NOT NULL,
    curr_status VARCHAR(30) DEFAULT 'available',
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