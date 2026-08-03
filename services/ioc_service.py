from services.base_service import BaseService


class IOCService(BaseService):

    def __init__(self):

        super().__init__()

    # ==================================================
    # READ
    # ==================================================

    def get_all_iocs(self):

        return self.repository.get_all_iocs()

    def get_ioc(self, ioc_id):

        return self.repository.get_ioc(ioc_id)

    def get_by_type(self, ioc_type):

        return self.repository.get_by_type(ioc_type)

    # ==================================================
    # COUNT
    # ==================================================

    def count(self):

        return self.repository.count()

    def statistics(self):

        return {

            "total": self.repository.count(),

            "ipv4": self.repository.count_ipv4(),

            "ipv6": self.repository.count_ipv6(),

            "domain": self.repository.count_domain(),

            "url": self.repository.count_url(),

            "manual": self.repository.count_manual()

        }

    # ==================================================
    # WRITE
    # ==================================================

    def add_manual_ioc(self, value, ioc_type):

        self.repository.add_manual_ioc(

            value,

            ioc_type

        )

    def update_manual_ioc(self, ioc_id, value, ioc_type):

        self.repository.update_manual_ioc(

            ioc_id,

            value,

            ioc_type

        )

    def delete_ioc(self, ioc_id):

        self.repository.delete_ioc(

            ioc_id

        )

    def set_enabled(self, ioc_id, enabled):

        self.repository.set_enabled(

            ioc_id,

            enabled

        )

    def save(self, address):

        self.repository.save(

            address

        )

    def save_many(self, addresses):

        self.repository.save_many(

            addresses

        )

    def truncate_all(self):

        self.repository.truncate_all()
