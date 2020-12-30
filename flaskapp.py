from flask import flask
app = Flask(__name__)

@app.route('/') # 'http://www.google.com'
def home():
    return "Hello, world!"

app.run(port=5000)
