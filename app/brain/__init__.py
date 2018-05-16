# Import flask dependencies
import subprocess
from sqlalchemy import sql
from app.limb.model import Limb
from app import app, constants as c, db
from flask import Blueprint, request, json, abort

# Define the blueprint: 'brain', set its url prefix: app.url/brain
brain = Blueprint('brain', __name__)


@brain.route('/', methods=c.ALL)
@brain.route('/brain', methods=c.ALL)
def welcome():
    """
    Welcome on Virtual Brain API
    Route to show a little message for user
    ---
    tags:
        - brain
    responses:
        200:
            description: Return string
    """
    result = {"msg": "Virtual Brain API"}
    return app.response_class(response=json.dumps(result), status=c.OK, mimetype=c.JSON)


@brain.route('/brain/password', methods=c.EDIT)
def change_password():
    """
    Change brain password
    Use this route to change the ssh password on Virtual Brain
    ---
    tags:
        - brain
    responses:
        200:
            description: Return json with new limb
    """
    req = request.get_json(force=True)
    password = req['password'] if type(req['password']) is str else abort(c.CONFLICT, c.TYPE_ERROR.format('password'))
    print('echo -e "{}" | sudo passwd pi'.format(password + "\\n" + password))
    p = subprocess.call('bash change_password.sh "{}"'.format(password + "\\n" + password), shell=True)
    result = {"status": p}
    # result = {"status": 0}
    return app.response_class(response=json.dumps(result), status=c.OK, mimetype=c.JSON)


@brain.route('/subscribe', methods=c.EDIT)
def subscribe():
    """
    Subscribe a limb
    Use this route to subscribe a limb on Virtual Brain API
    ---
    tags:
        - brain
    responses:
        200:
            description: Return json with new limb
    """
    req = request.get_json(force=True)
    name = req['name'] if type(req['name']) is str else abort(c.CONFLICT, c.TYPE_ERROR.format('name'))
    ip = req['ip'] if type(req['ip']) is str else abort(c.CONFLICT, c.TYPE_ERROR.format('ip'))
    area = req['area'] if type(req['area']) is str else abort(c.CONFLICT, c.TYPE_ERROR.format('area'))
    sub_area = req['sub_area'] if 'sub_area' in req else sql.null()
    ssh_key = req['ssh_key'] if type(req['ssh_key']) is str else abort(c.CONFLICT, c.TYPE_ERROR.format('ssh_key'))
    result = {"name": name, "ip": ip, "area": area, "sub_area": str(sub_area), "ssh_key": ssh_key}
    n_limb = Limb(name=name, ip=ip, area=area, sub_area=sub_area, ssh_key=ssh_key)
    db.session.add(n_limb)
    db.session.commit()
    return app.response_class(response=json.dumps(result), status=c.OK, mimetype=c.JSON)
