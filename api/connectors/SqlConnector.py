import os
from dotenv import load_dotenv
load_dotenv()
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from flask import jsonify

class DB_CONNECTION:
    def __init__(self, env='LOCAL'):
        """
            Initializes the database connection based on the provided environment.

            Args:
                env: str | The environment for which to choose the connection URL. [defaul='LOCAL']
        """
        if env=='DEVELOPMENT':
            db_url = 'MYSQL_DEV_URL'
        elif env=='PRODUCTION':
            db_url = 'MYSQL_PROD_URL'
        else:
            db_url = 'MYSQL_LOCAL_URL'

        engine = create_engine(os.getenv(db_url))
        self.session = sessionmaker(bind=engine)

    def get_db(self):
        """
            Creates a new database sqlalchemy.orm.session.Session and returns it.
        """
        db = self.session()
        try:
            yield db
        finally:
            db.close()
    
    def execute_query(self, query, update=False, dict_format=False):
        """
            Executes a SQL query on the database and returns the results.

            Args:
                query: str | The SQL query to execute.
                update: bool | Whether the query is an update operation (defaults to False).
                dict_format: bool | Whether to return results as dictionaries (defaults to False).

            Returns:
                int - For update operations, returns number of rows updated.
                list - For select operations, returns a list of rows (tuples) or dictionaries (if dict_format is True).

            Raises:
                Exception: Any exception that occurs during query execution.
        """
        db = next(self.get_db())
        query = text(query)
        try:
            result = db.execute(query)
            if update:
                db.commit()
                return result.rowcount
            else:
                if dict_format==True:
                    data = [dict(row) for row in result.mappings()]
                    json_data = jsonify(data)
                    return json_data
                else:
                    return result.fetchall()
        except Exception as e:
            if update:
                db.rollback()
            raise e
        finally:
            db.close()