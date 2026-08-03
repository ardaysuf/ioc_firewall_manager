from firewall.manager import FirewallManager

from core.settings import Settings
from services.ioc_service import IOCService


class FirewallSynchronizer:

    def __init__(self):

        self.manager = FirewallManager()

        self.service = IOCService()

    def sync(self):

        firewall_rules = self.manager.list()

        sql_ips = set()

        # ==========================
        # IPv4
        # ==========================

        if Settings.BLOCK_IPV4:

            for row in self.service.get_by_type("ipv4"):

                if row.IPv4:

                    sql_ips.add(row.IPv4)

        # ==========================
        # IPv6
        # ==========================

        if Settings.BLOCK_IPV6:

            for row in self.service.get_by_type("ipv6"):

                if row.IPv6:

                    sql_ips.add(row.IPv6)

        # ==========================
        # Firewall Sync
        # ==========================

        to_create = sql_ips - firewall_rules

        to_delete = firewall_rules - sql_ips

        skipped = len(sql_ips & firewall_rules)

        created = 0

        deleted = 0

        if to_create:

            if self.manager.create_many(list(to_create)):

                created = len(to_create)

        if to_delete:

            if self.manager.delete_many(list(to_delete)):

                deleted = len(to_delete)

        return {

            "created": created,

            "deleted": deleted,

            "skipped": skipped

        }
