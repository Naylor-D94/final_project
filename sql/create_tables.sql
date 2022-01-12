START TRANSACTION;

-- Use (swtich to) webapp_db 
USE webapp_db;

-- Drop the Persons table if it exists
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Persons;
DROP TABLE IF EXISTS Credentials;

-- Create the Credentias table and set the uniqe auto_incrementing ID
CREATE TABLE Credentials (
    credId int NOT NULL AUTO_INCREMENT,
    username varchar(255) NOT NULL,
    userpwd varchar(255) NOT NULL,

    PRIMARY KEY (credId)
);

-- Create the Persons table and set the uniqe auto_incrementing ID
CREATE TABLE Persons (
    PersonID int NOT NULL AUTO_INCREMENT,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    email varchar(255) NOT NULL,
    addr varchar(1024),
    credId int NOT NULL,

    PRIMARY KEY (PersonID),
    FOREIGN KEY (credId) REFERENCES Credentials(credId)
);

-- INSERT into Persons (LastName, email) VALUES ('Shams0', 'shams0.mail.com');

-- Create the orders table
CREATE TABLE Orders (
    OrderID int NOT NULL AUTO_INCREMENT,
    OrderNumber int NOT NULL,
    OrderDesc varchar(1024),
    PersonID int NOT NULL,

    PRIMARY KEY (OrderID),
    FOREIGN KEY (PersonID) REFERENCES Persons(PersonID)
);

