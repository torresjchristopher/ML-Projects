<?php
// Database connection parameters
$servername = getenv('MYSQL_HOST');
$username = getenv('MYSQL_USER');
$password = getenv('MYSQL_PASSWORD');
$dbname = getenv('MYSQL_DATABASE');

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Query to get all tables in the database
$sql = "SHOW TABLES";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    echo "<h1>Tables in the database:</h1>";
    echo "<ul>";
    // Output each table name
    while($row = $result->fetch_array()) {
        $table_name = $row[0];
        echo "<li><a href='show-table.php?table=$table_name'>$table_name</a></li>";
    }
    echo "</ul>";
} else {
    echo "No tables found in the database.";
}

$conn->close();
?>
