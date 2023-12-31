from flask import Flask, request, render_template, send_file
from filters import apply_blur, apply_contour, apply_edge, apply_greyscale, apply_sharpen, apply_smooth

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'imageUpload' in request.files:
        image = request.files['imageUpload']
        if image.filename != '':
            img = Image.open(image)
            img.save('uploaded_image.jpg')
            
            return render_template('index.html')
    return "No image uploaded."

@app.route('/apply_filter', methods=['POST'])
def apply_filter():
    filter_name = request.form.get('filter_name')
    if filter_name and filter_name in ["blur", "contour", "edge", "greyscale", "sharpen", "smooth"]:
        img = Image.open('uploaded_image.jpg')

        if filter_name == "blur":
            filtered_img = apply_blur(img)
        elif filter_name == "contour":
            filtered_img = apply_contour(img)
        elif filter_name == "edge":
            filtered_img = apply_edge(img)
        elif filter_name == "grayscale":
            filtered_img = apply_greyscale(img)
        elif filter_name == "sharpen":
            filtered_img = apply_sharpen(img)
        elif filter_name == "smooth":
            filtered_img = apply_smooth(img)
        
        output_buffer = io.BytesIO()
        filtered_img.save(output_buffer, format="JPEG")
        output_buffer.seek(0)

        return send_file(output_buffer, mimetype='image/jpeg')

    return "Invalid filter name."
            
if __name__ == '__main__':
    app.run(debug=True)
