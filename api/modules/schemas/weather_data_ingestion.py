from flask_restx import fields
from flask_restx import Api

# Initialize the Flask-RESTX API
api = Api()

# Define the request model (schema) for the weather data ingestion endpoint
weather_data_ingestion_model = api.model('WeatherData', {
    'station_id': fields.String(required=True, description='Station ID'),
    'temperature': fields.Float(required=True, description='Temperature'),
    'humidity': fields.Float(required=True, description='Humidity'),
    'wind_speed': fields.Float(required=True, description='Wind Speed')
})
