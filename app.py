from flask import Flask, render_template, request, send_from_directory, jsonify
from werkzeug.utils import secure_filename
import socket, os

HOSTNAME = socket.gethostname()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'ico', 'svg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save('files/' + filename)
        success_message = f'File "{filename}" uploaded successfully!'
        alert_class = 'alert-success'
    else:
        allowed_extensions = ', '.join(ALLOWED_EXTENSIONS)
        success_message = f'Invalid image type. Only the following types are allowed: {allowed_extensions}'
        alert_class = 'alert-danger'
    return render_template('index.html', success=success_message, alert_class=alert_class)

@app.route('/images/<filename>')
def serve_image(filename):
    return send_from_directory('files', filename)

@app.route('/images')
def images():
    filenames = os.listdir('files')
    return render_template('images.html', filenames=filenames)

@app.route('/static/<filename>')
def serve_static_image(filename):
    return send_from_directory('static', filename)

@app.route('/static')
def static_images():
    filenames = os.listdir('static')
    return render_template('static.html', filenames=filenames)

@app.route('/status', methods=['GET'])
def status():
    return jsonify(
        Healthy = True,
        Host = HOSTNAME,
        StatusCode = 200
        ), 200, {'ContentType':'application/json'}

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8889)