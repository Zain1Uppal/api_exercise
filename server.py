from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug import exceptions
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app) 
CORS(app)
Games = [{'id':1,'name':'farcry 6'}, {'id':2,'name': 'COD'}]

@app.route('/')
def entry():
    return 'Welcome to this API'

@app.route('/Games', methods=['GET', 'POST'])
def games_handler():
    if request.method == 'GET':
        return jsonify({'Game': Games}), 200
    elif request.method == 'POST':
        data = request.get_json()
        for game in Games:
            print(game['name'])
            if(game['name'] == data['name']):
                return jsonify('Game already exists'), 403
        Games.append(data)
        data['id'] = len(Games)
        resp = {'Game': Games}
        # msg = Message(f"Game {data['name']} has been added",
        #                 sender="zainuppal2@gmail.com",
        #                 recipients=["zainuppal1@gmail.com"])
        # mail.send(msg)
        return jsonify(resp), 201

@app.route('/Games/<int:game_id>')
def game_handler(game_id):
    game = next(game for game in Games if game['id'] == game_id)
    return jsonify({'Game':game}), 200


@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return jsonify({"message": f"Error {err}"}), 404

@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return jsonify({"message": f"{err}"}), 500



if __name__ == '__main__':
    app.run(debug=True)