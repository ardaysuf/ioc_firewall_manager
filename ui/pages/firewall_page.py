from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QMessageBox
)

from services.firewall_service import FirewallService


class FirewallPage(QWidget):

    def __init__(self):

        super().__init__()

        self.service = FirewallService()

        self.setup_ui()

    def setup_ui(self):

        layout = QVBoxLayout()

        self.sync_button = QPushButton(
            "Firewall'u Senkronize Et"
        )

        self.status_label = QLabel(
            "Hazır"
        )

        self.sync_button.clicked.connect(
            self.sync_firewall
        )

        layout.addWidget(self.sync_button)

        layout.addWidget(self.status_label)

        layout.addStretch()

        self.setLayout(layout)

    def sync_firewall(self):

        result = self.service.sync()

        self.status_label.setText(

            f"Oluşturulan: {result['created']}   "
            f"Silinen: {result['deleted']}   "
            f"Atlanan: {result['skipped']}"

        )

        QMessageBox.information(

            self,

            "Tamam",

            "Firewall senkronizasyonu tamamlandı."

        )
