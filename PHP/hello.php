<?php
// Simple PHP script to demonstrate GET method

// Check if the 'name' parameter exists in the URL
if (isset($_GET['name'])) {
    $name = htmlspecialchars($_GET['name']);
    echo "Hello, $name!";
} else {
    echo "Hello, stranger! Please provide your name using the 'name' parameter in the URL.";
    echo "<br>Example: hello.php?name=John";
}
?>