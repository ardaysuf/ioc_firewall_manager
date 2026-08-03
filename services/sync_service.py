import time
import math
import concurrent.futures

from logs.logger import logger

from api.client import FirewallAPI
from api.parser import AddressParser

from services.base_service import BaseService


class SyncService(BaseService):

    def __init__(self):

        super().__init__()

        self.api = FirewallAPI()

    def sync_with_limit(self, limit=100):

        start = time.time()

        logger.info(
            f"Senkronizasyon başladı. Hedef: {limit} IOC"
        )

        total = 0
        sources_types = ["ip", "ip6", "domain", "url"]
        per_type_limit = math.ceil(limit / len(sources_types))
        api_page_size = 20
        pages_needed = math.ceil(per_type_limit / api_page_size)

        for page in range(1, pages_needed + 1):

            if total >= limit:
                break

            with concurrent.futures.ThreadPoolExecutor(
                max_workers=4
            ) as executor:

                futures = [
                    executor.submit(
                        self.api.get_addresses,
                        page, api_page_size, ioc_type
                    )
                    for ioc_type in sources_types
                ]

                for future in concurrent.futures.as_completed(
                    futures
                ):
                    data = future.result().json()
                    addresses = AddressParser.parse(data)
                    self.repository.save_many(addresses)
                    total += len(addresses)

        duration = round(time.time() - start, 2)

        logger.info(
            f"{total} IOC senkronize edildi. ({duration} sn)"
        )

        return {

            "count": total,

            "duration": duration

        }
