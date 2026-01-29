<?php
// Connect to MySQL using Docker environment variables
$host = getenv('DOCKER_DB_HOST') ?: 'db';
$username = getenv('DOCKER_DB_USER') ?: 'root';
$password = getenv('DOCKER_DB_PASS') ?: 'MyRootPassword44';
$database = getenv('DOCKER_DB_DBNAME') ?: 'membership';

// Create connection
$conn = new mysqli($host, $username, $password, $database);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Map of query ID to actual SQL queries
$queries = [
    1 => "SELECT * FROM MEMBERS;",
    2 => "SELECT * FROM EVENTS;",
    3 => "SELECT * FROM WORKER;",
    4 => "SELECT * FROM MEMBERSHIP_TYPE;",
    5 => "SELECT memberID, amount, paymentDate FROM PAYMENTS ORDER BY paymentDate DESC;",
    6 => "SELECT M.name, MT.typeName FROM MEMBERS M JOIN MEMBERSHIP_TYPE MT ON M.typeID = MT.typeID;",
    7 => "SELECT MEM.name AS member_name, E.eventName, E.eventDate FROM ATTENDS A JOIN MEMBERS MEM ON A.memberID = MEM.memberID JOIN EVENTS E ON A.eventID = E.eventID;",
    8 => "SELECT W.name AS worker_name, E.eventName, E.eventDate FROM ORGANIZES O JOIN WORKER W ON O.workerID = W.workerID JOIN EVENTS E ON O.eventID = E.eventID;",
    9 => "SELECT M.name, SUM(P.amount) AS total_paid FROM MEMBERS M JOIN PAYMENTS P ON M.memberID = P.memberID GROUP BY M.name;",
    10 => "SELECT E.eventName, COUNT(A.memberID) AS num_attendees FROM EVENTS E JOIN ATTENDS A ON E.eventID = A.eventID GROUP BY E.eventName HAVING COUNT(A.memberID) > 5;",
    11 => "SELECT E.eventName, COUNT(A.memberID) AS num_attendees FROM EVENTS E LEFT JOIN ATTENDS A ON E.eventID = A.eventID GROUP BY E.eventName;",
    12 => "SELECT W.name, E.eventName FROM WORKER W JOIN ORGANIZES O ON W.workerID = O.workerID JOIN EVENTS E ON O.eventID = E.eventID WHERE W.role = 'Manager';",
    13 => "SELECT M.name FROM MEMBERS M LEFT JOIN ATTENDS A ON M.memberID = A.memberID WHERE A.eventID IS NULL;",
    14 => "SELECT W.name FROM WORKER W LEFT JOIN ORGANIZES O ON W.workerID = O.workerID WHERE O.eventID IS NULL;",
    15 => "SELECT * FROM EVENTS WHERE eventDate > '2024-01-01';",
    16 => "SELECT M.name, SUM(P.amount) AS total_paid FROM MEMBERS M JOIN PAYMENTS P ON M.memberID = P.memberID GROUP BY M.name ORDER BY total_paid DESC LIMIT 1;",
    17 => "SELECT W.name, COUNT(O.eventID) AS events_organized FROM WORKER W JOIN ORGANIZES O ON W.workerID = O.workerID GROUP BY W.name;",
    18 => "SELECT DATE_FORMAT(paymentDate, '%Y-%m') AS month, SUM(amount) AS total_amount FROM PAYMENTS GROUP BY month ORDER BY month DESC;",
    19 => "SELECT E.eventName, COUNT(A.memberID) AS attendees FROM EVENTS E JOIN ATTENDS A ON E.eventID = A.eventID GROUP BY E.eventName ORDER BY attendees DESC LIMIT 3;",
    20 => "SELECT MT.typeName, AVG(P.amount) AS avg_payment FROM MEMBERSHIP_TYPE MT JOIN MEMBERS M ON M.typeID = MT.typeID JOIN PAYMENTS P ON P.memberID = M.memberID GROUP BY MT.typeName;"
];

// Get which query ID the user selected
$query_id = isset($_POST['query_id']) ? intval($_POST['query_id']) : 0;

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Query Results</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        table { border-collapse: collapse; margin-top: 20px; width: 100%; }
        th, td { padding: 10px; border: 1px solid #ccc; }
        th { background-color: #f2f2f2; }
        a { display: inline-block; margin-top: 20px; }
    </style>
</head>
<body>

<h1>Query Results</h1>

<?php
if ($query_id > 0 && isset($queries[$query_id])) {
    $sql = $queries[$query_id];
    $result = $conn->query($sql);

    if ($result && $result->num_rows > 0) {
        echo "<table><tr>";
        // Table headers
        while ($fieldinfo = $result->fetch_field()) {
            echo "<th>{$fieldinfo->name}</th>";
        }
        echo "</tr>";

        // Table rows
        while ($row = $result->fetch_assoc()) {
            echo "<tr>";
            foreach ($row as $col) {
                echo "<td>" . htmlspecialchars($col) . "</td>";
            }
            echo "</tr>";
        }
        echo "</table>";
    } else {
        echo "<p>No results found.</p>";
    }
} else {
    echo "<p>Invalid query selection.</p>";
}

// Close database connection
$conn->close();
?>

<a href="index.php">← Back to Menu</a>

</body>
</html>
