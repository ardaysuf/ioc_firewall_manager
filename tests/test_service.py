from services.ioc_service import IOCService


service = IOCService()

print()

print(service.statistics())

print()

print(service.count())

service.close()
