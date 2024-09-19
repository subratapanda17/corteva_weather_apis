from flask_restx import reqparse

getWeatherDataParser = reqparse.RequestParser()
getWeatherDataParser.add_argument('date', type=int, required=False, help='Date of the weather data in YYYYMMDD format', location='args')
getWeatherDataParser.add_argument('weather_station_id', type=str, required=False, help='weather station id', location='args')
getWeatherDataParser.add_argument('page_no', type=int, required=False, help='weather station id', location='args')

