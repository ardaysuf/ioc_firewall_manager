from PySide6.QtCore import QThread, Signal

from services.sync_service import SyncService


class SyncWorker(QThread):

    finished = Signal(dict)
    failed = Signal(str)

    def __init__(self, limit=100):

        super().__init__()

        self.limit = limit

    def run(self):

        try:

            service = SyncService()

            result = service.sync_with_limit(self.limit)

            self.finished.emit(result)

        except Exception as ex:

            import traceback
            traceback.print_exc()

            self.failed.emit(str(ex))
