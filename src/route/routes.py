"""
Defines the blueprint for the routes
"""

from flask import Blueprint, jsonify, current_app
from flask.ext.restful import Api

ROUTES_BLUEPRINT = Blueprint('routes', __name__)
ROUTES_BLUEPRINT_API = Api(ROUTES_BLUEPRINT)


@ROUTES_BLUEPRINT.route('/routes')
def list_routes():
    output = []
    for rule in current_app.url_map.iter_rules():
        methods = ','.join(rule.methods)
        line = "{:50s} {:20s}".format(str(rule), methods)
        output.append(line)
    return jsonify(routes=output)
