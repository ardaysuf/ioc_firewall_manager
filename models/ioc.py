from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class IOC:

    id: int

    url: str

    type: str

    desc: str

    source: str

    date: datetime | str | None

    criticality_level: int

    connectiontype: str

    domain: str = ""

    ipv4: str = ""

    ipv6: str = ""

    @property
    def display_name(self):

        return self.url
