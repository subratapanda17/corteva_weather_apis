from flask import Blueprint, jsonify, request
from flask_restx import Resource, Api, fields, Namespace
from api.modules.functions.get_weather_data import GET_WEATHER_DATA
from api.modules.schemas.get_weather_data import getWeatherDataParser
from api.config import settings
from flask import current_app as app

get_weather_data_ns = Namespace(settings.COMMON_NAMESPACE_NAME, description=settings.COMMON_NAMESPACE_DESCRIPTION)
@get_weather_data_ns.route('/getWeatherData/')
class GETWeatherData(Resource):
    @get_weather_data_ns.expect(getWeatherDataParser)
    @get_weather_data_ns.doc(
        description="Retrieve weather data based on provided parameters",
        responses=settings.doc_responses
    )
    def get(self):
        app.logger.info("Received request for fething weather data")
        try:
            req_obj = getWeatherDataParser.parse_args(strict=True)
            date = req_obj.get('date')
            weather_station_id = req_obj.get('weather_station_id')
            page_no = req_obj.get('page_no')

            response = GET_WEATHER_DATA(date, weather_station_id).fetch_weather_data(page_no)
            app.logger.info("Request complete")
            return response, getattr(settings, response.get("status"))
        except Exception as e:
            app.logger.error(f"Error during weather stats fetch: {str(e)}")
            return {"error": str(e)}, 500
