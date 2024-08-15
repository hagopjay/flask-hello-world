from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello there World!'

@app.route('/about')
def about():
    return 'AboutZ'
