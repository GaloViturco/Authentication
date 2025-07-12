from flask import Flask, send_file, jsonify
from flask_cors import CORS 
from services.captcha_service import CaptchaService
import io

app = Flask(__name__)

CORS(app)

@app.route('/generate-captcha', methods=['GET'])
def generate_captcha():
    """Genera un captcha y lo devuelve como imagen."""
    captcha_text, captcha_image = CaptchaService.generate_captcha()
    
    img_io = io.BytesIO()
    captcha_image.write(captcha_text, img_io)
    img_io.seek(0)
    
    return send_file(img_io, mimetype='image/png', as_attachment=True, download_name='captcha.png')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
