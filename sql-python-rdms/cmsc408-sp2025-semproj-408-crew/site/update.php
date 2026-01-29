<?php
// Include database connection
require_once 'db_connection.php';

// Check if form is submitted
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $memberID = $_POST['memberID'];
    $name = $_POST['name'];
    $contactInfo = $_POST['contactInfo'];
    $typeID = $_POST['typeID'];

    // Prepare the SQL statement for updating
    $stmt = $conn->prepare("UPDATE MEMBERS SET name = ?, contactInfo = ?, typeID = ? WHERE memberID = ?");
    $stmt->bind_param("ssii", $name, $contactInfo, $typeID, $memberID);

    // Execute the query
    if ($stmt->execute()) {
        echo "Member updated successfully!";
    } else {
        echo "Error: " . $stmt->error;
    }

    // Close the statement
    $stmt->close();
}

// Fetch the list of members for selection
$result = $conn->query("SELECT * FROM MEMBERS");

// Fetch membership types for the dropdown
$types = $conn->query("SELECT * FROM MEMBERSHIP_TYPE");

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Update Member</title>
</head>
<body>

<h1>Update Member</h1>

<form method="POST" action="update.php">
    <label for="memberID">Select Member:</label>
    <select name="memberID" required>
        <?php
        while ($row = $result->fetch_assoc()) {
            echo "<option value='{$row['memberID']}'>{$row['name']}</option>";
        }
        ?>
    </select><br><br>

    <label for="name">New Name:</label>
    <input type="text" name="name" required><br><br>

    <label for="contactInfo">New Contact Info:</label>
    <input type="text" name="contactInfo" required><br><br>

    <label for="typeID">New Membership Type:</label>
    <select name="typeID" required>
        <?php
        while ($row = $types->fetch_assoc()) {
            echo "<option value='{$row['typeID']}'>{$row['typeName']}</option>";
        }
        ?>
    </select><br><br>

    <button type="submit">Update Member</button>
</form>

</body>
</html>
