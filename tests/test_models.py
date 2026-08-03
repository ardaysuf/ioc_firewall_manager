from models import IOC
from models import FirewallRule


ioc = IOC(

    id=1,

    url="1.1.1.1",

    type="ip",

    desc="Test",

    source="API",

    date=None,

    criticality_level=4,

    connectiontype="PH"

)

print(ioc)

print(ioc.is_ip())

print(ioc.is_domain())

print(ioc.display_name)

print()

rule = FirewallRule(

    name="IOC_1.1.1.1",

    remote_address="1.1.1.1"

)

print(rule)
