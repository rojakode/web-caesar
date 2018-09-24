from flask import Flask, render_template, request
from caesar import rotate_string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/", methods=['POST'])
def home():
    rot = int(request.form.get("rot"))
    text = str(request.form.get("text"))

    rotate = rotate_string(text, rot)
    return render_template('index.html', rotated = rotate)

app.run(debug = True)