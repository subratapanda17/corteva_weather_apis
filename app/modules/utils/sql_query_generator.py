class SQLQueryGenerator:
    def select(self, table_name, columns):
        query = f"SELECT {', '.join(columns)} FROM {table_name}"
        return query

    def where(self, conditions):
        query = f" WHERE {conditions}"
        return query

    def group_by(self, columns):
        query = f" GROUP BY {', '.join(columns)}"
        return query

    def having(self, conditions):
        query = f" HAVING {conditions}"
        return query

    def order_by(self, columns, ascending=True):
        query = f" ORDER BY {', '.join(columns)} {'ASC' if ascending else 'DESC'}"
        return query

    def limit(self, limit):
        query = f" LIMIT {limit}"
        return query

    def offset(self, offset):
        query = f" OFFSET {offset}"
        return query

    def count(self):
        query = f"SELECT COUNT(*) FROM {self.table_name}"
        return query

    def insert(self, table_name, values):
        columns = list(values.keys())
        placeholders = ', '.join(['%s'] * len(columns))
        query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({placeholders})"
        return query

    def update(self, table_name, updates, where_conditions):
        query = f"UPDATE {table_name} SET {', '.join(f'{key} = %s' for key in updates)}"
        if where_conditions:
            query += f" WHERE {where_conditions}"
        return query

    def delete(self, table_name, where_conditions):
        query = f"DELETE FROM {table_name}"
        if where_conditions:
            query += f" WHERE {where_conditions}"
        return query

    def on_conflict(self, columns, action="NOTHING"):
        query = f" ON CONFLICT ({', '.join(columns)}) DO {action}"
        return query