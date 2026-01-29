<?php
// Include database connection
require_once 'db_connection.php';

// Check if form is submitted
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $memberID = $_POST['memberID'];  // Manually entered memberID
    $name = $_POST['name'];
    $contactInfo = $_POST['contactInfo'];
    $typeID = $_POST['typeID']; // This is the membership type

    // Prepare the SQL statement
    $stmt = $conn->prepare("INSERT INTO MEMBERS (memberID, name, contactInfo, typeID) VALUES (?, ?, ?, ?)");
    $stmt->bind_param("issi", $memberID, $name, $contactInfo, $typeID);

    // Execute the query
    if ($stmt->execute()) {
        echo "Member added successfully!";
    } else {
        echo "Error: " . $stmt->error;
    }

    // Close the statement
    $stmt->close();
}

// Fetch membership types for the dropdown
$result = $conn->query("SELECT * FROM MEMBERSHIP_TYPE");
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Add Member</title>
</head>
<body>

<h1>Add Member</h1>

<form method="POST" action="create.php">
    <label for="memberID">Member ID (Manual Entry):</label>
    <input type="number" name="memberID" required><br><br>

    <label for="name">Name:</label>
    <input type="text" name="name" required><br><br>

    <label for="contactInfo">Contact Info:</label>
    <input type="text" name="contactInfo" required><br><br>

    <label for="typeID">Membership Type:</label>
    <select name="typeID" required>
        <?php
        while ($row = $result->fetch_assoc()) {
            echo "<option value='{$row['typeID']}'>{$row['typeName']}</option>";
        }
        ?>
    </select><br><br>

    <button type="submit">Add Member</button>
</form>

</body>
</html>
