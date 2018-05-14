from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/rpi/password', methods=['PUT'])
def change_password():
    req_data = request.get_json(force=True)  # force=True will make sure this works even if a client does not specify application/json
    password = req_data['password']  # or whatever key you have in your json
    return 'echo -e "{}\n{}" | sudo passwd pi'.format(password, password)
