from connectors.SqlConnector import DB_CONNECTION
from utils.sql_query_generator import SQLQueryGenerator
import pandas as pd
from datetime import datetime


db = DB_CONNECTION('LOCAL')

class InsertWeatherData:
    def __init__(self) -> None:
        self.raw_data_path = '../../data/wx_data/'

    def iterate_data(self):
        df = pd.DataFrame()
        for index, row in df.iterrows():
            weather_station_id = row['weather_station_id']
            date = row['date']
            maxtemp = row['maxtemp']
            mintemp = row['mintemp']
            rainfall = row['rainfall']
            uniq_id = row['uniq_id']  # f""{weather_station_id}_{date}"
        
        def generate_query(self):
            generator = SQLQueryGenerator()
            insert_query = generator.insert(
                                            "my_table", {
                                                            "weather_station_id": weather_station_id, 
                                                            "date": date,
                                                            "maxtemp": maxtemp,
                                                            "mintemp": mintemp,
                                                            "rainfall": rainfall,
                                                            "uniq_id": uniq_id,
                                                            # "created_date": date,
                                                            "updated_date": datetime.now()
                                            }).on_conflict(["uniq_id"], "NOTHING").build()
    