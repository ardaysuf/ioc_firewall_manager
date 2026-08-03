from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QMessageBox,
    QProgressBar,
    QComboBox
)

from workers.sync_worker import SyncWorker


class SyncPage(QWidget):

    def __init__(self):

        super().__init__()

        self.worker = None

        self.setup_ui()

    def setup_ui(self):

        layout = QVBoxLayout()

        self.status = QLabel("Hazır")

        self.progress = QProgressBar()

        self.progress.setRange(0, 0)

        self.progress.hide()

        options_layout = QHBoxLayout()

        limit_label = QLabel("Çekilecek IOC Sayısı:")

        self.limit_combo = QComboBox()

        self.limit_combo.addItems(
            ["20", "50", "100", "200", "500", "1000"]
        )

        self.limit_combo.setCurrentText("100")

        options_layout.addWidget(limit_label)
        options_layout.addWidget(self.limit_combo)
        options_layout.addStretch()

        self.sync_button = QPushButton(
            "API'den IOC Senkronize Et"
        )

        self.sync_button.clicked.connect(
            self.start_sync
        )

        layout.addWidget(self.status)

        layout.addWidget(self.progress)

        layout.addLayout(options_layout)

        layout.addWidget(self.sync_button)

        layout.addStretch()

        self.setLayout(layout)

    def start_sync(self):

        self.sync_button.setEnabled(False)

        self.progress.show()

        self.status.setText("Senkronizasyon devam ediyor...")

        limit = int(self.limit_combo.currentText())

        self.worker = SyncWorker(limit=limit)

        self.worker.finished.connect(
            self.sync_finished
        )

        self.worker.failed.connect(
            self.sync_failed
        )

        self.worker.start()

    def sync_finished(self, result):

        self.progress.hide()

        self.sync_button.setEnabled(True)

        self.status.setText(

            f"{result['count']} IOC | {result['duration']} sn"

        )

        QMessageBox.information(

            self,

            "Tamamlandı",

            "Senkronizasyon başarıyla tamamlandı."

        )

    def sync_failed(self, message):

        self.progress.hide()

        self.sync_button.setEnabled(True)

        self.status.setText("Hata")

        QMessageBox.critical(

            self,

            "Hata",

            message

        )
