from flask import Flask, json, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_swagger import swagger
from app import constants as c

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


@app.errorhandler(c.NOT_FOUND)
def not_found(error):
    result = {'error': str(error)}
    response = app.response_class(
        response=json.dumps(result),
        status=c.NOT_FOUND,
        mimetype=c.JSON
    )
    return response


@app.errorhandler(c.CONFLICT)
def not_found(error):
    result = {'error': str(error)}
    response = app.response_class(
        response=json.dumps(result),
        status=c.NOT_FOUND,
        mimetype=c.JSON
    )
    return response


from app.brain import brain
from app.limb import limb

app.register_blueprint(brain)
app.register_blueprint(limb, url_prefix='/limb')


@app.route('/teapot', methods=c.ALL)
def teapot():
    result = {'msg': 'I\'m a teapot'}
    response = app.response_class(
        response=json.dumps(result),
        status=c.I_M_A_TEAPOT,
        mimetype=c.JSON
    )
    return response


@app.route("/spec")
def spec():
    swag = swagger(app)
    swag['info']['version'] = "0.1"
    swag['info']['title'] = "Virtual Brain Api"
    swag['info']['desciption'] = "The API to manage Virtual Brain and Virtual Limb"
    swag['info']['author'] = "Jonathan LOQUET (loquet_j) <loquet_j@etna-alternance.net>"
    swag['info']['group'] = "VirtualSkin"
    swag['info']['members'] = [
        "Antoine MARTIN (martin_a) <martin_a@etna-alternance.net>",
        "Raphaël DEBRAY(debray_r) <debray_r@etna-alternance.net>",
        "Florian BERENICE (bereni_f) <bereni_f@etna-alternance.net>",
        "Jonathan LOQUET (loquet_j) <loquet_j@etna-alternance.net>"
    ]
    swag['info']['school'] = "ETNA"
    return jsonify(swag)
