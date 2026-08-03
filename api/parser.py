from urllib.parse import urlparse

from models import IOC


class AddressParser:

    @staticmethod
    def parse(data):

        addresses = []

        for model in data["models"]:

            value = model["url"]
            ioc_type = model["type"]

            domain = ""
            ipv4 = ""
            ipv6 = ""

            if ioc_type == "ip":

                ioc_type = "ipv4"
                ipv4 = value

            elif ioc_type == "ip6":

                ioc_type = "ipv6"
                ipv6 = value

            elif ioc_type == "domain":

                domain = value

            elif ioc_type == "url":

                parsed = urlparse(
                    value if value.startswith(("http://", "https://"))
                    else "http://" + value
                )

                domain = parsed.hostname or ""

            addresses.append(

                IOC(

                    id=model["id"],

                    url=value,

                    type=ioc_type,

                    desc=model["desc"],

                    source=model["source"],

                    date=model["date"],

                    criticality_level=model["criticality_level"],

                    connectiontype=model["connectiontype"],

                    domain=domain,

                    ipv4=ipv4,

                    ipv6=ipv6

                )

            )

        return addresses
