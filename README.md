# Library Management System

## Overview

The **Library Management System** is a web-based application designed to help libraries manage books, members, and borrowing activities. With an intuitive interface and comprehensive functionality, this application streamlines library operations and enhances user experience.

## Features

- 📚 **Book Management**: Add, edit, delete, and view books with details like title, author, genre, and availability.
- 👤 **Member Management**: Easily add, view, and manage library members.
- 📖 **Borrowing & Return System**: Track book loans and returns, making it easy to manage borrowing records.
- 🔒 **User Authentication**: Secure login/logout functionality for both admins and members.
- 🌐 **Responsive Design**: Built with a responsive layout, accessible from both desktops and mobile devices.

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Backend**: Flask(a lightweight Python web framework) 
- **Database**: MongoDB

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/library-management-system.git
Navigate to the project directory:

cd library-management-system
Import the database:

Open your MySQL database tool (e.g., phpMyAdmin).
Create a new database named library_management.
Import the library_management.sql file located in the project directory.
Configure the database connection:

Open the config.php file in the project directory.
Update the database credentials as needed:

$servername = "localhost";
$username = "your_username";
$password = "your_password";
$dbname = "library_management";
Start your local server and navigate to the project in your browser:

http://localhost/library-management-system

Usage
Login: Access the system with user credentials.
Book Management: Navigate to "Add Book" or "Book List" to manage the book inventory.
Member Management: Use "Add Member" or "Member List" for member operations.
Borrowing System: Borrow and return books in the "Borrow Book" section.


Future Scope
📱 Mobile App Development: Expand functionality for mobile platforms.
🌍 Multi-Language Support: Make the system accessible in multiple languages.
🔍 Advanced Search Options: Enable filtering and searching for books and members with more criteria.
