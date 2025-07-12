from captcha.image import ImageCaptcha
import random

class CaptchaGenerator:
    """Genera imágenes de captcha con texto aleatorio."""
    
    @staticmethod
    def generate_captcha():
        """Genera una imagen de captcha y retorna el texto y la imagen."""
        image = ImageCaptcha()

        captcha_text = str(random.randint(1000, 9999))
        
        captcha_image = image.generate(captcha_text)
        
        return captcha_text, captcha_image
