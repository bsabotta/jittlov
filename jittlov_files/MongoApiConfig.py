from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin


class MongoApiConfig:

    @staticmethod
    def mongo_url():
        return "[databaseUrl]"

    @staticmethod
    def mongo_database():
        return "[databaseName]"

    @staticmethod
    def mongo_collection():
        return "[databaseTable]"

    @staticmethod
    def swagger_url():
        return "/api/docs"

    @staticmethod
    def api_url():
        return "[apiBroadcastHttp][apiBroadcastIp]:[apiBroadcastPort]"

    @staticmethod
    def api_spec():
        return_value = {
            'APISPEC_SPEC': APISpec(
                title='[apiName] API',
                version='v1',
                plugins=[MarshmallowPlugin()],
                openapi_version='2.0.0'
            ),
            'APISPEC_SWAGGER_URL': '/swagger/',  # URI to access API Doc JSON
            'APISPEC_SWAGGER_UI_URL': '/swagger-ui/'  # URI to access UI of API Doc
        }
        return return_value

    @staticmethod
    def api_name():
        return "[apiName]"
