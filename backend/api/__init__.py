from os import environ as env

from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_restful import Api, Resource
from sqlalchemy import exc

# from models import setup_db
from database.models import db_drop_and_create_all, setup_db, Drink
from auth.auth import AuthError, requires_auth

# Endpoints:
root = '/'
ping = '/ping'


# Application factory
def create_app(test_config=None):
    app = Flask(__name__)

    # Initializes Cross Origin Resource sharing for the app
    CORS(app)
    # Set Access-Control-Allow
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        return response

    # if not test_config:
    #     setup_db(app, env('DEV_DB_URI'))
    # else:
    #     setup_db(app, env('TEST_DB_URI'))

    api = Api(app)

    # Resources
    class Ping(Resource):
        """ """

        def get(self):
            return {
                "success": True
            }, 200

    # Mapping routes to resources
    api.add_resource(Ping, root, ping)

    # Error handlers for expected errors including 404 and 422.
    @app.errorhandler(400)
    def bad_request(error):
        error_message = 'The server could not understand the request due to invalid syntax.'
        return jsonify({
            'success': False,
            'error': 400,
            'message': error_message
        }), 400

    @app.errorhandler(404)
    def requested_method_not_found(error):
        error_message = 'The server can not find requested resource. ' \
                        'The endpoint may be valid but the resource itself does not exist.'
        return jsonify({
            'success': False,
            'error': 404,
            'message': error_message
        }), 404

    @app.errorhandler(405)
    def method_not_allowed(error):
        error_message = 'The request method is known by the server but has not been allowed and cannot be used.'
        return jsonify({
            'success': False,
            'error': 405,
            'message': error_message
        }), 405

    @app.errorhandler(422)
    def unprocessable_entity(error):
        error_message = 'Server understands the content type of the request entity, and the syntax of the ' \
                        'request entity is correct, but it was unable to process the contained instructions.'
        return jsonify({
            'success': False,
            'error': 422,
            'message': error_message
        }), 422

    return app
