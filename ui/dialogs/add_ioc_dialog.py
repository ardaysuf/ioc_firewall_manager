from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QComboBox,
    QPushButton,
    QMessageBox
)

from database.repository import IOCRepository


class AddIOCDialog(QDialog):

    def __init__(self):

        super().__init__()

        self.repository = IOCRepository()

        self.setWindowTitle("Yeni IOC")

        self.setFixedSize(400, 180)

        layout = QVBoxLayout()

        row1 = QHBoxLayout()

        row1.addWidget(QLabel("IOC"))

        self.value = QLineEdit()

        row1.addWidget(self.value)

        layout.addLayout(row1)

        row2 = QHBoxLayout()

        row2.addWidget(QLabel("Tür"))

        self.type = QComboBox()

        self.type.addItems(

            [

                "ipv4",

                "ipv6",

                "domain",

                "url"

            ]

        )

        row2.addWidget(self.type)

        layout.addLayout(row2)

        buttons = QHBoxLayout()

        save = QPushButton("Kaydet")

        cancel = QPushButton("İptal")

        buttons.addWidget(save)

        buttons.addWidget(cancel)

        layout.addLayout(buttons)

        self.setLayout(layout)

        save.clicked.connect(self.save)

        cancel.clicked.connect(self.close)

    def save(self):

        value = self.value.text().strip()

        if value == "":

            QMessageBox.warning(
                self,
                "Hata",
                "IOC boş olamaz."
            )

            return

        self.repository.add_manual_ioc(
            value,
            self.type.currentText()
        )

        self.repository.close()

        self.accept()
