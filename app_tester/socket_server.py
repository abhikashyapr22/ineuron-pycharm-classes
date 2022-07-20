from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("Start.html")

socketio = SocketIO(app)

pin = True
@socketio.on('change_gpio')
def handle_my_custom_event(json):
    pin = json['status']
    print('pin = ' , pin)

@socketio.on('connect', namespace='/')
def test_connect():
    print('Connected')


if __name__ == '__main__':
    socketio.run(app)