from flask import Blueprint, jsonify
from flask_restx import Resource, Api, fields
from api.modules.schemas.get_weather_stats import get_weather_stats_model
from api.modules.functions.get_weather_stats import GET_WEATHER_STATS

# Create a blueprint for the weather data ingestion endpoint
weather_get_bp = Blueprint('get_weather_data', __name__)
api = Api(weather_get_bp)

@api.route('/getWeatherStats/')
class GETWeatherStats(Resource):
    @api.expect(get_weather_stats_model)
    def get(self):
        
        return jsonify("getweatherStats NONE")
