from PySide6.QtWidgets import (
    QMainWindow,
    QTabWidget,
    QStatusBar
)

from ui.dialogs.about_dialog import AboutDialog

from ui.pages.dashboard_page import DashboardPage
from ui.pages.ioc_page import IOCPage
from ui.pages.sync_page import SyncPage
from ui.pages.firewall_page import FirewallPage


class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("Firewall IOC Manager")

        self.resize(1200, 750)

        self.dashboard = DashboardPage()

        self.tabs = QTabWidget()

        self.tabs.addTab(self.dashboard, "Dashboard")
        self.tabs.addTab(IOCPage(), "IOC")
        self.tabs.addTab(SyncPage(), "Synchronization")
        self.tabs.addTab(FirewallPage(), "Firewall")

        self.tabs.currentChanged.connect(self.on_tab_changed)

        self.setCentralWidget(self.tabs)

        self.status = QStatusBar()

        self.status.showMessage("Hazır")

        self.setStatusBar(self.status)

    def on_tab_changed(self, index):
        if index == 0:
            self.refresh_dashboard()

    def refresh_dashboard(self):

        self.dashboard.refresh()

        self.status.showMessage(
            "Dashboard güncellendi."
        )

    def show_about(self):

        dialog = AboutDialog()

        dialog.exec()
