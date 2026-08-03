from database.schema import DatabaseSchema

DatabaseSchema.create_database()
DatabaseSchema.create_ioc_table()
DatabaseSchema.create_sync_history_table()

print("Veritabanı yapısı kontrol edildi.")
