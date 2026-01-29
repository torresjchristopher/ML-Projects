-- Load data into MEMBERSHIP_TYPE table
LOAD DATA INFILE '/var/lib/mysql-files/membership_type.csv'
INTO TABLE MEMBERSHIP_TYPE
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(typeID, typeName);

-- Load data into MEMBERS table
LOAD DATA INFILE '/var/lib/mysql-files/members.csv'
INTO TABLE MEMBERS
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(memberID, name, contactInfo, typeID);

-- Load data into EVENTS table
LOAD DATA INFILE '/var/lib/mysql-files/events.csv'
INTO TABLE EVENTS
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(eventID, eventName, eventDate, location);

-- Load data into PAYMENTS table
LOAD DATA INFILE '/var/lib/mysql-files/payments.csv'
INTO TABLE PAYMENTS
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(paymentID, memberID, amount, paymentDate);

-- Load data into ATTENDS table
LOAD DATA INFILE '/var/lib/mysql-files/attends.csv'
INTO TABLE ATTENDS
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(memberID, eventID);

-- Load data into WORKER table
LOAD DATA INFILE '/var/lib/mysql-files/worker.csv'
INTO TABLE WORKER
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(workerID, name, role);

-- Load data into ORGANIZES table
LOAD DATA INFILE '/var/lib/mysql-files/organizes.csv'
INTO TABLE ORGANIZES
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(workerID, eventID);
