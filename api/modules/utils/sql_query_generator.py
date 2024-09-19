
class SQLQueryGenerator:
    """
        This module has been created to simplify raw SQL query construction. Although most developers including myself are comfortable with writing raw queries themselves, this would provide the some advantages such as flexibility in query construciton, code maintainability, consistent querying and improved readability. 
        However, it does not support complex query construction yet, considering the time-frame for the coding challange; that feature will be implemented in later stages if possible after careful consideration.
    """
    def __init__(self):
        self.query_parts = []
        self.table_name = None
        self.values_list = []
    
    def select(self, table_name, columns):
        self.table_name = table_name
        self.query_parts.append(f"SELECT {', '.join(columns)} FROM {table_name}")
        return self

    def where(self, conditions):
        self.query_parts.append(f" WHERE {conditions}")
        return self

    def group_by(self, columns):
        self.query_parts.append(f" GROUP BY {', '.join(columns)}")
        return self

    def having(self, conditions):
        self.query_parts.append(f" HAVING {conditions}")
        return self

    def order_by(self, columns, ascending=True):
        self.query_parts.append(f" ORDER BY {', '.join(columns)} {'ASC' if ascending else 'DESC'}")
        return self

    def limit(self, limit):
        self.query_parts.append(f" LIMIT {limit}")
        return self

    def offset(self, offset):
        self.query_parts.append(f" OFFSET {offset}")
        return self

    def count(self, table_name):
        self.table_name = table_name
        if self.table_name:
            self.query_parts.append(f"SELECT COUNT(*) FROM {self.table_name}")
        return self

    def insert(self, table_name, values=None):
        self.table_name = table_name
        if values:
            columns = list(values.keys())
            value_strings = ', '.join(repr(value) for value in values.values())
            self.query_parts.append(f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({value_strings})")
        return self

    def insert_many(self, table_name, values):
        self.table_name = table_name
        if values:
            columns = list(values[0].keys())
            value_strings = ', '.join(
                f"({', '.join(repr(item[key]) for key in columns)})" 
                for item in values
            )
            self.query_parts.append(f"INSERT IGNORE INTO {table_name} ({', '.join(columns)}) VALUES {value_strings}")
        return self

    def update(self, table_name, updates, where_conditions=None):
        self.query_parts.append(f"UPDATE {table_name} SET {', '.join(f'{key} = %s' for key in updates)}")
        if where_conditions:
            self.query_parts.append(f" WHERE {where_conditions}")
        return self

    def delete(self, table_name, where_conditions=None):
        self.query_parts.append(f"DELETE FROM {table_name}")
        if where_conditions:
            self.query_parts.append(f" WHERE {where_conditions}")
        return self

    def on_conflict(self, columns, action="NOTHING"):
        self.query_parts.append(f" ON CONFLICT ({', '.join(columns)}) DO {action}")
        return self
    
    def build(self):
        return ' '.join(self.query_parts)
