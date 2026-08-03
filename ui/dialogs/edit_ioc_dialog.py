from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QComboBox,
    QPushButton,
    QHBoxLayout
)


class EditIOCDialog(QDialog):

    def __init__(self, row):

        super().__init__()

        self.setWindowTitle("IOC Düzenle")

        self.resize(450, 180)

        self.ioc_id = row.Id

        layout = QVBoxLayout()

        layout.addWidget(QLabel("IOC"))

        self.value = QLineEdit(row.Value)

        layout.addWidget(self.value)

        layout.addWidget(QLabel("Tür"))

        self.type = QComboBox()

        self.type.addItems(

            [

                "ip",

                "domain",

                "url"

            ]

        )

        index = self.type.findText(

            row.Type.lower()

        )

        if index >= 0:

            self.type.setCurrentIndex(index)

        layout.addWidget(self.type)

        buttons = QHBoxLayout()

        save = QPushButton("Kaydet")

        cancel = QPushButton("İptal")

        save.clicked.connect(self.accept)

        cancel.clicked.connect(self.reject)

        buttons.addStretch()

        buttons.addWidget(save)

        buttons.addWidget(cancel)

        layout.addLayout(buttons)

        self.setLayout(layout)

    def get_data(self):

        return {

            "id": self.ioc_id,

            "value": self.value.text().strip(),

            "type": self.type.currentText()

        }
