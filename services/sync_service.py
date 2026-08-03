import time

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

        try:

            # Tür filtresi yok → API en son IOC'leri tarihe göre karma döndürür
            # API sayfa başına max 20 döndürüyor, limit dolana kadar sayfa sayfa çek
            page = 1
            api_page_size = 20

            while total < limit:

                response = self.api.get_addresses(
                    page=page,
                    per_page=api_page_size,
                    ioc_type=None
                )

                data = response.json()
                addresses = AddressParser.parse(data)

                if not addresses:
                    break  # API'nin sonu

                # Limiti aşmamak için kalan kadar al
                remaining = limit - total
                addresses = addresses[:remaining]

                self.repository.save_many(addresses)
                total += len(addresses)

                # Son sayfa mı?
                if page >= data.get("pageCount", 1):
                    break

                page += 1

        except Exception as e:

            logger.error(f"Senkronizasyon hatası: {e}")

        duration = round(time.time() - start, 2)

        logger.info(
            f"{total} IOC senkronize edildi. ({duration} sn)"
        )

        return {

            "count": total,

            "duration": duration

        }

