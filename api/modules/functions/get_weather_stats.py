from api.connectors.SqlConnector import DB_CONNECTION
from api.modules.utils.sql_query_generator import SQLQueryGenerator
import pandas as pd
from datetime import datetime
import os


db = DB_CONNECTION('LOCAL')

class GET_WEATHER_STATS:
    def __init__(self):
        raw_data_path = 'api/data/wx_data/'
        self.all_weather_stn_data = pd.DataFrame()
        for file in os.listdir(raw_data_path):
            weather_station_id = file.split('.')[0]
            df = pd.read_csv(os.path.join(raw_data_path,file), delimiter='\t',header=None, names=['date','maxtemp','mintemp','rainfall'])
            df['weather_station_id'] = weather_station_id
            self.all_weather_stn_data = pd.concat([self.all_weather_stn_data,df], axis=0)
        
        self.all_weather_stn_data['uniq_id'] = self.all_weather_stn_data['weather_station_id'] + '_' + self.all_weather_stn_data['date'].astype(str)
        self.all_weather_stn_data.reset_index(drop=True,inplace=True)
        print("weather dataframe generated with cols", self.all_weather_stn_data.columns)

    def generate_insert_query(self, df, on_conflict_col='uniq_id', on_conflict_action='NOTHING'):
        generator = SQLQueryGenerator()
        val_list= []
        count=0
        for idx,row in df.iterrows():
            val_list.append({
                'date': row['date'],
                'maxtemp': row['maxtemp'],
                'mintemp': row['mintemp'],
                'rainfall': row['rainfall'],
                'weather_station_id': row['weather_station_id'],
                'uniq_id': row['uniq_id'],
            })
            count+=1
            # if count==20:
            #     break
        query = (generator
                 .insert_many('corveta_weather_record', val_list)
                 .build())
        return query

    def insert_weather_data(self):
        insert_query = self.generate_insert_query(self.all_weather_stn_data, 'uniq_id', 'NOTHING')

        rowscount = db.execute_query(insert_query, update=True)
        print(rowscount)

        response = {
            "status": "SUCCESS",
            "message": f"{rowscount} rows inserted"
        }
        return response

