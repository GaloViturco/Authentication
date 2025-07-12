
# Utils Folder 📂

## Overview 🌟

The **utils** folder contains utility classes that provide supporting functionality for the main business logic of the application. In this folder, the **captcha_generator.py** file contains the logic for generating CAPTCHA images. This class is essential for creating the CAPTCHA content used by the **CaptchaService**.

### Role of the **captcha_generator.py** File 📝

- **CAPTCHA Generation**: The **CaptchaGenerator** class is responsible for generating random CAPTCHA images. It leverages the **ImageCaptcha** class from the **captcha** library to create the images and randomly generates numeric text for each CAPTCHA.
- **Random Number Generation**: The CAPTCHA text is generated as a random 4-digit number, ensuring that each generated CAPTCHA is unique.
- **Integration with the Service Layer**: The **CaptchaGenerator** is used by the **CaptchaService** to provide the image and text required for CAPTCHA validation and user interaction.

### Why This Folder Is Important 🔑

- **Supporting Functionality**: The **utils** folder contains utility classes that support the core functionality of the microservice. By separating the CAPTCHA generation logic into its own class, the code remains modular and clean.
- **Decoupling Business Logic**: The **captcha_generator.py** class focuses solely on generating the CAPTCHA images, while the **CaptchaService** handles the business logic. This separation of concerns ensures that each part of the application has a single responsibility.
- **Extensibility**: The utility class can be easily extended to support different types of CAPTCHAs or incorporate more complex algorithms for image generation.

---

### In Summary 📝
The **utils** folder is key to maintaining a clean architecture. The **captcha_generator.py** file encapsulates the logic for generating CAPTCHA images, which is used by the service layer to provide dynamic CAPTCHA challenges. This modularity makes the system easier to maintain and scale as needed.
