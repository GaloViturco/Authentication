from utils.captcha_generator import CaptchaGenerator

class CaptchaService:
    """Servicio que maneja la lógica de negocio de generación de captchas."""
    
    @staticmethod
    def generate_captcha():
        """Genera el captcha y devuelve la imagen y el texto."""
        captcha_text, captcha_image = CaptchaGenerator.generate_captcha()
        return captcha_text, captcha_image
