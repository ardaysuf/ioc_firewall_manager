from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QGridLayout,
    QVBoxLayout,
    QPushButton
)

from services.ioc_service import IOCService


class DashboardPage(QWidget):

    def __init__(self):

        super().__init__()

        self.service = IOCService()

        self.setup_ui()

        self.refresh()

    def setup_ui(self):

        layout = QVBoxLayout()

        grid = QGridLayout()

        self.total = QLabel()
        self.ipv4 = QLabel()
        self.ipv6 = QLabel()
        self.domain = QLabel()
        self.url = QLabel()
        self.manual = QLabel()

        cards = [

            ("Toplam IOC", self.total),

            ("IPv4 IOC", self.ipv4),

            ("IPv6 IOC", self.ipv6),

            ("Domain IOC", self.domain),

            ("URL IOC", self.url),

            ("Manuel IOC", self.manual)

        ]

        row = 0
        col = 0

        for title, label in cards:

            card = QWidget()

            card_layout = QVBoxLayout(card)

            title_label = QLabel(title)

            title_label.setAlignment(Qt.AlignCenter)

            title_label.setStyleSheet(
                "font-size:16px;font-weight:bold;"
            )

            label.setAlignment(Qt.AlignCenter)

            label.setStyleSheet(
                "font-size:28px;font-weight:bold;color:#1976D2;"
            )

            card_layout.addWidget(title_label)

            card_layout.addWidget(label)

            card.setStyleSheet("""

                QWidget{

                    border:1px solid gray;

                    border-radius:8px;

                    padding:12px;

                }

            """)

            grid.addWidget(card, row, col)

            col += 1

            if col == 3:

                row += 1

                col = 0

        layout.addLayout(grid)

        self.refresh_button = QPushButton(
            "Yenile"
        )

        self.refresh_button.clicked.connect(
            self.refresh
        )

        layout.addWidget(self.refresh_button)

        layout.addStretch()

        self.setLayout(layout)

    def refresh(self):

        stats = self.service.statistics()

        self.total.setText(

            str(stats["total"])

        )

        self.ipv4.setText(

            str(stats["ipv4"])

        )

        self.ipv6.setText(

            str(stats["ipv6"])

        )

        self.domain.setText(

            str(stats["domain"])

        )

        self.url.setText(

            str(stats["url"])

        )

        self.manual.setText(

            str(stats["manual"])

        )
