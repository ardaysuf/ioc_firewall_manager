from firewall.policy import FirewallPolicy

policy = FirewallPolicy()

rules = policy.get_rules()

print(f"Toplam kural sayısı : {rules.Count}")
