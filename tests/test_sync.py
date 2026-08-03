from services.sync_service import SyncService


service = SyncService()

result = service.sync_page()

print()

print(result)

service.close()
