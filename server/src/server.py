from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit, join_room
from flask_cors import CORS
from loguru import logger
import os

debug_mode = os.getenv("SERVER_DEBUG") == 'true'
port = os.getenv("SERVER_PORT")

server = Flask(__name__)
server.config["DEBUG"] = debug_mode
server.config["WTF_CSRF_ENABLED"] = False
server.config['SECRET_KEY'] = os.getenv("WEB_SOCKETS_SECRET")
socket = SocketIO(server)
CORS(server)

example_data = ['foo', 'bar']


@server.route('/api/v1/test', methods=['GET'])
def test():
    return jsonify(example_data)


@socket.on('/api/v1/book_load')
def book_load(data):
    # test socket
    vid = data.get('book_name')
    logger.debug("book: {0}".format(str(vid)))
    emit('book_load', {'vid': vid}, broadcast=False)


if __name__ == '__main__':
    logger.info("Starting server! Debug: {0}".format(str(debug_mode)))
    server.run(host='0.0.0.0', port=port)
