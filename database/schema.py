from database.connection import DatabaseConnection


class DatabaseSchema:

    @staticmethod
    def create_database():

        conn = DatabaseConnection.get_connection()

        cursor = conn.cursor()

        cursor.execute("""

        IF OBJECT_ID('IOC','U') IS NULL

        BEGIN

            CREATE TABLE IOC
            (

                Id BIGINT PRIMARY KEY,

                Value NVARCHAR(500) NOT NULL,

                Type NVARCHAR(30) NOT NULL,

                Description NVARCHAR(100),

                Source NVARCHAR(30),

                IOCDate DATETIME,

                CriticalityLevel INT,

                ConnectionType NVARCHAR(30),

                Origin NVARCHAR(30),

                IsEnabled BIT DEFAULT 1,

                CreatedAt DATETIME DEFAULT GETDATE(),

                UpdatedAt DATETIME NULL

            )

        END

        """)

        conn.commit()
