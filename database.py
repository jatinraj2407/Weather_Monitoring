import psycopg2

class Database:
    def __init__(self):
        self.connection = psycopg2.connect(
            dbname='your_db_name', 
            user='your_user', 
            password='your_password', 
            host='localhost'
        )
        self.cursor = self.connection.cursor()

    def store_daily_summary(self, summary):
        insert_query = """
        INSERT INTO weather_summary (date, avg_temp, max_temp, min_temp, dominant_condition) 
        VALUES (%s, %s, %s, %s, %s)
        """
        self.cursor.execute(insert_query, (summary['date'], summary['avg_temp'], summary['max_temp'], summary['min_temp'], summary['dominant_condition']))
        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()
