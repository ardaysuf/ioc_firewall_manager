from firewall.manager import FirewallManager


manager = FirewallManager()

rules = manager.list()

print(f"Toplam IOC Firewall Kuralı: {len(rules)}")
print()

for rule in rules:
    print(rule)
