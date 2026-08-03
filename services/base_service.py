from database.repository import IOCRepository


class BaseService:

    def __init__(self):

        self.repository = IOCRepository()

    def commit(self):

        self.repository.commit()

    def rollback(self):

        self.repository.rollback()

    def close(self):

        self.repository.close()
