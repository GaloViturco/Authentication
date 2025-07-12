
# Captcha Microservice 🔒

## Overview 🌟

The **Captcha Microservice** is a small and efficient microservice responsible for generating CAPTCHA challenges. CAPTCHAs are commonly used to verify that a user is human and not a bot, particularly during login or registration processes. This service is designed to generate random and secure CAPTCHA images, providing an additional layer of security to applications and websites.

### Purpose 💡

The **Captcha Microservice** ensures that users interacting with the system are human and not automated bots. This is critical in preventing spam, brute force attacks, and other forms of automated abuse that could compromise the system’s integrity.

## Key Features 🔑

- **Random CAPTCHA Generation**: The service generates random CAPTCHA images with unique, hard-to-guess codes.
- **Image Format**: CAPTCHA images are delivered in PNG format, ensuring high quality and fast loading times.
- **Easy Integration**: The service can be easily integrated into any web application or system by calling a simple API endpoint.
- **Security**: Helps prevent spam and unauthorized login attempts by requiring users to solve a CAPTCHA before proceeding.

## Programming Language & Technologies ⚙️

- **Programming Language**: The service is built using **Python**. Python is used for its simplicity, ease of integration, and efficient handling of image generation tasks.
- **Libraries**: The service uses libraries like **Flask** (a Python web framework) for handling HTTP requests and **captcha.image** for generating CAPTCHA images.

## Architecture 🏗️

### Microservice Architecture 🔥

- The **Captcha Microservice** is built as a **self-contained microservice** that runs independently and communicates with other systems over HTTP APIs.
- The microservice follows the **REST architecture**, allowing external applications to interact with it through simple GET requests.

### Design Patterns 📝

- **Controller-Service Pattern**: The architecture follows the **controller-service pattern**. The **controller** manages the incoming requests and responses, while the **service** contains the business logic for generating and serving CAPTCHA images.
- **Stateless Architecture**: The microservice is stateless, meaning that it does not store any session information between requests, ensuring scalability.

### Folder Structure 📁

- **config**: Contains the **`config.py`** file for storing configuration values used across the application.
- **controllers**: Contains the **`captcha_controller.py`** file, which handles incoming HTTP requests for generating CAPTCHA images and returning them as a response.
- **services**: Contains the **`captcha_service.py`** file, where the business logic for generating CAPTCHA codes is located.
- **utils**: Contains the **`captcha_generator.py`** file, which uses libraries to generate the CAPTCHA images.
- **app.py**: The main entry point of the microservice. It initializes the Flask application and connects the controller and services.
- **Dockerfile**: The file used to containerize the application with **Docker**, allowing for easy deployment and scaling.
- **requirements.txt**: Lists the necessary Python dependencies for the microservice, such as **Flask** and **captcha**.

## Deployment 🛠️

### Steps to Deploy:

1. **Clone the Repository**:
    ```bash
    git clone https://github.dev/Loony213/Authentication2
    cd Authentication2
    ```

2. **Build the Docker Image**:
    ```bash
    docker build -t kamartinez/captcha .
    ```

3. **Run the Docker Container**:
    ```bash
    docker run -d --name captcha-microservice -p 80:80 --restart unless-stopped kamartinez/captcha
    ```

    This will run the microservice on port 80, making it accessible through your host machine.

4. **Access the Service**:
    After running the container, the service will be available at **http://localhost/generate-captcha** (or your server IP if deployed remotely).

---

## Technologies Used ⚙️

- **Python**: Used for developing the microservice due to its ease of use and available libraries for generating CAPTCHA images.
- **Flask**: A lightweight web framework for building APIs and handling HTTP requests.
- **Docker**: Used for containerization, making the microservice easy to deploy and scale.
- **captcha.image**: Python library used to generate the CAPTCHA images.
- **CORS**: For enabling cross-origin requests from other services or frontend applications.

---

### In Summary 📝
The **Captcha Microservice** is a crucial component for securing your application by ensuring that users are human and not bots. It uses a simple yet effective approach to generate CAPTCHA challenges and integrate them into your system with minimal effort.

---

### Let's Keep the Web Secure! 🔒
Keep your application safe with our easy-to-integrate CAPTCHA service. 💪
