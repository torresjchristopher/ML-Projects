<?php
// Database connection details
$servername = "mysql-semproj-container";  // Use MySQL container name or IP
$username = "root";                       // MySQL username
$password = "MyRootPassword44";           // Your MySQL password
$dbname = "membership";                   // The name of your database

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
?>
