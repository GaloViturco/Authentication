
# Login Microservice 🔐

## Overview 🌟

The **Login** microservice is responsible for authenticating normal users into the system. It verifies the credentials provided by users and grants them access to the system if they are valid. This service is a core part of the **Authentication Domain** and interacts with the database to store and verify user credentials securely.

### Purpose 💡

The **Login** microservice ensures secure and reliable user login functionality. It checks the credentials of users, allowing them to authenticate and gain access to the system. By using an isolated microservice for login, we achieve modularity and scalability, enabling easy management and future enhancements.

## Key Features 🔑

- **User Authentication**: Validates user credentials (e.g., username and password) against the stored data in the database.
- **Security**: Uses encryption and secure practices for storing and verifying passwords.
- **SQL Server Integration**: The service connects to a SQL Server database to fetch user data and credentials for authentication.
- **Error Handling**: Proper error responses are provided when login fails, ensuring that users are informed if their credentials are incorrect.

## Technology Stack ⚙️

- **Programming Language**: The **Login** microservice is developed using **Python**.
- **Framework**: The service uses **Flask** as the web framework for handling HTTP requests and responses.
- **Database**: User credentials and data are stored securely in a **SQL Server** database.
- **Docker**: The microservice is containerized using Docker for easy deployment and management.
- **Docker Compose**: The service can be easily deployed using **Docker Compose**, allowing it to be run alongside other services in the **Authentication Domain**.

## Folder Structure 📁

### Main Folders and Files:

- **controllers**: Contains the **login_controller.py** file, which handles HTTP requests related to login functionality. It processes incoming login requests, validates the credentials, and returns appropriate responses.
- **models**: Contains the **user_model.py** file, which defines the structure of the user data and interactions with the SQL Server database.
- **routes**: Contains **login_routes.py**, which defines the URL routes for login and authentication functionality.
- **services**: Contains **auth_service.py**, which contains the logic for validating user credentials and authenticating users.
- **utils**: Contains utility functions such as **db.py** (for database connection) and other helper functions used across the microservice.
- **app.py**: The entry point for the **Login** microservice, which initializes the Flask app and configures routes.
- **Dockerfile**: Defines the instructions for building the Docker image for the microservice.
- **requirements.txt**: Lists the Python dependencies needed to run the **Login** microservice.
- **README.md**: This file, which provides an overview of the **Login** microservice and its structure.

---

## How to Deploy 🛠️

### Steps to Deploy:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/GaloViturco/Authentication
    cd Authentication-Domain/Login
    ```

2. **Build and Run with Docker Compose**:
    ```bash
    docker-compose up --build
    ```

    This will build and start the **Login** microservice along with its dependencies.

3. **Access the Service**:
    The **Login** service will be available at the specified port (usually **8002**), which can be defined in the **Dockerfile** or **docker-compose.yml** file.

---

## Technologies Used ⚙️

- **Python**: A high-level programming language used to build the service.
- **Flask**: A lightweight web framework for Python used to handle HTTP requests.
- **SQL Server**: A relational database used for storing user credentials and data.
- **Docker**: A platform for developing and deploying applications inside containers.
- **Docker Compose**: A tool for defining and running multi-container Docker applications.

---

### In Summary 📝

The **Login** microservice is designed to authenticate users into the system. By leveraging **Flask** for handling requests and **SQL Server** for secure data storage, this microservice offers a robust and scalable authentication solution. The use of Docker ensures that the service is easy to deploy and manage in any environment.

---

### Start Securing Your Application Today! 🔐
Allow your users to log in securely with this efficient and scalable **Login** microservice! 💪
