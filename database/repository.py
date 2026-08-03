import time

from database.connection import DatabaseConnection
from database.queries import IOCQueries


class IOCRepository:

    def __init__(self):

        self.conn = DatabaseConnection.get_connection()
        self.cursor = self.conn.cursor()

    # ==========================
    # READ
    # ==========================

    def get_all_iocs(self):

        self.cursor.execute(IOCQueries.GET_ALL)

        return self.cursor.fetchall()

    def get_ioc(self, ioc_id):

        self.cursor.execute(
            IOCQueries.GET_BY_ID,
            (ioc_id,)
        )

        return self.cursor.fetchone()

    def get_by_type(self, ioc_type):

        self.cursor.execute(
            IOCQueries.GET_BY_TYPE,
            (ioc_type,)
        )

        return self.cursor.fetchall()

    # ==========================
    # COUNT
    # ==========================

    def count(self):

        self.cursor.execute(IOCQueries.COUNT)

        return self.cursor.fetchone()[0]

    def count_ipv4(self):

        self.cursor.execute(

            IOCQueries.COUNT_IPV4

        )

        return self.cursor.fetchone()[0]

    def count_ipv6(self):

        self.cursor.execute(

            IOCQueries.COUNT_IPV6

        )

        return self.cursor.fetchone()[0]

    def count_domain(self):

        self.cursor.execute(IOCQueries.COUNT_DOMAIN)

        return self.cursor.fetchone()[0]

    def count_url(self):

        self.cursor.execute(IOCQueries.COUNT_URL)

        return self.cursor.fetchone()[0]

    def count_manual(self):

        self.cursor.execute(IOCQueries.COUNT_MANUAL)

        return self.cursor.fetchone()[0]

    # ==========================
    # EXISTS
    # ==========================

    def exists(self, ioc_id):

        self.cursor.execute(
            IOCQueries.EXISTS,
            (ioc_id,)
        )

        return self.cursor.fetchone()[0] > 0

    # ==========================
    # SAVE
    # ==========================

    def save(self, address):

        if self.exists(address.id):

            self.update(address)

        else:

            self.add(address)

    def save_many(self, addresses):

        for address in addresses:

            self.save(address)

        self.conn.commit()

    # ==========================
    # INSERT
    # ==========================

    def add(self, address):

        self.cursor.execute(

            IOCQueries.INSERT,

            (
                address.id,
                address.url,
                address.type,
                address.domain,
                address.ipv4,
                address.ipv6,
                address.desc,
                address.source,
                address.date,
                address.criticality_level,
                address.connectiontype,
                "API",
                1
            )

        )

    def add_manual_ioc(self, value, ioc_type):

        manual_id = -int(time.time() * 1000)

        domain = ""
        ipv4 = ""
        ipv6 = ""

        if ioc_type == "domain":

            domain = value

        elif ioc_type == "ipv4":

            ipv4 = value

        elif ioc_type == "ipv6":

            ipv6 = value


        self.cursor.execute(

            IOCQueries.INSERT,

            (
                manual_id,
                value,
                ioc_type,
                domain,
                ipv4,
                ipv6,
                "MANUAL",
                "USER",
                None,
                0,
                "MANUAL",
                "MANUAL",
                1
            )

        )

        self.conn.commit()

    # ==========================
    # UPDATE
    # ==========================

    def update(self, address):

        self.cursor.execute(

            IOCQueries.UPDATE,

            (
                address.url,
                address.type,
                address.domain,
                address.ipv4,
                address.ipv6,
                address.desc,
                address.source,
                address.date,
                address.criticality_level,
                address.connectiontype,
                address.id
            )

        )

    def update_manual_ioc(self, ioc_id, value, ioc_type):

        domain = ""
        ipv4 = ""
        ipv6 = ""

        if ioc_type == "domain":

            domain = value

        elif ioc_type == "ipv4":

            ipv4 = value

        elif ioc_type == "ipv6":

            ipv6 = value

        elif ioc_type == "url":

            from urllib.parse import urlparse

            parsed = urlparse(

                value if value.startswith(("http://", "https://"))
                else "http://" + value

            )

            domain = parsed.hostname or ""

        self.cursor.execute(

            IOCQueries.UPDATE_MANUAL,

            (

                value,
                ioc_type,
                domain,
                ipv4,
                ipv6,
                ioc_id

            )

        )

        self.conn.commit()

    def set_enabled(self, ioc_id, enabled):

        self.cursor.execute(

            IOCQueries.ENABLE,

            (
                enabled,
                ioc_id
            )

        )

        self.conn.commit()

    # ==========================
    # DELETE
    # ==========================

    def delete_ioc(self, ioc_id):

        self.cursor.execute(

            IOCQueries.DELETE,

            (ioc_id,)

        )

        self.conn.commit()

    def truncate_all(self):

        self.cursor.execute(IOCQueries.TRUNCATE)

        self.conn.commit()

    # ==========================
    # TRANSACTION
    # ==========================

    def commit(self):

        self.conn.commit()

    def rollback(self):

        self.conn.rollback()

    def close(self):

        if self.cursor:

            self.cursor.close()
