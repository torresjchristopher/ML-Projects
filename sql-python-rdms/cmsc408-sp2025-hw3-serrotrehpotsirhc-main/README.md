# Welcome to Homework 3

## Project Overview 


This project explores **Entity-Relationship (ER) modeling** by defining and visualizing three real-world database scenarios. The project includes:  

- **Scenario Design:** Defining three database scenarios with entities, attributes, and relationships.  
- **Graphical Representation:** Using **Chen's Notation (Graphviz)** and **Crow's Foot Notation (Mermaid)** to model each scenario.  
- **Relational Model Construction:** Converting each ER model into relational schemas.  
- **Design Choices Explanation:** Documenting the rationale behind modeling decisions.  

## Scenarios Modeled  


1. **University Course Enrollment System**  
   - Models students, courses, and professors.  
   - Defines enrollment and teaching relationships.  

2. **Hospital Patient Management System**  
   - Represents patients, doctors, and appointments.  
   - Captures how appointments are scheduled and handled. 

3. **Movie Theater Booking System**  
   - Covers customers, movies, and screenings.  
   - Models how customers book screenings.  

## Graphical Representations


Each scenario is modeled in **two notations**:


- **Chen's Notation** → Illustrates entities, attributes, and relationships with diamonds.  
- **Crow’s Foot Notation** → Shows relationships with cardinality symbols for better database structuring.  

## Relational Models 


Each ER model was transformed into **relational schemas** with: 


- **Tables & Attributes**  
- **Primary and Foreign Keys**  
- **Bridge Tables (where necessary for many-to-many relationships)**  

## **Design Choices**  


### Normalization & Cardinality


- **Many-to-Many Relationships** (e.g., students enrolling in courses, customers booking screenings) were handled using **bridge tables** to avoid redundancy.  
- **One-to-Many Relationships** (e.g., doctors handling appointments, professors teaching courses) were directly mapped using **foreign keys** to maintain **referential integrity**.  

### Graphviz vs. Mermaid 


- **Graphviz (Chen’s Notation)** was used for detailed conceptual modeling, making attribute representation clearer.  
- **Mermaid (Crow’s Foot Notation)** was chosen for **logical database design**, which aligns more closely with relational modeling.  

### Why These Scenarios? 
- They represent common **real-world database applications** used in education, healthcare, and entertainment.  
- They demonstrate **different levels of complexity**, from simple one-to-many relationships (hospital system) to complex many-to-many relationships (course enrollment).  

**Quarto** will render report.qmd in the reports folder into the report.html file. 

**Further examples** found in the example folder!

Thank you! - Christopher Torres