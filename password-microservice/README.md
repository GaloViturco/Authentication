
# Password Microservice 🔑

## Overview 🌟

The **Password Microservice** is a dedicated microservice designed to generate random and secure passwords for users. This service is critical in ensuring that users have strong, unpredictable passwords that adhere to best security practices.

### Purpose 💡

The **Password Microservice** aims to provide an easy-to-use and automated method for generating strong passwords. It ensures that users are provided with passwords that are both complex and unique, making them harder to guess or crack.

## Key Features 🔑

- **Random Password Generation**: The service generates random passwords using a mix of characters, numbers, and symbols to ensure that passwords are strong and secure.
- **Configurable Password Length**: The length of the generated passwords can be customized to meet the specific security requirements of the application.
- **Easy Integration**: The service is built to be easily integrated with any application via simple API calls.
- **Secure Passwords**: Passwords are generated to adhere to modern security standards, including sufficient entropy to prevent common attacks such as brute force or dictionary attacks.

## Programming Language & Technologies ⚙️

- **Programming Language**: The service is built using **JavaScript (Node.js)**, chosen for its non-blocking, event-driven nature that makes it ideal for building fast, scalable microservices.
- **Libraries**: The service uses libraries like **crypto** (for secure random generation) and **express** (for routing HTTP requests) to handle the password generation logic.

## Architecture 🏗️

### Microservice Architecture 🔥

- The **Password Microservice** follows a **microservices architecture**, allowing it to be deployed independently and scale as needed.
- The service is built to handle **RESTful API requests**, making it easy to integrate into any system that needs secure password generation.

### Design Patterns 📝

- **Controller-Service Pattern**: The service follows the **controller-service pattern**. The **PasswordController** handles HTTP requests, while the **PasswordService** encapsulates the logic for generating passwords.
- **Stateless Architecture**: The password service is stateless, meaning it doesn't store any data between requests, making it easily scalable.

### Folder Structure 📁

- **config**: Contains the **`config.js`** file for application configuration such as environment variables or settings.
- **controllers**: Contains the **`passwordController.js`** file that handles the HTTP requests and responds with a randomly generated password.
- **services**: Contains the **`passwordService.js`** file, where the business logic for generating the random passwords is located.
- **utils**: Contains the **`passwordGenerator.js`** file that is responsible for the actual logic behind generating secure passwords.
- **app.js**: The main entry point of the microservice that initializes the express app and connects the controller and services.
- **Dockerfile**: The file that contains the instructions to containerize the application using **Docker**.
- **package.json**: Contains the dependencies and scripts required to run the application.
- **package-lock.json**: Ensures the correct versions of dependencies are installed.

## Deployment 🛠️

### Steps to Deploy:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/GaloViturco/Authentication
    cd Authentication2
    ```

2. **Build the Docker Image**:
    ```bash
    docker build -t galo12/password .
    ```

3. **Run the Docker Container**:
    ```bash
    docker run -d --name password-microservice -p 80:80 --restart unless-stopped galo12/password
    ```

    This will run the microservice on port 80, making it accessible through your host machine.

4. **Access the Service**:
    After running the container, the service will be available at **http://localhost/generate-password** (or your server IP if deployed remotely).

---

## Technologies Used ⚙️

- **JavaScript (Node.js)**: Chosen for its efficiency in handling asynchronous operations and its widespread use in web applications.
- **Express.js**: A minimal and flexible Node.js web application framework used to handle HTTP requests and responses.
- **Docker**: Used for containerization, allowing the microservice to be deployed easily and scaled without dependencies on specific environments.
- **Crypto (Node.js module)**: Used for generating secure, random passwords.

---

### In Summary 📝
The **Password Microservice** is an essential part of securing user accounts by automatically generating strong, random passwords. It is built using **Node.js**, and follows a **microservices architecture**, making it scalable and easy to integrate into any system that requires secure password generation.

---

### Secure Your Users with Strong Passwords! 🔐
Make password management easy and secure with this microservice! 💪
