import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()

class DB_CONNECTION:
    def __init__(self, env='LOCAL') -> None:
        if env=='DEVELOPMENT':
            self.db_url = 'POSTGRES_DEV_URL'
        elif env=='PRODUCTION':
            self.db_url = 'POSTGRES_PROD_URL'
        else:
            self.db_url = 'POSTGRES_LOCAL_URL'

        self.db = ''
        self.connection = psycopg2.connect(self.db_url)
        self.cursor = self.connection.cursor()
    
    def execute_query(self):
        pass