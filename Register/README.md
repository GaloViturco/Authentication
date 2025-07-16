
# Register-Service Microservice 🚀

This microservice is part of the **Authentication-Domain** repository and is responsible for user registration. It allows new users to register by providing their details, ensuring secure and valid user data entry. This service is built using Python and follows a microservices architecture to ensure scalability and modularity.

## Repository Link 📁
- [GitHub Repository](https://github.com/GaloViturco/Authentication)

## Docker Image 🐳
- **Docker Image:** `galo12/register-service`

## Purpose 🎯
The **Register-Service** microservice allows new users to register into the system by securely storing their credentials and personal information. This service ensures that the registration process is handled with security, validation, and proper handling of user data.

## Architecture Style 🏗️
- **Microservice Architecture:** This service is designed to be a standalone component that communicates with other services via defined APIs, making it independently deployable.
- **Design Pattern:** The service follows the **MVC (Model-View-Controller)** pattern, separating the concerns of data management, business logic, and routing.

## Technologies 💻
- **Programming Language:** Python 3.x
- **Framework:** Flask (for API routing and management)
- **Database:** SQL (integration via `db.py`)
- **Containerization:** Docker

## Project Structure 🧑‍💻
The repository is structured as follows:

```
Register/
├── controllers/              # Contains logic for handling user requests.
│   └── register_controller.py # Controller to manage the registration process.
│
├── models/                   # Contains database models.
│   └── user_model.py         # Defines the user model, including registration details.
│
├── routes/                   # API routes for registration.
│   └── register_routes.py     # Routes to handle registration-related API calls.
│
├── services/                 # Contains business logic services.
│   └── auth_service.py       # Service for processing user registration requests.
│
├── utils/                    # Utility functions and helper methods.
│   └── db.py                 # Database connection and management.
│
├── app.py                    # Main application entry point.
├── Dockerfile                # Docker configuration for containerization.
├── README.md                 # This file.
└── requirements.txt          # Python dependencies for the project.
```

### Folder Descriptions 📂
- **controllers/**: Manages incoming requests and sends responses, following the MVC structure.
- **models/**: Contains the data models, primarily used to interact with the database.
- **routes/**: Handles the routes or endpoints that the microservice exposes.
- **services/**: Encapsulates the core business logic, like registration.
- **utils/**: Houses utility functions like database connection handling (`db.py`).

## How to Deploy ⚙️
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/GaloViturco/Authentication
   ```

2. **Install Dependencies:**
   Navigate to the project directory and install the necessary Python packages.
   ```bash
   pip install -r requirements.txt
   ```

3. **Docker Deployment:**
   - Build the Docker image:
     ```bash
     docker build -t galo12/register-service .
     ```
   - Run the container:
     ```bash
     docker run -p 5000:5000 galo12/register-service
     ```

4. **Access the Service:**
   - The service will be accessible on `http://localhost:5000` once the container is running.

## Features ✨
- **User Registration:** Facilitates the secure registration of new users.
- **Data Validation:** Ensures that the provided user data is valid before storing it in the database.
- **Modular and Scalable:** Designed to scale and integrate with other microservices.
- **Secure User Data Handling:** Follows security best practices for storing user credentials.

## Usage 📝
After deploying the microservice, make POST requests to `/register` with the new user's details to register them.

### Example POST Request:
```json
{
    "username": "newuser",
    "password": "newpassword",
    "email": "user@example.com",
    "full_name": "New User"
}
```

## License 📜
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
