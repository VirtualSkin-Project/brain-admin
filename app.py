import subprocess
from flask import Flask
from flask import request


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/rpi/password', methods=['PUT'])
def change_password():
    req_data = request.get_json(force=True)
    password = req_data['password']
    print("echo -e '{}' | sudo passwd pi".format(password + '\\n' + password))
    p = subprocess.Popen(['echo', '-e', '"{}"', '|', 'sudo passwd pi'.format(password + "\\n" + password)], shell=True)
    comm = p.communicate()
    print(comm)
    return str({"status": True})
