from database.repository import IOCRepository

repository = IOCRepository()

ips = repository.get_by_type("ip")

print(f"Toplam IP : {len(ips)}")

for ip in ips[:10]:
    print(ip)

repository.close()
