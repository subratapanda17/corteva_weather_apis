from flask_restx import fields
from flask_restx import Api

api = Api()

weather_data_ingestion_model = api.model('WeatherDataIngestion', {
    'station_id': fields.String(required=True, description='Station ID')
})
