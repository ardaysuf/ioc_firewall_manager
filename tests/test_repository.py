from database.repository import IOCRepository


repository = IOCRepository()

print()

print("Toplam IOC")

print(repository.count())

print()

print("IP")

print(repository.count_ip())

print()

print("Domain")

print(repository.count_domain())

print()

print("URL")

print(repository.count_url())

print()

print("Manual")

print(repository.count_manual())

repository.close()
