from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLineEdit,
    QTableWidget,
    QTableWidgetItem,
    QMessageBox,
    QAbstractItemView,
    QHeaderView,
    QLabel
)

from services.ioc_service import IOCService
from ui.dialogs.add_ioc_dialog import AddIOCDialog
from ui.dialogs.edit_ioc_dialog import EditIOCDialog


class IOCPage(QWidget):

    def __init__(self):

        super().__init__()

        self.service = IOCService()

        self.setup_ui()

        self.load_data()

    def setup_ui(self):

        layout = QVBoxLayout()

        toolbar = QHBoxLayout()

        self.search = QLineEdit()
        self.search.setPlaceholderText("IOC Ara...")

        self.count_label = QLabel()

        self.add_button = QPushButton("IOC Ekle")
        self.delete_button = QPushButton("Sil")
        self.clear_button = QPushButton("VT Temizle")
        self.clear_button.setStyleSheet(
            "background: #C62828; color: white;"
        )
        self.refresh_button = QPushButton("Yenile")

        toolbar.addWidget(self.search)
        toolbar.addWidget(self.count_label)
        toolbar.addStretch()
        toolbar.addWidget(self.add_button)
        toolbar.addWidget(self.delete_button)
        toolbar.addWidget(self.clear_button)
        toolbar.addWidget(self.refresh_button)

        self.table = QTableWidget()

        self.table.setColumnCount(5)

        self.table.setHorizontalHeaderLabels(
            [
                "ID",
                "Değer",
                "Tür",
                "Kritiklik",
                "Kaynak"
            ]
        )

        self.table.setSelectionBehavior(
            QAbstractItemView.SelectRows
        )

        self.table.setSelectionMode(
            QAbstractItemView.SingleSelection
        )

        self.table.setEditTriggers(
            QAbstractItemView.NoEditTriggers
        )

        self.table.setAlternatingRowColors(True)

        self.table.verticalHeader().setVisible(False)

        self.table.horizontalHeader().setSectionResizeMode(
            0,
            QHeaderView.ResizeToContents
        )

        self.table.horizontalHeader().setSectionResizeMode(
            1,
            QHeaderView.Stretch
        )

        self.table.horizontalHeader().setSectionResizeMode(
            2,
            QHeaderView.ResizeToContents
        )

        self.table.horizontalHeader().setSectionResizeMode(
            3,
            QHeaderView.ResizeToContents
        )

        self.table.horizontalHeader().setSectionResizeMode(
            4,
            QHeaderView.ResizeToContents
        )

        layout.addLayout(toolbar)

        layout.addWidget(self.table)

        self.setLayout(layout)

        self.search.textChanged.connect(
            self.filter_table
        )

        self.refresh_button.clicked.connect(
            self.load_data
        )

        self.add_button.clicked.connect(
            self.add_ioc
        )

        self.delete_button.clicked.connect(
            self.delete_ioc
        )

        self.clear_button.clicked.connect(
            self.clear_db
        )

        self.table.doubleClicked.connect(
            self.edit_ioc
        )

    def load_data(self):

        rows = self.service.get_all_iocs()

        self.table.setRowCount(len(rows))

        self.count_label.setText(
            f"Toplam IOC : {len(rows)}"
        )

        for row, item in enumerate(rows):

            self.table.setItem(
                row,
                0,
                QTableWidgetItem(str(item.Id))
            )

            self.table.setItem(
                row,
                1,
                QTableWidgetItem(item.Value)
            )

            self.table.setItem(
                row,
                2,
                QTableWidgetItem(item.Type.upper())
            )

            level = str(item.CriticalityLevel)
            self.table.setItem(
                row,
                3,
                QTableWidgetItem(level)
            )

            self.table.setItem(
                row,
                4,
                QTableWidgetItem(item.Origin)
            )

    def filter_table(self):

        text = self.search.text().lower()

        visible = 0

        for row in range(self.table.rowCount()):

            show = False

            for col in range(self.table.columnCount()):

                item = self.table.item(row, col)

                if item and text in item.text().lower():

                    show = True
                    break

            self.table.setRowHidden(
                row,
                not show
            )

            if show:

                visible += 1

        self.count_label.setText(
            f"Gösterilen IOC : {visible}"
        )

    def add_ioc(self):

        dialog = AddIOCDialog()

        if dialog.exec():

            self.load_data()

    def edit_ioc(self):

        row = self.table.currentRow()

        if row == -1:

            return

        class IOC:
            pass

        obj = IOC()

        obj.Id = int(
            self.table.item(row, 0).text()
        )

        obj.Value = self.table.item(row, 1).text()
        obj.Type = self.table.item(row, 2).text().lower()

        dialog = EditIOCDialog(obj)

        if not dialog.exec():

            return

        data = dialog.get_data()

        self.service.update_manual_ioc(

            data["id"],

            data["value"],

            data["type"]

        )

        self.load_data()

    def delete_ioc(self):

        row = self.table.currentRow()

        if row == -1:

            QMessageBox.warning(

                self,

                "Uyarı",

                "Önce bir IOC seç."

            )

            return

        ioc_id = int(

            self.table.item(

                row,

                0

            ).text()

        )

        answer = QMessageBox.question(

            self,

            "Sil",

            "Seçilen IOC silinsin mi?"

        )

        if answer != QMessageBox.Yes:

            return

        self.service.delete_ioc(

            ioc_id

        )

        self.load_data()

    def clear_db(self):

        answer = QMessageBox.warning(

            self,

            "Veritabanını Temizle",

            "Tüm IOC kayıtları silinecek!\n"
            "Bu işlem geri alınamaz.\n\n"
            "Devam etmek istiyor musunuz?",

            QMessageBox.Yes | QMessageBox.No,

            QMessageBox.No

        )

        if answer != QMessageBox.Yes:

            return

        self.service.truncate_all()

        self.load_data()

        QMessageBox.information(

            self,

            "Tamamlandı",

            "Veritabanı başarıyla temizlendi."

        )
