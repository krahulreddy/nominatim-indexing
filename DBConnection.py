import psycopg2
from psycopg2.extras import RealDictCursor, DictCursor, register_hstore
import json
import logging


class DBConnection:
    def __init__(self):
        self.connection = self.connect_to_db()

    def test_connection(self):
        '''
            Tests the connection to DB by getting dsn parameters of the connection
            and executing a test query
        '''
        self.connection.get_dsn_parameters()
        self.connection.fetch_test()

    def connect_to_db(self):
        '''
        Tries to create a connection to the Nominatim postresql DB
        '''
        logging.debug("=================================================================")
        logging.debug("Trying to create a connection")
        try:
            connection = psycopg2.connect(
                user="nominatim",         # Provide a user with read only permission
                                          # to avoid security issues
                                          
                password="",              # Replace with your password while using
                host="127.0.0.1",
                port="5432",
                database="nominatim"
            )

            # Nominatim uses hstore datatype to store few fields like name.
            # register_hstore will help fetch those fields as dictionary objects.
            register_hstore(connection, globally=True, unicode=True)
            logging.debug("Success")
            return connection
        except:
            logging.debug("Failed")
            exit

    def get_dsn_parameters(self):
        '''
        logging.debugs the DSN parameters of the existing connection for debugging.
        '''
        logging.debug("=================================================================")
        logging.debug("Trying to logging.debug DSN parameters: ")
        try:
            logging.debug(self.connection.connection.get_dsn_parameters())
        except:
            logging.debug("Failed")
            exit
 
    def fetch_test(self):
        '''
        Executes a test query on the connection
        '''
        logging.debug("=================================================================")
        logging.debug("Trying to fetch from placex table: ")

        try:
            sql = "SELECT * from placex limit 1;"
            cursor = self.connection.cursor(cursor_factory=DictCursor)
            cursor.execute(sql)
            record = cursor.fetchone()
            logging.debug(sql, "\n")
            logging.debug(json.dumps(record))
            cursor.close()

        except:
            logging.debug("Failed")
            exit

    def close_connection(self):
        '''
        Closes the connection to the DB 
        '''
        self.connection.close()
