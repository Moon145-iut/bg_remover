from flask import Flask, request, render_template, send_file
from rembg import remove
from PIL import Image
import io
import os

def create_app():
    app = Flask(__name__)
    UPLOAD_FOLDER = 'static/uploads'
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    def remove_background(image):
        """Remove background from an image"""
        try:
            # Remove background
            output_image = remove(image)
            # Convert to bytes
            img_byte_arr = io.BytesIO()
            output_image.save(img_byte_arr, format='PNG')
            img_byte_arr.seek(0)
            return img_byte_arr
        except Exception as e:
            print(f"Error processing image: {str(e)}")
            return None

    @app.route('/', methods=['GET', 'POST'])
    def upload_file():
        if request.method == 'POST':
            if 'file' not in request.files:
                return 'No file uploaded', 400
            file = request.files['file']
            if file.filename == '':
                return 'No file selected', 400
            
            # Process the image
            input_image = Image.open(file)
            result = remove_background(input_image)
            
            if result:
                return send_file(
                    result,
                    mimetype='image/png',
                    as_attachment=True,
                    download_name='output.png'
                )
        return render_template('upload.html')

    return app

app = create_app()
