# my-ddl.sql

## DO NOT RENAME OR OTHERWISE CHANGE THE SECTION TITLES OR ORDER.
## The autograder will look for specific code sections. If it can't find them, you'll get a "0"

# Code specifications.
# 0. Where there a conflict between the problem statement in the google doc and this file, this file wins.
# 1. Complete all sections below.
# 2. Table names must MATCH EXACTLY to schemas provided.
# 3. Define primary keys in each table as appropriate.
# 4. Define foreign keys connecting tables as appropriate.
# 5. Assign ID to skills, people, roles manually (you must pick the ID number!)
# 6. Assign ID in the peopleskills and peopleroles automatically (use auto_increment)
# 7. Data types: ONLY use "int", "varchar(255)", "varchar(4096)" or "date" as appropriate.

# Section 1
# Drops all tables.  This section should be amended as new tables are added.

SET FOREIGN_KEY_CHECKS=0;
DROP TABLE IF EXISTS peopleskills;
DROP TABLE IF EXISTS people;
DROP TABLE IF EXISTS skills;
SET FOREIGN_KEY_CHECKS=1;

# Section 2
# Create skills( id,name, description, tag, url, time_commitment)
# ID, name, description and tag cannot be NULL. Other fields can default to NULL.
# tag is a skill category grouping.  You can assign it based on your skill descriptions.
# time committment offers some sense of how much time was required (or will be required) to gain the skill.
# You can assign the skill descriptions.  Please be creative!

CREATE TABLE skills (
    id int PRIMARY KEY,
    name varchar(256) NOT NULL,
    description varchar(4098) NOT NULL,
    tag varchar(256) NOT NULL,
    url varchar(1024),
    time_commitment varchar(256)
);


# Section 3
# Populate skills
# Populates the skills table with eight skills, their tag fields must exactly contain “Skill 1”, “Skill 2”, etc.
# You can assign skill names.  Please be creative!

INSERT into skills(id, name, description, tag, url, time_commitment) values 
(1, 'Rope Jumping', 'Jumping Rope', 'Skill 1', 'www.google.com', NULL), 
(2, 'Sky Diving', 'Jumping Rope', 'Skill 2', 'www.google.com',NULL),
(3, 'Race Car Driving', 'Jumping Rope', 'Skill 3', 'www.google.com', NULL),
(4, 'Heavy Lifting', 'Jumping Rope', 'Skill 4', 'www.google.com', NULL),
(5, 'Swimmer', 'Jumping Rope', 'Skill 5', 'www.google.com', NULL),
(6, 'Cliff Jumping', 'Jumping Rope', 'Skill 6', 'www.google.com', NULL),
(7, 'Mural Artist', 'Jumping Rope', 'Skill 7', 'www.google.com', NULL),
(8, 'Author', 'Jumping Rope', 'Skill 8', 'www.google.com', NULL);


# Section 4
# Create people( id,first_name, last_name, email, linkedin_url, headshot_url, discord_handle, brief_bio, date_joined)
# ID cannot be null, Last name cannot be null, date joined cannot be NULL.
# All other fields can default to NULL.

CREATE TABLE people (
    id INT,
    first_name VARCHAR(256),
    last_name VARCHAR(256) NOT NULL,
    email VARCHAR(256),
    linkedin_url VARCHAR(1024),
    headshot_url VARCHAR(1024),
    discord_handle VARCHAR(256),
    brief_bio VARCHAR(4096),
    date_joined DATE NOT NULL,
    PRIMARY KEY (id)
);

# Section 5
# Populate people with 10 people.
# Their last names must exactly be “Person 1”, “Person 2”, etc.
# Other fields are for you to assign.

INSERT INTO people (id, first_name, last_name, email, linkedin_url, headshot_url, discord_handle, brief_bio, date_joined)
VALUES
(1, 'Avery', 'Person 1', 'avery1@example.com', 'https://linkedin.com/in/avery1', 'https://example.com/headshots/avery.jpg', '@avery01', 'Fitness enthusiast and tech blogger.', '2025-01-01'),
(2, 'Jordan', 'Person 2', 'jordan2@example.com', 'https://linkedin.com/in/jordan2', 'https://example.com/headshots/jordan.jpg', '@jordan02', 'Mechanical engineer who loves extreme sports.', '2025-01-01'),
(3, 'Taylor', 'Person 3', 'taylor3@example.com', 'https://linkedin.com/in/taylor3', 'https://example.com/headshots/taylor.jpg', '@taylor03', 'Writer and hobbyist swimmer.', '2025-01-01'),
(4, 'Morgan', 'Person 4', 'morgan4@example.com', 'https://linkedin.com/in/morgan4', 'https://example.com/headshots/morgan.jpg', '@morgan04', 'Artist focused on sustainable designs.', '2025-01-01'),
(5, 'Riley', 'Person 5', 'riley5@example.com', 'https://linkedin.com/in/riley5', 'https://example.com/headshots/riley.jpg', '@riley05', 'Racing enthusiast and cliff diver.', '2025-01-01'),
(6, 'Skylar', 'Person 6', 'skylar6@example.com', 'https://linkedin.com/in/skylar6', 'https://example.com/headshots/skylar.jpg', '@skylar06', 'Tech consultant with a passion for flying.', '2025-01-01'),
(7, 'Casey', 'Person 7', 'casey7@example.com', 'https://linkedin.com/in/casey7', 'https://example.com/headshots/casey.jpg', '@casey07', 'Athlete and mural enthusiast.', '2025-01-01'),
(8, 'Quinn', 'Person 8', 'quinn8@example.com', 'https://linkedin.com/in/quinn8', 'https://example.com/headshots/quinn.jpg', '@quinn08', 'Entrepreneur and adventure lover.', '2025-01-01'),
(9, 'Reese', 'Person 9', 'reese9@example.com', 'https://linkedin.com/in/reese9', 'https://example.com/headshots/reese.jpg', '@reese09', 'Freelancer and swimmer.', '2025-01-01'),
(10, 'Parker', 'Person 10', 'parker10@example.com', 'https://linkedin.com/in/parker10', 'https://example.com/headshots/parker.jpg', '@parker10', 'Strength coach and motivational speaker.', '2025-01-01');

COMMIT;

# Section 6
# Create peopleskills( id, skills_id, people_id, date_acquired )
# None of the fields can ba NULL. ID can be auto_increment.

DROP TABLE IF EXISTS peopleskills;

CREATE TABLE peopleskills (

    id INT AUTO_INCREMENT PRIMARY KEY,
    skills_id INT NOT NULL,
    people_id INT NOT NULL,
    date_acquired DATETIME,
    
    FOREIGN KEY (skills_id) REFERENCES skills(id),
    FOREIGN KEY (people_id) REFERENCES people(id)

);



# Section 7
# Populate peopleskills such that:
# Person 1 has skills 1,3,6;
# Person 2 has skills 3,4,5;
# Person 3 has skills 1,5;
# Person 4 has no skills;
# Person 5 has skills 3,6;
# Person 6 has skills 2,3,4;
# Person 7 has skills 3,5,6;
# Person 8 has skills 1,3,5,6;
# Person 9 has skills 2,5,6;
# Person 10 has skills 1,4,5;
# Note that no one has yet acquired skills 7 and 8.
 

 
INSERT INTO peopleskills (people_id, skills_id, date_acquired) VALUES
(1, 1, '2024-01-01'),
(1, 3, '2024-01-01'),
(1, 6, '2024-01-01'),
(2, 3, '2024-01-01'),
(2, 4, '2024-01-01'),
(2, 5, '2024-01-01'),
(3, 1, '2024-01-01'),
(3, 5, '2024-01-01'),
(5, 3, '2024-01-01'),
(5, 6, '2024-01-01'),
(6, 2, '2024-01-01'),
(6, 3, '2024-01-01'),
(6, 4, '2024-01-01'),
(7, 3, '2024-01-01'),
(7, 5, '2024-01-01'),
(7, 6, '2024-01-01'),
(8, 1, '2024-01-01'),
(8, 3, '2024-01-01'),
(8, 5, '2024-01-01'),
(8, 6, '2024-01-01'),
(9, 2, '2024-01-01'),
(9, 5, '2024-01-01'),
(9, 6, '2024-01-01'),
(10, 1, '2024-01-01'),
(10, 4, '2024-01-01'),
(10, 5, '2024-01-01');
COMMIT;