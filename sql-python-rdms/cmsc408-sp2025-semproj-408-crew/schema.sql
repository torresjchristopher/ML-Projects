-- ========================================
-- Create table: MEMBERSHIP_TYPE
-- Stores different types of memberships (e.g., Gold, Silver)
-- ========================================
CREATE TABLE MEMBERSHIP_TYPE (
  typeID INT PRIMARY KEY,                   -- Unique ID for the membership type
  typeName VARCHAR(100)                     -- Name of the membership type
);

-- ========================================
-- Create table: MEMBERS
-- Stores member details and their associated membership type
-- ========================================
CREATE TABLE MEMBERS (
  memberID INT PRIMARY KEY,                 -- Unique ID for each member
  name VARCHAR(100),                        -- Member's name
  contactInfo VARCHAR(100),                 -- Email, phone, etc.
  typeID INT,                               -- FK to MEMBERSHIP_TYPE
  FOREIGN KEY (typeID) REFERENCES MEMBERSHIP_TYPE(typeID)
);

-- ========================================
-- Create table: PAYMENTS
-- Stores payment history for members
-- ========================================
CREATE TABLE PAYMENTS (
  paymentID INT PRIMARY KEY AUTO_INCREMENT, -- Unique ID for payment (auto-increment)
  memberID INT,                             -- FK to MEMBERS table
  amount DECIMAL(10, 2),                    -- Amount paid
  paymentDate DATE,                         -- Date of payment
  FOREIGN KEY (memberID) REFERENCES MEMBERS(memberID)
);

-- ========================================
-- Create table: EVENTS
-- Stores information about events (e.g., workshops, galas)
-- ========================================
CREATE TABLE EVENTS (
  eventID INT PRIMARY KEY,                  -- Unique event ID
  eventName VARCHAR(100),                   -- Name of the event
  eventDate DATE,                           -- Date of the event
  location VARCHAR(100)                     -- Location of the event
);

-- ========================================
-- Create table: WORKER
-- Stores staff/worker info who help organize or run events
-- ========================================
CREATE TABLE WORKER (
  workerID INT PRIMARY KEY,                 -- Unique ID for each worker
  name VARCHAR(100),                        -- Worker's name
  role VARCHAR(50)                          -- Role (e.g., Manager, Volunteer)
);

-- ========================================
-- Create table: ATTENDS
-- Many-to-many relationship between MEMBERS and EVENTS
-- Shows which members attended which events
-- ========================================
CREATE TABLE ATTENDS (
  memberID
