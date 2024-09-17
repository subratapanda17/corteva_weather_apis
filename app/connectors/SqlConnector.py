import os
from dotenv import load_dotenv
load_dotenv()
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DB_CONNECTION:
    def __init__(self, env='LOCAL'):
        """
            Initializes the database connection based on the provided environment.

            Args:
                env (str, optional): The environment for which to choose the connection URL. [defaul='LOCAL']
        """
        if env=='DEVELOPMENT':
            db_url = 'POSTGRES_DEV_URL'
        elif env=='PRODUCTION':
            db_url = 'POSTGRES_PROD_URL'
        else:
            db_url = 'POSTGRES_LOCAL_URL'

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
                query (str): The SQL query to execute.
                update (bool, optional): Whether the query is an update operation (defaults to False).
                dict_format (bool, optional): Whether to return results as dictionaries (defaults to False).

            Returns:
                bool - For update operations, returns True if successful, False otherwise.
                list - For select operations, returns a list of rows (tuples) or dictionaries (if dict_format is True).

            Raises:
                Exception: Any exception that occurs during query execution.
        """
        db = next(self.get_db())
        try:
            result = db.execute(query)
            if update:
                db.commit()
                return result.rowcount > 0
            else:
                if update==True:
                    return result.mappings().all()
                else:
                    return result.fetchall()
        except Exception as e:
            if update:
                db.rollback()
            raise e
        finally:
            db.close()