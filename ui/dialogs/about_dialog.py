from PySide6.QtWidgets import (
    QDialog,
    QLabel,
    QPushButton,
    QVBoxLayout
)


class AboutDialog(QDialog):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("Hakkında")

        self.resize(450, 220)

        layout = QVBoxLayout()

        title = QLabel(
            "<h2>Firewall IOC Manager</h2>"
        )

        info = QLabel(

            """
Versiyon : 1.0

IOC Yönetimi

Firewall Senkronizasyonu

API Senkronizasyonu

SQL Server Desteği

PySide6 Arayüzü
            """

        )

        close = QPushButton("Kapat")

        close.clicked.connect(self.accept)

        layout.addWidget(title)

        layout.addWidget(info)

        layout.addStretch()

        layout.addWidget(close)

        self.setLayout(layout)
