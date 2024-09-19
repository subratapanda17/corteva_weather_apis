from flask_restx import reqparse

getWeatherStatsParser = reqparse.RequestParser()
getWeatherStatsParser.add_argument('year', type=int, required=True, help='Year to calculate weather stats YYYY', location='args')
getWeatherStatsParser.add_argument('weather_station_id', type=str, required=False, help='weather station id', location='args')

