CREATE DATABASE auda_database;

USE auda_database;

CREATE TABLE clients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    phone VARCHAR(20)
);

CREATE TABLE vehicles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    brand VARCHAR(50) NOT NULL,
    model VARCHAR(50) NOT NULL,
    year INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

CREATE TABLE appointments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    appointment_date DATETIME NOT NULL,
    client_id INT,
    vehicle_id INT,
    type ENUM('PURCHASE', 'SALE') NOT NULL,
    FOREIGN KEY (client_id) REFERENCES clients(id),
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(id)
);

INSERT INTO clients (first_name, last_name, email, phone) VALUES
('Carlos', 'Monzon', 'carlos.monzon@example.com', '1234567890'),
('Ana', 'Gómez', 'ana.gomez@example.com', '2345678901'),
('Carlos', 'Martínez', 'carlos.martinez@example.com', '3456789012'),
('María', 'López', 'maria.lopez@example.com', '4567890123');

INSERT INTO vehicles (brand, model, year, price) VALUES
('Chevrolet', 'Camaro', 2021, 40000.00),
('Chevrolet', 'Malibu', 2020, 25000.00),
('Chevrolet', 'Impala', 2019, 28000.00),
('Chevrolet', 'Tahoe', 2018, 50000.00);

INSERT INTO appointments (appointment_date, client_id, vehicle_id, type) VALUES
('2023-06-15 10:00:00', 1, 1, 'PURCHASE'),
('2023-06-16 11:00:00', 2, 2, 'SALE'),
('2023-06-17 12:00:00', 3, 3, 'PURCHASE'),
('2023-06-18 13:00:00', 4, 4, 'SALE');
