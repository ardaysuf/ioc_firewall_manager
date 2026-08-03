from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout
)


class StatusCard(QFrame):

    def __init__(self, title, value):

        super().__init__()

        self.setMinimumHeight(120)

        layout = QVBoxLayout()

        self.title = QLabel(title)
        self.title.setAlignment(Qt.AlignCenter)

        self.value = QLabel(str(value))
        self.value.setAlignment(Qt.AlignCenter)

        self.title.setObjectName("CardTitle")
        self.value.setObjectName("CardValue")

        layout.addWidget(self.title)
        layout.addWidget(self.value)

        self.setLayout(layout)
