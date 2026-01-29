
-- ========================================
-- Create table: MEMBERSHIP_TYPE
-- ========================================
CREATE TABLE MEMBERSHIP_TYPE (
  typeID INT PRIMARY KEY,
  typeName VARCHAR(100)
);

-- ========================================
-- Create table: MEMBERS
-- ========================================
CREATE TABLE MEMBERS (
  memberID INT PRIMARY KEY,
  name VARCHAR(100),
  contactInfo VARCHAR(100),
  typeID INT,
  FOREIGN KEY (typeID) REFERENCES MEMBERSHIP_TYPE(typeID)
);

-- ========================================
-- Create table: PAYMENTS
-- ========================================
CREATE TABLE PAYMENTS (
  paymentID INT PRIMARY KEY AUTO_INCREMENT,
  memberID INT,
  amount DECIMAL(10,2),
  paymentDate DATE,
  FOREIGN KEY (memberID) REFERENCES MEMBERS(memberID)
);

-- ========================================
-- Create table: EVENTS
-- ========================================
CREATE TABLE EVENTS (
  eventID INT PRIMARY KEY,
  eventName VARCHAR(100),
  eventDate DATE,
  location VARCHAR(100)
);

-- ========================================
-- Create table: WORKER
-- ========================================
CREATE TABLE WORKER (
  workerID INT PRIMARY KEY,
  name VARCHAR(100),
  role VARCHAR(50)
);

-- ========================================
-- Create table: ATTENDS (junction table between MEMBERS and EVENTS)
-- ========================================
CREATE TABLE ATTENDS (
  memberID INT,
  eventID INT,
  PRIMARY KEY (memberID, eventID),
  FOREIGN KEY (memberID) REFERENCES MEMBERS(memberID),
  FOREIGN KEY (eventID) REFERENCES EVENTS(eventID)
);

-- ========================================
-- Create table: ORGANIZES (junction table between WORKER and EVENTS)
-- ========================================
CREATE TABLE ORGANIZES (
  workerID INT,
  eventID INT,
  PRIMARY KEY (workerID, eventID),
  FOREIGN KEY (workerID) REFERENCES WORKER(workerID),
  FOREIGN KEY (eventID) REFERENCES EVENTS(eventID)
);
