START TRANSACTION;

-- Use (swtich to) webapp_db 
USE webapp_db;

-- Drop the Persons table if it exists
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


-- Create the Template table
CREATE TABLE Template (
    race varchar(100) NOT NULL,
    armor varchar(100) NOT NULL,
    weapon varchar(1024) NOT NULL,
    primary_stat varchar(100) NOT NULL
);

