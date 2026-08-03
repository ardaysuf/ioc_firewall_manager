import requests

from api.endpoints import APIEndpoints
from api.exceptions import (
    APIConnectionError,
    APIResponseError
)


class FirewallAPI:

    def __init__(self):

        self.session = requests.Session()

        self.session.headers.update({

            "User-Agent": "Firewall v1.0"

        })

    def get_addresses(

        self,

        page=1,

        per_page=100,

        ioc_type=None

    ):

        params = {

            "page": page,

            "count": per_page

        }

        if ioc_type:

            params["type"] = ioc_type

        try:

            response = self.session.get(

                APIEndpoints.ADDRESS_INDEX,

                params=params,

                timeout=20

            )

        except requests.RequestException as ex:

            raise APIConnectionError(ex)

        if response.status_code != 200:

            raise APIResponseError(

                response.status_code

            )

        return response

    def get_all_addresses(

        self,

        per_page=100,

        ioc_type=None

    ):

        page = 1

        while True:

            response = self.get_addresses(

                page=page,

                per_page=per_page,

                ioc_type=ioc_type

            )

            data = response.json()

            yield data

            if page >= data["pageCount"]:

                break

            page += 1

    # ==========================
    # IOC Türleri
    # ==========================

    def get_all_ipv4(self):

        yield from self.get_all_addresses(

            ioc_type="ip"

        )

    def get_all_ipv6(self):

        yield from self.get_all_addresses(

            ioc_type="ip6"

        )

    def get_all_domains(self):

        yield from self.get_all_addresses(

            ioc_type="domain"

        )

    def get_all_urls(self):

        yield from self.get_all_addresses(

            ioc_type="url"

        )
