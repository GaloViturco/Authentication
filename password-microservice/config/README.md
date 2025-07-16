
# Config Folder 📂

## Overview 🌟

The **config** folder contains configuration files that define global settings for the microservice. Specifically, the **config.js** file defines the port on which the application will run. This file centralizes the configuration of the port, making it easier to modify and configure the application.

### Role of the **config.js** File 📝

- **Port Configuration**: The **config.js** file is used to set the port number for the microservice. It reads the port value from the environment variable `PORT` if available, otherwise defaults to `8002`. This allows for flexibility when deploying the application in different environments.

### Why This Folder Is Important 🔑

- **Centralized Configuration**: Storing all configuration settings in one place helps keep the code clean and organized. It ensures that the microservice will always run on the correct port, regardless of the environment.
- **Scalability**: As the application grows and more settings are needed, this folder can be extended to include additional configuration files for various environments (e.g., development, testing, production).
- **Flexibility**: By using environment variables, the configuration can easily be changed without modifying the code, making it easier to deploy the application across different environments or cloud platforms.

---

### In Summary 📝
The **config** folder serves a crucial role in managing the configuration settings for the application. The **config.js** file specifically manages the port configuration for the microservice, ensuring that the service can be run in different environments without code changes.
