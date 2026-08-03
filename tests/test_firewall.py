from firewall.manager import FirewallManager


manager = FirewallManager()

rules = manager.get_rules()

print(f"Toplam Kural : {rules.Count}")

print()

print("İlk 10 Kural")

print("----------------------------")

count = 0

for rule in rules:

    print(rule.Name)

    count += 1

    if count == 10:

        break
