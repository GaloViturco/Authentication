const express = require('express');
const PasswordController = require('./controllers/passwordController');
const config = require('./config/config');

const app = express();

// Ruta para la generación de contraseñas
app.get('/generate-password', PasswordController.generatePassword);

// Iniciamos el servidor
app.listen(config.port, () => {
  console.log(`Server running on port ${config.port}`);
});
