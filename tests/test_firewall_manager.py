from firewall.manager import FirewallManager


manager = FirewallManager()

print()

print("Firewall'daki IOC kuralları:")

print()

for rule in manager.list():

    print(rule)
