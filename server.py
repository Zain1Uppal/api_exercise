from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug import exceptions

app = Flask(__name__)
CORS(app)
Games = ['farcry 6', 'COD']

@app.route('/')
def entry():
    return 'Welcome to this API'

@app.route('/Games', methods=['GET', 'POST'])
def pokemon_handler():
    if request.method == 'GET':
        return jsonify({'Game': Games}), 200s
    elif request.method == 'POST':
        data = request.json
        return f"{data['name']} played {data['Game']}"


@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return jsonify({"message": f"Error {err}"}), 404

@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return jsonify({"message": f"{err}"}), 500



if __name__ == '__main__':
    app.run(debug=True)