<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Query Selection</title>
  <style>
    body {
      margin: 0;
      font-family: Arial, sans-serif;
      background-color: #f4f4f4;
      color: #333;
    }

    header {
      background-color: DarkSeaGreen;
      padding: 30px 0;
      text-align: center;
    }

    header h1 {
      font-family: Verdana, sans-serif;
      font-size: 28px;
      color: white;
      margin: 0;
    }

    .container {
      max-width: 600px;
      margin: 50px auto;
      background: white;
      padding: 30px;
      box-shadow: 0 0 10px rgba(0,0,0,0.1);
      border-radius: 8px;
    }

    .container p {
      font-size: 18px;
      font-weight: bold;
    }

    label, select {
      display: block;
      margin-bottom: 15px;
      font-size: 16px;
    }

    select {
      width: 100%;
      padding: 10px;
      border-radius: 4px;
      border: 1px solid #ccc;
      font-size: 16px;
    }

    button {
      background-color: DarkSeaGreen;
      color: white;
      padding: 10px 20px;
      font-size: 16px;
      border: none;
      border-radius: 5px;
      cursor: pointer;
      transition: background-color 0.3s ease;
    }

    button:hover {
      background-color: seagreen;
    }
  </style>
</head>
<body>

  <header>
    <h1>Welcome to 408 Crew's Country Club Database</h1>
  </header>

  <div class="container">
    <p>Select a Query to Run</p>
    <form action="queries.php" method="POST">
      <label for="query_id">Choose a query:</label>
      <select name="query_id" id="query_id" required>
        <option value="" disabled selected>Select a query</option>
        <option value="1">1. Show all members</option>
        <option value="2">2. Show all events</option>
        <option value="3">3. Show all workers</option>
        <option value="4">4. Show all membership types</option>
        <option value="5">5. List all payments (most recent first)</option>
        <option value="6">6. Members with their membership type</option>
        <option value="7">7. Members attending events</option>
        <option value="8">8. Workers organizing events</option>
        <option value="9">9. Total paid per member</option>
        <option value="10">10. Events with more than 5 attendees</option>
        <option value="11">11. Members who paid more than $100</option>
        <option value="12">12. Events organized by managers</option>
        <option value="13">13. Members who have not attended any event</option>
        <option value="14">14. Workers who haven't organized any events</option>
        <option value="15">15. Events happening after 2024</option>
        <option value="16">16. Top paying member</option>
        <option value="17">17. Workers and number of events they organized</option>
        <option value="18">18. Monthly payment totals</option>
        <option value="19">19. Top 3 events by attendees</option>
        <option value="20">20. Average payment by membership type</option>
      </select>

      <button type="submit">Run Query</button>
    </form>
<<<<<<< HEAD

    <p>Or choose an action:</p>
    <ul>
    <li><a href="create.php"> Add Member</a></li>
    <li><a href="update.php"> Update Member</a></li>
    <li><a href="delete.php"> Delete Member</a></li>
    </ul>
=======
>>>>>>> ff12dfdca1acc7cb7874843d2bfc7cfcea92f623
  </div>

</body>
</html>


<?php
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

// Query to get all tables in the database
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
