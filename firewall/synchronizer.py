from firewall.manager import FirewallManager
from firewall.hosts_manager import HostsManager

from core.settings import Settings
from services.ioc_service import IOCService


# GET_BY_TYPE sorgusu sütun sırası: (Id, Value, Type, Domain, IPv4, IPv6)
_COL_DOMAIN = 3
_COL_IPV4   = 4
_COL_IPV6   = 5


class FirewallSynchronizer:

    def __init__(self):

        self.manager = FirewallManager()

        self.service = IOCService()

    def sync(self):

        # ==========================
        # Mevcut kuralları al
        # ==========================

        firewall_ips  = self.manager.list()
        hosts_domains = HostsManager.list()

        # ==========================
        # Veritabanındaki kayıtları al
        # ==========================

        db_ips     = set()
        db_domains = set()

        if Settings.BLOCK_IPV4:

            for row in self.service.get_by_type("ipv4"):

                val = row[_COL_IPV4]

                if val:
                    db_ips.add(val)

        if Settings.BLOCK_IPV6:

            for row in self.service.get_by_type("ipv6"):

                val = row[_COL_IPV6]

                if val:
                    db_ips.add(val)

        if Settings.BLOCK_DOMAIN:

            for row in self.service.get_by_type("domain"):

                val = row[_COL_DOMAIN]

                if val:
                    db_domains.add(val)

        print(f"DB — IP: {len(db_ips)}, Domain: {len(db_domains)}")
        print(f"Firewall — IP: {len(firewall_ips)}, Hosts domain: {len(hosts_domains)}")

        # ==========================
        # IP — Windows Firewall Sync
        # ==========================

        ip_to_create = db_ips - firewall_ips
        ip_to_delete = firewall_ips - db_ips
        ip_skipped   = len(db_ips & firewall_ips)

        ip_created = 0
        ip_deleted = 0

        if ip_to_create:

            if self.manager.create_many(list(ip_to_create)):

                ip_created = len(ip_to_create)

        if ip_to_delete:

            if self.manager.delete_many(list(ip_to_delete)):

                ip_deleted = len(ip_to_delete)

        # ==========================
        # Domain — Hosts Dosyası Sync
        # ==========================

        hosts_result = HostsManager.sync(db_domains)

        domain_created = hosts_result.get("created", 0)
        domain_deleted = hosts_result.get("deleted", 0)
        domain_skipped = hosts_result.get("skipped", 0)
        hosts_error    = hosts_result.get("error", None)

        if hosts_error:
            print(f"[HOSTS HATA] {hosts_error}")

        return {

            "created": ip_created + domain_created,
            "deleted": ip_deleted + domain_deleted,
            "skipped": ip_skipped + domain_skipped,

            "ip_created":     ip_created,
            "ip_deleted":     ip_deleted,
            "ip_skipped":     ip_skipped,

            "domain_created": domain_created,
            "domain_deleted": domain_deleted,
            "domain_skipped": domain_skipped,

            "hosts_error":    hosts_error,

        }
