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
    p = subprocess.Popen(["echo -e '{}\n{}' | sudo passwd pi".format(password, password)], shell=True, stdout=subprocess.PIPE)
    result = "password updated successfully" in p.communicate()
    return {"status": result}
