# namspace details
COMMON_NAMESPACE_NAME = 'weather data apis'
COMMON_NAMESPACE_DESCRIPTION = 'multiple perations of corteva weather data'

# database details
DB_TYPE = 'LOCAL'
SQL_TABLE_NAME = 'corteva_weather_record'

# response codes
OK = 200
SUCCESS = 200
BAD_REQUEST = 400
NOT_FOUND = 404
CONFLICT = 409
INTERNAL_SERVER_ERROR = 500


# documented responses
doc_responses = {
            200: 'Success',
            400: 'Bad Request',
            404: 'Not Found',
            500: 'Internal Server Error'
}

class TestingConfig:
   TESTING = True
   DEBUG = True
   SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'