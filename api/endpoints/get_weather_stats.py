from flask import Blueprint, jsonify, request
from flask_restx import Resource, Api, fields, Namespace
from api.modules.functions.get_weather_stats import GET_WEATHER_STATS
from api.modules.schemas.get_weather_stats import getWeatherStatsParser

get_weather_stats_ns = Namespace('get_weather_stas', description='Weather data stats')

@get_weather_stats_ns.route('/getWeatherStats/')
class GETWeatherData(Resource):
    @get_weather_stats_ns.expect(getWeatherStatsParser)
    def get(self):
        req_obj = getWeatherStatsParser.parse_args(strict=True)
        year = req_obj.get('year')
        weather_station_id = req_obj.get('weather_station_id')

        response = GET_WEATHER_STATS(year, weather_station_id).get_stats()
        return response
