from services.firewall_service import FirewallService


service = FirewallService()

result = service.sync()

print(result)
