from flask_restx import fields
from flask_restx import Api

api = Api()

get_weather_data_model = api.model('getWeatherData', {
    'station_id': fields.String(required=False, description='Station ID string'),
    'date': fields.Integer(required=False, description='date int [yyyymmdd]')
})
