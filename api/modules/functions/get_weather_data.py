from api.connectors.SqlConnector import DB_CONNECTION
from api.modules.utils.sql_query_generator import SQLQueryGenerator
import pandas as pd
from datetime import datetime
import os
from flask import jsonify
import json


db = DB_CONNECTION('LOCAL')

class GET_WEATHER_DATA:
    """
        fetches weather data based of filters
        Args:
            date: int [YYYYMMDD]
            weather_station_id: str
        Returns:
            collected weather data from DB
    """
    def __init__(self, date:int=None, weather_station_id:str=None):
        """
            generates SQL query conditions (if applicable) based on filter selected by user
        """
        self.filters = []
        if date:
            self.filters.append(f"date = {date}")
        if weather_station_id:
            self.filters.append(f"weather_station_id = '{weather_station_id}'")
        
        self.conditions = " AND ".join(self.filters) if self.filters else ""


    def generate_select_query(self, page_no):
        """
            generates sql query based on provided conditions for
                fetching data
                counting total records
            Returns:
                raw SQL query, raw SQL query
        """
        count_generator = SQLQueryGenerator()
        query_generator = SQLQueryGenerator()
        limit = 50
        offset = (page_no-1)*limit

        if len(self.conditions)>0:
            count_query = (count_generator
                           .count('corveta_weather_record')
                           .where(self.conditions)
                           .build())
            query = (query_generator
                    .select('corveta_weather_record','*')
                    .where(self.conditions)
                    .limit(limit).offset(offset)
                    .build())
        else:
            count_query = (count_generator
                           .count('corveta_weather_record')
                           .build())
            query = (query_generator
                    .select('corveta_weather_record','*')
                    .limit(limit).offset(offset)
                    .build())
        return query, count_query

    def fetch_weather_data(self, page_no):
        """
            collects weather data from DB based on conditions
            Args:
                page_no: int [for paginated results]
            Returns:
                message: str [number of rows fetched]
                per_page: int [50 records]
                page_no: int
                total_pages: int
                total_records: int
                data: list[dict]
                    date: int,
                    id: int,
                    maxtemp: int,
                    mintemp: int,
                    rainfall: int,
                    uniq_id: str,
                    weather_station_id: str
        """
        if not page_no:
            page_no = 1

        select_query, count_query= self.generate_select_query(page_no)
        total_records = db.execute_query(count_query)[0][0]
        result = db.execute_query(select_query, dict_format=True)
        result = json.loads(result.data)

        if total_records > 0:
            return  {
                "status": "SUCCESS",
                "message": f"{len(result)} rows fetched",
                "page_no": page_no,
                "per_page": 50,
                "total_pages": int((total_records/50)+1),
                "total_records": total_records,
                "data": result
            }
        else:
            return {
                "status": "NOT_FOUND",
                "message": "no record found"
            }

