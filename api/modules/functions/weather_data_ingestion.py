from api.connectors.SqlConnector import DB_CONNECTION
from api.modules.utils.sql_query_generator import SQLQueryGenerator
import pandas as pd
from datetime import datetime
import os
from flask import current_app as app
from api.config import settings


db = DB_CONNECTION(settings.DB_TYPE)
sql_table_name = settings.SQL_TABLE_NAME

class INGEST_WEATHER_DATA:
    """
        Processes the data from the provided weather data files and inserts the data into MySQL Database
        Returns:
            message: stating if the data ingestion is successful (with number of rows inserted) or not
    """
    def __init__(self):
        """
            Processes the weather data collected from all files in the specified directory and creates a pandas dataframe
        """
        raw_data_path = 'api/data/wx_data/'
        self.error = None
        try:
            self.all_weather_stn_data = pd.DataFrame()
            for file in os.listdir(raw_data_path):
                weather_station_id = file.split('.')[0]
                df = pd.read_csv(os.path.join(raw_data_path,file), delimiter='\t',header=None, names=['date','maxtemp','mintemp','rainfall'])
                df['weather_station_id'] = weather_station_id
                self.all_weather_stn_data = pd.concat([self.all_weather_stn_data,df], axis=0)
            
            self.all_weather_stn_data['uniq_id'] = self.all_weather_stn_data['weather_station_id'] + '_' + self.all_weather_stn_data['date'].astype(str)
            self.all_weather_stn_data.reset_index(drop=True,inplace=True)
            print(self.all_weather_stn_data.shape)
        except:
            self.error = "no data file found  in directory to insert"
            

    def generate_insert_query(self, df):
        """
            generates insert query data
            Returns:
                    RAW sql query
        """
        generator = SQLQueryGenerator()
        val_list= []
        for idx,row in df.iterrows():
            val_list.append({
                'date': row['date'],
                'maxtemp': row['maxtemp'],
                'mintemp': row['mintemp'],
                'rainfall': row['rainfall'],
                'weather_station_id': row['weather_station_id'],
                'uniq_id': row['uniq_id'],
            })

        query = (generator
                 .insert_many(sql_table_name, val_list)
                 .build())
        return query

    def insert_weather_data(self):
        """
            fetches the insert query and executes it
            Returns:
                json stating api completion/failure
                    message: str
        """
        if self.error:
            app.logger.error("no data file found  in directory to insert")
            return {
                "status" : "NOT_FOUND",
                "message" : "no data file found in directory to insert"
            }
        
        batch_size = 10000
        total_rows = self.all_weather_stn_data.shape[0]
        total_batches = (total_rows // batch_size) + (total_rows % batch_size > 0)
        app.logger.info(f"Inserting data in {total_batches} batches, each with a size of {batch_size} rows")

        total_inserted_rows = 0
        st_time = datetime.now()

        # data insertion in batches
        for i in range(total_batches):
            start_idx = i * batch_size
            end_idx = min(start_idx + batch_size, total_rows)
            batch_df = self.all_weather_stn_data.iloc[start_idx:end_idx]

            batch_st_time = datetime.now()
            insert_query = self.generate_insert_query(batch_df)
            rows_inserted = db.execute_query(insert_query, update=True)
            batch_et_time = datetime.now()

            batch_time_taken = (batch_et_time - batch_st_time).total_seconds()

            total_inserted_rows += rows_inserted
            app.logger.info(f"Batch {i+1}/{total_batches}: Inserted {rows_inserted} rows | Time taken = {batch_time_taken:.2f} seconds")
        
        et_time = datetime.now()
        total_time_taken = (et_time - st_time).total_seconds()

        if total_inserted_rows > 0:
            app.logger.info(f"Total {total_inserted_rows} rows inserted | Total time taken = {total_time_taken:.2f} seconds")
            response = {
                "status": "SUCCESS",
                "message": f"{total_inserted_rows} rows inserted"
            }
        
        else:
            app.logger.error(f"No rows inserted (data may already exist) | Total time taken = {total_time_taken:.2f} seconds")
            response = {
                "status": "CONFLICT",
                "message": "Selected data already present in DB or no new rows inserted"
            }

        return response

