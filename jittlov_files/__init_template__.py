import os

from flask import Flask, json, request, Response

from flask_apispec.extension import FlaskApiSpec
from flask_apispec import use_kwargs

from flask_restful import Resource, Api, fields, marshal_with

from [apiName].MongoApiConfig import MongoApiConfig
from [apiName].Schema import ModelSchema
from [apiName].MongoApi import MongoApi


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # SWAGGER SETTINGS
    SWAGGER_URL = MongoApiConfig.swagger_url()
    API_URL = MongoApiConfig.api_url()
    # END SWAGGER SETTINGS

    app.config.update(MongoApiConfig.api_spec())

    docs = FlaskApiSpec(app)
    mongo_data_api = MongoApi()

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # READ ----> GET
    @marshal_with(ModelSchema)
    @app.route('/' + MongoApiConfig.api_name(), methods=['GET'], provide_automatic_options=False)
    def mongo_read():
        response = mongo_data_api.read()
        return Response(response=json.dumps(response),
                        status=200,
                        mimetype='application/json')

    # READ ----> GET/ID
    @marshal_with(ModelSchema)
    @app.route('/' + MongoApiConfig.api_name() + '/<object_id>', methods=['GET'], provide_automatic_options=False)
    def mongo_read_by_id(object_id):
        response = mongo_data_api.read_by_id(object_id)
        return Response(response=json.dumps(response),
                        status=200,
                        mimetype='application/json')

    # CREATE ---> POST
    @use_kwargs(ModelSchema, location='json')
    @marshal_with(ModelSchema)
    @app.route('/' + MongoApiConfig.api_name(), methods=['POST'], provide_automatic_options=False)
    def mongo_write():

        data = request.json
        if data is None or data == {}:
            return Response(response=json.dumps({"Error": "Please provide data to post"}),
                            status=400,
                            mimetype='application/json')
        response = mongo_data_api.write(data)
        return Response(response=json.dumps(response),
                        status=200,
                        mimetype='application/json')

    # UPDATE ----> PUT
    @use_kwargs(ModelSchema, location='json')
    @marshal_with(ModelSchema)
    @app.route('/' + MongoApiConfig.api_name() + '/<object_id>', methods=['PUT'], provide_automatic_options=False)
    def mongo_update(object_id):
        data = request.json
        if data is None or data == {}:
            return Response(response=json.dumps({"Error": "Please provide data to put"}),
                            status=400,
                            mimetype='application/json')
        response = mongo_data_api.update(object_id, data)
        return Response(response=json.dumps(response),
                        status=200,
                        mimetype='application/json')

    # DELETE -----> DELETE
    @app.route('/' + MongoApiConfig.api_name() + '/<object_id>', methods=['DELETE'], provide_automatic_options=False)
    def mongo_delete(object_id):
        if id is None or object_id == {}:
            return Response(response=json.dumps({"Error": "Please provide object id"}),
                            status=400,
                            mimetype='application/json')
        response = mongo_data_api.delete(object_id)
        return Response(response=json.dumps(response),
                        status=200,
                        mimetype='application/json')

    docs.register(mongo_read)
    docs.register(mongo_write)
    docs.register(mongo_update)
    docs.register(mongo_delete)
    docs.register(mongo_read_by_id)

    return app
