<h1>hello world!</h1>

<p>Below is a list of tables stored locally.</p>

<?php
// Database connection parameters
$servername = "mysql_db"; // Docker service name for the MySQL container
$username = "root";
$password = "root_password";
$dbname = "my_database";

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
