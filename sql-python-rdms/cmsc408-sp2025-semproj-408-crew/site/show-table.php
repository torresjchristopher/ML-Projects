<?php
// Include your connection code here if it's not already included
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

$table = isset($_GET['table']) ? $_GET['table'] : '';

// Validate table name (optional but good practice for security)
$valid_tables = ['ATTENDS', 'EVENTS', 'MEMBERS', 'MEMBERSHIP_TYPE', 'ORGANIZES', 'PAYMENTS', 'WORKER'];
if (!in_array($table, $valid_tables)) {
    die("Invalid table.");
}

// SQL query to select all data from the selected table
$sql = "SELECT * FROM $table";
$result = $conn->query($sql);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Show Table: <?php echo htmlspecialchars($table); ?></title>
    <style>
        table { border-collapse: collapse; width: 100%; margin-top: 20px; }
        th, td { padding: 10px; border: 1px solid #ccc; }
        th { background-color: #f2f2f2; }
    </style>
</head>
<body>

<h1>Data from Table: <?php echo htmlspecialchars($table); ?></h1>

<?php
if ($result && $result->num_rows > 0) {
    echo "<table><tr>";
    // Table headers
    while ($fieldinfo = $result->fetch_field()) {
        echo "<th>" . htmlspecialchars($fieldinfo->name) . "</th>";
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
    echo "<p>No data found for this table.</p>";
}

// Close database connection
$conn->close();
?>

<a href="index.php">← Back to Menu</a>

</body>
</html>
