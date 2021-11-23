from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug import exceptions

app = Flask(__name__)
CORS(app)
Games = [{'name':'farcry 6'}, {'name': 'COD'}]

@app.route('/')
def entry():
    return 'Welcome to this API'

@app.route('/Games', methods=['GET', 'POST'])
def game_handler():
    if request.method == 'GET':
        return jsonify({'Game': Games}), 200
    elif request.method == 'POST':
        data = request.get_json()
        Games.append(data)
        resp = {'Game': Games}
        return jsonify(resp), 201


@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return jsonify({"message": f"Error {err}"}), 404

@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return jsonify({"message": f"{err}"}), 500



if __name__ == '__main__':
    app.run(debug=True)