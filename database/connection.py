import pyodbc

from core.config import Config


class DatabaseConnection:

    _connection = None

    @classmethod
    def get_connection(cls):

        if cls._connection is None:

            connection_string = (
                f"DRIVER={{{Config.DRIVER}}};"
                f"SERVER={Config.SQL_SERVER};"
                f"DATABASE={Config.DATABASE};"
                "Trusted_Connection=yes;"
                "TrustServerCertificate=yes;"
            )

            print(connection_string)

            print("DRIVER :", Config.DRIVER)

            print("SERVER :", Config.SQL_SERVER)

            print("DATABASE :", Config.DATABASE)

            cls._connection = pyodbc.connect(
                connection_string
            )

        return cls._connection

    @classmethod
    def close(cls):

        if cls._connection:

            cls._connection.close()

            cls._connection = None
