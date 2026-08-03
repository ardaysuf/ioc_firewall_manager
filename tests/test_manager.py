from firewall.manager import FirewallManager

manager = FirewallManager()

manager.sync_ip_rules()

print("\nTamamlandı.")
