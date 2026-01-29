/*select all members*/
SELECT * FROM MEMBERS;


/*list all events*/
SELECT * FROM EVENTS;


/*List all workers and their roles*/

SELECT * FROM WORKER;

/*List all membership types */


SELECT * FROM MEMBERSHIP_TYPE;

/* show all payments made by each member */



SELECT memberID, amount, paymentDate FROM PAYMENTS ORDER BY paymentDate DESC;

               /***JOIN QUERIES*****/


/*show memebrs with their membership type*/

SELECT M.name, MT.typeName
FROM MEMBERS M
JOIN MEMBERSHIP_TYPE MT ON M.typeID = MT.typeID;


/*Show memebers and the events they attended */

SELECT MEM.name AS member_name, E.eventName, E.eventDate
FROM ATTENDS A
JOIN MEMBERS MEM ON A.memberID = MEM.memberID
JOIN EVENTS E ON A.eventID = E.eventID;

/*SHow workers and events they organized */

SELECT W.name AS worker_name, E.eventName, E.eventDate
FROM ORGANIZES O
JOIN WORKER W ON O.workerID = W.workerID
JOIN EVENTS E ON O.eventID = E.eventID;

/*List members and total amount they paid*/

SELECT M.name, SUM(P.amount) AS total_paid
FROM MEMBERS M
JOIN PAYMENTS P ON M.memberID = P.memberID
GROUP BY M.name;


/*Show which events have more than 5 attendees or any amount needed to see */

SELECT E.eventName, COUNT(A.memberID) AS num_attendees
FROM EVENTS E
JOIN ATTENDS A ON E.eventID = A.eventID
GROUP BY E.eventName
HAVING COUNT(A.memberID) > 5;




               /********These are the filter queries *********/


/* Show members who have paid more than $100 or any certain amount */

SELECT M.name, SUM(P.amount) AS total_paid
FROM MEMBERS M
JOIN PAYMENTS P ON M.memberID = P.memberID
GROUP BY M.name
HAVING total_paid > 100;


/* Show events organized by workers with manager role */

SELECT W.name, E.eventName
FROM WORKER W
JOIN ORGANIZES O ON W.workerID = O.workerID
JOIN EVENTS E ON O.eventID = E.eventID
WHERE W.role = 'Manager';


/* list all member who did not attend any events */

SELECT M.name
FROM MEMBERS M
LEFT JOIN ATTENDS A ON M.memberID = A.memberID
WHERE A.eventID IS NULL;

/* list workers who have not organized any events */


SELECT W.name
FROM WORKER W
LEFT JOIN ORGANIZES O ON W.workerID = O.workerID
WHERE O.eventID IS NULL;


/* List events that happened after certain dates */

SELECT * FROM EVENTS
WHERE eventDate > '2024-01-01';



/*Find member who paid the most*/

SELECT M.name, SUM(P.amount) AS total_paid
FROM MEMBERS M
JOIN PAYMENTS P ON M.memberID = P.memberID
GROUP BY M.name
ORDER BY total_paid DESC
LIMIT 1;


/* List number of events each worker has organized */
SELECT W.name, COUNT(O.eventID) AS events_organized
FROM WORKER W
JOIN ORGANIZES O ON W.workerID = O.workerID
GROUP BY W.name;


/*totak payments received per month */

SELECT DATE_FORMAT(paymentDate, '%Y-%m') AS month, SUM(amount) AS total_amount
FROM PAYMENTS
GROUP BY month
ORDER BY month DESC;


/* Top 3 most attended events */




SELECT E.eventName, COUNT(A.memberID) AS attendees
FROM EVENTS E
JOIN ATTENDS A ON E.eventID = A.eventID
GROUP BY E.eventName
ORDER BY attendees DESC
LIMIT 3;



/*Average payment amount per membership type*/




SELECT MT.typeName, AVG(P.amount) AS avg_payment
FROM MEMBERSHIP_TYPE MT
JOIN MEMBERS M ON M.typeID = MT.typeID
JOIN PAYMENTS P ON P.memberID = M.memberID
GROUP BY MT.typeName;














