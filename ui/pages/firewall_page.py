from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QMessageBox,
    QGroupBox,
    QGridLayout
)

from services.firewall_service import FirewallService


class FirewallPage(QWidget):

    def __init__(self):

        super().__init__()

        self.service = FirewallService()

        self.setup_ui()

    def setup_ui(self):

        layout = QVBoxLayout()
        layout.setSpacing(12)

        self.sync_button = QPushButton(
            "🔄  Firewall'u Senkronize Et"
        )
        self.sync_button.clicked.connect(self.sync_firewall)

        # --- Sonuç Tablosu ---
        result_group = QGroupBox("Son Senkronizasyon Sonucu")
        grid = QGridLayout()
        grid.setSpacing(10)
        grid.setColumnMinimumWidth(0, 220)
        grid.setColumnMinimumWidth(1, 90)
        grid.setColumnMinimumWidth(2, 90)
        grid.setColumnMinimumWidth(3, 90)

        # Başlık satırı
        grid.addWidget(QLabel(""),                          0, 0)
        grid.addWidget(QLabel("<b>Oluşturulan</b>"),        0, 1)
        grid.addWidget(QLabel("<b>Silinen</b>"),            0, 2)
        grid.addWidget(QLabel("<b>Atlanan</b>"),            0, 3)

        # IP satırı
        grid.addWidget(QLabel("🔒 IP  (Windows Firewall)"), 1, 0)
        self.ip_created_label = QLabel("–")
        self.ip_deleted_label = QLabel("–")
        self.ip_skipped_label = QLabel("–")
        grid.addWidget(self.ip_created_label, 1, 1)
        grid.addWidget(self.ip_deleted_label, 1, 2)
        grid.addWidget(self.ip_skipped_label, 1, 3)

        # Domain satırı
        grid.addWidget(QLabel("🌐 Domain  (Hosts Dosyası)"), 2, 0)
        self.dom_created_label = QLabel("–")
        self.dom_deleted_label = QLabel("–")
        self.dom_skipped_label = QLabel("–")
        grid.addWidget(self.dom_created_label, 2, 1)
        grid.addWidget(self.dom_deleted_label, 2, 2)
        grid.addWidget(self.dom_skipped_label, 2, 3)

        # Toplam satırı
        grid.addWidget(QLabel("<b>📊 Toplam</b>"),          3, 0)
        self.total_created_label = QLabel("–")
        self.total_deleted_label = QLabel("–")
        self.total_skipped_label = QLabel("–")
        grid.addWidget(self.total_created_label, 3, 1)
        grid.addWidget(self.total_deleted_label, 3, 2)
        grid.addWidget(self.total_skipped_label, 3, 3)

        result_group.setLayout(grid)

        # --- Bilgi Notu ---
        info_label = QLabel(
            "🔒 IP → Windows Firewall\n"
            "🌐 Domain → Hosts dosyası (tüm domain engellenir)"
        )
        info_label.setWordWrap(True)

        layout.addWidget(self.sync_button)
        layout.addWidget(result_group)
        layout.addWidget(info_label)
        layout.addStretch()

        self.setLayout(layout)

    def sync_firewall(self):

        self.sync_button.setEnabled(False)
        self.sync_button.setText("⏳  Senkronize ediliyor...")

        result = self.service.sync()

        self.sync_button.setEnabled(True)
        self.sync_button.setText("🔄  Firewall'u Senkronize Et")

        self.ip_created_label.setText(str(result.get("ip_created", 0)))
        self.ip_deleted_label.setText(str(result.get("ip_deleted", 0)))
        self.ip_skipped_label.setText(str(result.get("ip_skipped", 0)))

        self.dom_created_label.setText(str(result.get("domain_created", 0)))
        self.dom_deleted_label.setText(str(result.get("domain_deleted", 0)))
        self.dom_skipped_label.setText(str(result.get("domain_skipped", 0)))

        self.total_created_label.setText(str(result.get("created", 0)))
        self.total_deleted_label.setText(str(result.get("deleted", 0)))
        self.total_skipped_label.setText(str(result.get("skipped", 0)))

        if result.get("hosts_error"):
            QMessageBox.warning(
                self, "Uyarı",
                f"Domain (Hosts): {result['hosts_error']}"
            )
        else:
            QMessageBox.information(
                self, "Tamam",
                "Firewall senkronizasyonu tamamlandı."
            )
