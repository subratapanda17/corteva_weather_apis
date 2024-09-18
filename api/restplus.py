from flask_restplus import Api
import logging


log = logging.getLogger(__name__)

api  = Api(
    title='API restplus title',
    description="API restplus description",
    doc='/docs'
)

ns_conf = api.namespace(
    "Weather api resources",
    description = "Route for corveta coding challange weather data apis"
)


@api.errorhandler
def default_error_handler(error):
    '''
        Default error handler
    '''
    message = 'Unexpected error occured: {}'.format(error.specific)
    log.error(message)
    return {'message': message}, 500