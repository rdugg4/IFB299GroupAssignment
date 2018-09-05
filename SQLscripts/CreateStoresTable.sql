DROP TABLE IF EXISTS Stores;
CREATE table Stores (
	ID INT NOT NULL AUTO_INCREMENT KEY,
    Name VARCHAR(255),
    Address VARCHAR(255),
    Phone VARCHAR(20),
    City VARCHAR(255),
    State VARCHAR(255)
);

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/store.csv' 
INTO TABLE Stores
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;