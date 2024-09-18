from flask_restx import fields
from flask_restx import Api

api = Api()

get_weather_stats_model = api.model('getWeatherStats', {
    'station_id': fields.String(required=False, description='Station ID string'),
    'date': fields.Integer(required=False, description='date int [yyyymmdd]')
})
