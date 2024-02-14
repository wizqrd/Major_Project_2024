<h1>Update logs</h1>
<h2>Login System</h2>
I made a script that will store user data in a csv file to keep track of logins and signup. Tried to make it efficient and readable by removing an else block.
<h2>Login System</h2>
Functionality:

- Sign-up: Allows users to create new accounts with usernames and passwords, storing them securely in the "user_data.csv" file using bcrypt for password hashing.

- Login: Enables users to enter their existing usernames and passwords, validating them against the stored data and granting access on successful login.

- Error Handling: Incorporates exception handling to gracefully address issues like invalid inputs, file access errors, and unexpected exceptions.

- Readability: Enhances code clarity with clear variable names, comments, and well-defined functions.

- Efficiency: Streamlines the code, removing redundancies and optimizing logic for better performance.
Improvements:

- Security: Implements secure password hashing with bcrypt, significantly improving password protection.

- Structure: Organizes the code into modular functions for maintainability and clarity.
<h4>To Do:</h4>
<h3>Creating a login system using a. cbf file to store data