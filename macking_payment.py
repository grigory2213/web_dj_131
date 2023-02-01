import psycopg2
from psycopg2 import Error

try:
    # Connect to an existing database
    connection = psycopg2.connect(user="postgres",
                                  password="1234",
                                  host="localhost",
                                  port="",
                                  database="web_profpoint")

    # Create a cursor to perform database operations
    cursor = connection.cursor()

    cursor.execute(f"SELECT tokenized_bank_card FROM base_profile WHERE inn = '192837462398';")

    record = cursor.fetchone()
    print("Токенезированная карта человека :", record, "\n")

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")