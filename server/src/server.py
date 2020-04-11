from flask import Flask, request, jsonify
import os

debug_mode = os.getenv("SERVER_DEBUG") == 'true'
port = os.getenv("SERVER_PORT")

server = Flask(__name__)
server.config["DEBUG"] = debug_mode
server.config["WTF_CSRF_ENABLED"] = False

example_data = ['foo', 'bar']


@server.route('/api/v1/test', methods=['GET'])
def test():
    return jsonify(example_data)


if __name__ == '__main__':
    print("Starting server! Debug: {0}".format(str(debug_mode)))
    server.run(host='0.0.0.0', port=port)
