from dataclasses import dataclass


@dataclass(slots=True)
class FirewallRule:

    name: str

    remote_address: str

    direction: str = "Outbound"

    action: str = "Block"

    enabled: bool = True
