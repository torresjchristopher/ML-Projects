<?php
// Check if the table name is provided as a query parameter
if (!isset($_GET['table'])) {
    die("No table specified.");
}

$table_name = $_GET['table'];

// Database connection parameters

$servername = getenv('MYSQL_HOST'); // Docker service name for the MySQL container
$username = getenv('MYSQL_USER');
$password = getenv('MYSQL_PASSWORD');
$dbname = getenv('MYSQL_DATABASE');


// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Query to retrieve the contents of the specified table
$sql = "SELECT * FROM `$table_name`";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    echo "<a href='/'>[home]</a><br/>";
    echo "<h1>Contents of table: $table_name</h1>";
    echo "<table border='1'>";
    
    // Output table headers
    $fields = $result->fetch_fields();
    echo "<tr>";
    foreach ($fields as $field) {
        echo "<th>" . htmlspecialchars($field->name ?? '') . "</th>";
    }
    echo "</tr>";

    // Output table rows
    while($row = $result->fetch_assoc()) {
        echo "<tr>";
        foreach ($row as $value) {
            echo "<td>" . htmlspecialchars($value ?? '') . "</td>";
        }
        echo "</tr>";
    }

    echo "</table>";
} else {
    echo "No records found in table: $table_name";
}

$conn->close();
?>
