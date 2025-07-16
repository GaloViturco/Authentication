
# Utils Folder 📂

## Overview 🌟

The **utils** folder contains helper functions and utilities used throughout the application. Specifically, the **db.py** file is responsible for establishing a connection with the SQL Server database. This connection is used across the application to interact with the user data stored in the database, including fetching and storing user information.

### Role of the **db.py** File 📝

The **db.py** file contains a single function, **get_connection()**, which establishes a connection to a remote SQL Server database using **pyodbc**. This connection is essential for performing CRUD operations on the database (such as user authentication, storing user credentials, etc.).

- **Database Connection**: The primary responsibility of **get_connection()** is to provide a connection to the **auth_db** SQL Server database, allowing the application to interact with user data securely.
- **pyodbc**: The file uses **pyodbc**, a Python module that allows Python programs to interact with databases via ODBC (Open Database Connectivity). It provides a reliable connection mechanism to SQL Server for the application.
- **Reusability**: This utility function can be reused throughout the application, ensuring that any part of the code that needs access to the database can do so in a consistent and secure way.

### Importance of the DB Utility 🔑

- **Centralized Database Access**: By centralizing the database connection logic in this utility, the application is able to keep database interactions modular and easy to maintain. This reduces the need to repeatedly configure connections in different parts of the application.
- **Security**: The connection string used in the function contains sensitive information, such as database credentials. This approach ensures that the connection is made securely, and the database access credentials are kept in one place for easy management.
- **Efficiency**: The utility streamlines the process of connecting to the database, ensuring that database interactions are handled efficiently and consistently throughout the codebase.

---

### In Summary 📝
The **utils** folder contains essential helper functions. The **db.py** file handles the database connection logic, allowing the application to securely interact with the SQL Server database. This utility ensures modularity, security, and efficiency in handling database operations.
