from flask import Blueprint, jsonify, request
from flask_restx import Resource, Api, fields, Namespace
from api.modules.functions.get_weather_stats import GET_WEATHER_STATS
from api.modules.schemas.get_weather_stats import getWeatherStatsParser
from api.config import settings
from flask import current_app as app

get_weather_stats_ns = Namespace(settings.COMMON_NAMESPACE_NAME, description=settings.COMMON_NAMESPACE_DESCRIPTION)

@get_weather_stats_ns.route('/getWeatherStats/')
class GETWeatherStats(Resource):
    @get_weather_stats_ns.expect(getWeatherStatsParser)
    @get_weather_stats_ns.doc(
        description="Retrieve weather statistics based on parameters",
        responses=settings.doc_responses
    )
    def get(self):
        app.logger.info("Received request for weather stats")
        try:
            req_obj = getWeatherStatsParser.parse_args(strict=True)
            year = req_obj.get('year')
            weather_station_id = req_obj.get('weather_station_id')

            response = GET_WEATHER_STATS(year, weather_station_id).get_stats()
            app.logger.info("Request complete")
            return response, getattr(settings, response.get("status"))
        except Exception as e:
            app.logger.error(f"Error during weather stats fetch: {str(e)}")
            return {"error": str(e)}, e.code
