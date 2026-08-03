from database.repository import IOCRepository

repository = IOCRepository()

repository.add_manual_ioc(
    value="example.com",
    ioc_type="domain"
)

repository.close()

print("Manuel IOC eklendi.")
