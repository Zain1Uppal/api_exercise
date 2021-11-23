from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug import exceptions

app = Flask(__name__)
CORS(app)

@app.route('/')
def entry():
    return 'Welcome to this API'


if __name__ == '__main__':
    app.run(debug=True)