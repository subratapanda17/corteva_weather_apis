from flask import Blueprint, jsonify
from flask_restx import Resource, Api, fields
from api.modules.functions.weather_data_ingestion import InsertWeatherData
from api.modules.schemas.weather_data_ingestion import weather_data_ingestion_model

# Create a blueprint for the weather data ingestion endpoint
weather_bp = Blueprint('weather_data_ingestion', __name__)
api = Api(weather_bp)

@api.route('/weather/ingest')
class WeatherDataIngest(Resource):
    @api.expect(weather_data_ingestion_model)
    def get(self):
        
        result = InsertWeatherData().insert_weather_data()
        
        return jsonify(result)
