from database.schema import DatabaseSchema


class DatabaseMigration:

    @staticmethod
    def migrate():

        DatabaseSchema.create_database()

        print()

        print("Database migration completed.")
