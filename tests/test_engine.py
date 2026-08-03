from firewall.engine import FirewallEngine


engine = FirewallEngine()

ips = engine.get_ip_iocs()
domains = engine.get_domain_iocs()
urls = engine.get_url_iocs()

print(f"IP      : {len(ips)}")
print(f"Domain  : {len(domains)}")
print(f"URL     : {len(urls)}")
