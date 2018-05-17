# Import flask dependencies
from flask import Blueprint, json, abort

# Import module models (i.e. Limb)
from app import app, db, constants as c
from app.limb.model import Limb

# Define the blueprint: 'limb', set its url prefix: app.url/limb
limb = Blueprint('limb', __name__)


@limb.route('/', methods=c.VIEW)
def limbs():
    """
    List limbs
    List limbs connected on Virtual Brain
    ---
    tags:
        - limb
    responses:
        200:
            description: Returns a list of limbs
    """
    q = db.session.query(Limb).all()
    result = [{col: getattr(d, col) for col in Limb.cols} for d in q]
    return app.response_class(response=json.dumps(result), status=c.OK, mimetype=c.JSON)


@limb.route('/<limb_id>', methods=c.DELETE)
def remove(limb_id):
    """
    Remove one of limb
    Route to remove a limb connected on Virtual Brain
    ---
    tags:
        - limb
    responses:
        200:
            description: Return code equals to 0 on success and greater on error
    """
    r_limb = db.session.query(Limb).get(limb_id)
    result = {}
    if r_limb is not None:
        db.session.delete(r_limb)
        if db.session.commit() is None:
            result = {"status": 0}
        else:
            abort(c.CONFLICT)
    else:
        abort(c.CONFLICT)
    return app.response_class(response=json.dumps(result), status=c.OK, mimetype=c.JSON)


@limb.route('/<limb_id>', methods=c.VIEW)
def show_limb(limb_id):
    """
    Show one of limb
    Route to show a limb connected on Virtual Brain
    ---
    tags:
        - limb
    responses:
        200:
            description: Return JSON with limb's data
    """
    r_limb = db.session.query(Limb).get(limb_id)
    result = [{col: getattr(d, col) for col in Limb.cols} for d in r_limb]
    return app.response_class(response=json.dumps(result), status=c.OK, mimetype=c.JSON)


@limb.route('/<name_limb>/password', methods=c.DELETE)
def remove(name_limb):
    """
    Change password of limb by name
    Route to remove a limb connected on Virtual Brain
    ---
    tags:
        - limb
    responses:
        200:
            description: Return code equals to 0 on success and greater on error
    """
    r_limb = db.session.query(Limb).get(name_limb)
    result = {}
    if r_limb is not None:
        db.session.delete(r_limb)
        if db.session.commit() is None:
            result = {"status": 0}
        else:
            abort(c.CONFLICT)
    else:
        abort(c.CONFLICT)
    return app.response_class(response=json.dumps(result), status=c.OK, mimetype=c.JSON)
