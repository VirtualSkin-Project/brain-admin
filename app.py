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
    print("echo -e '{}\n{}' | sudo passwd pi".format(password, password))
    p = subprocess.Popen(['echo -e "{}" | echo -e "{}" | sudo passwd pi'.format(password, password)], shell=True, stdout=subprocess.PIPE)
    comm = p.communicate()
    print(comm)
    result = "password updated successfully" in comm
    return str({"status": result})
