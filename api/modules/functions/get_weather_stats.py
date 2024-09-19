from api.connectors.SqlConnector import DB_CONNECTION
from api.modules.utils.sql_query_generator import SQLQueryGenerator
import pandas as pd
import json


db = DB_CONNECTION('LOCAL')

class GET_WEATHER_STATS:
    """
        fetches weather data based of filters (if present) and returns the weather statistics
        Args: 
            year: int [ex: YYYY]
            weather_station_id: str [ex: 'USC00134735']
        Returns:
            staistics of the weather data for required weather station and year
    """

    def __init__(self, year:int=None, weather_station_id:int=None):
        """
            generates SQL query conditions (if applicable) based on filter selected by user
        """
        self.year = year
        self.weather_station_id = weather_station_id
        self.filters = []
        if year:
            st_date = int(f"{year}0101")
            ed_date = int(f"{year}1231")
            self.filters.append(f"date BETWEEN {st_date} AND {ed_date}")
        if weather_station_id:
            self.filters.append(f"weather_station_id = '{weather_station_id}'")
        
        self.conditions = " AND ".join(self.filters) if self.filters else ""

    def generate_select_query(self):
        """
            generates raw SQL query with/without filters
            Returns:
                raw SQL query
        """
        query_generator = SQLQueryGenerator()

        if len(self.conditions)>0:
            query = (query_generator
                    .select('corveta_weather_record','*')
                    .where(self.conditions)
                    .build())
        else:
            query = (query_generator
                    .select('corveta_weather_record','*')
                    .build())
        return query

    def fetch_weather_data(self):
        """
            fetches the data from sql based on required conditions
            Returns:
                a generated pandas dataframe of the data collected
        """
        select_query= self.generate_select_query()
        result = db.execute_query(select_query, dict_format=True)
        result = json.loads(result.data)
        result_df = pd.DataFrame(result)

        return result_df
    
    def get_stats(self):
        """
            fetches weather data from DB and generated required reports
            Returns:
                list of weather data statistics for selected criteria
                    year: int
                    weather_station_id: int
                    average_max_temp: float
                    average_min_temp: float
                    total_precipitation_cm: float

        """
        df = self.fetch_weather_data()
        if len(df) == 0:
            response =  {
                "status": "NOT_FOUND",
                "message": "No data available for the given criteria"
            }
            return response
        
        df = df.replace(-9999, pd.NA).drop(columns=['id']) #replacing the noDataValue with NAN
        df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')
        df['year'] = df['date'].dt.year
        df['month'] = df['date'].dt.month
        df['day'] = df['date'].dt.day
        df['maxtemp'] = df['maxtemp'] / 10  # Convert tenths of degree Celsius to degrees Celsius
        df['mintemp'] = df['mintemp'] / 10  # Convert tenths of degree Celsius to degrees Celsius
        df['rainfall'] = df['rainfall'] / 100 # Convert tenths of millimeter to centimeters

        if self.year:
            df = df[df['year'] == self.year]
        if self.weather_station_id:
            df = df[df['weather_station_id'] == self.weather_station_id]

        stats = df.groupby(['year', 'weather_station_id']).agg(
                    average_max_temp=('maxtemp', 'mean'),
                    average_min_temp=('mintemp', 'mean'),
                    total_precipitation_cm=('rainfall', 'sum')
                ).reset_index()
        
        #changing the data type fomr object to float
        stats['average_max_temp'] = stats['average_max_temp'].astype(float)
        stats['average_min_temp'] = stats['average_min_temp'].astype(float)
        stats['total_precipitation_cm'] = stats['total_precipitation_cm'].astype(float)

        #rounding off the values to 2 decimal points
        stats['average_max_temp'] = stats['average_max_temp'].round(2)
        stats['average_min_temp'] = stats['average_min_temp'].round(2)
        stats['total_precipitation_cm'] = stats['total_precipitation_cm'].round(2)
        
        stats_dict = stats.to_dict(orient='records')
        response = {
            "status": "SUCCESS",
            "message": f"weather stats fetched",
            "data": stats_dict
        }

        return response

