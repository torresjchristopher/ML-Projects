<?php
// Include database connection
require_once 'db_connection.php';

// Check if form is submitted
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $memberID = $_POST['memberID'];

    // Prepare the SQL statement to delete the member
    $stmt = $conn->prepare("DELETE FROM MEMBERS WHERE memberID = ?");
    $stmt->bind_param("i", $memberID);

    // Execute the query
    if ($stmt->execute()) {
        echo "Member deleted successfully!";
    } else {
        echo "Error: " . $stmt->error;
    }

    // Close the statement
    $stmt->close();
}

// Fetch the list of members for selection (display their name)
$result = $conn->query("SELECT * FROM MEMBERS");

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Delete Member</title>
</head>
<body>

<h1>Delete Member</h1>

<form method="POST" action="delete.php">
    <label for="memberID">Select Member to Delete:</label>
    <select name="memberID" required>
        <?php
        while ($row = $result->fetch_assoc()) {
            echo "<option value='{$row['memberID']}'>{$row['name']}</option>";
        }
        ?>
    </select><br><br>

    <button type="submit">Delete Member</button>
</form>

</body>
</html>
