import sys
import ctypes

from PySide6.QtWidgets import QApplication, QMessageBox

from ui.main_window import MainWindow
from ui.theme import STYLE


def _is_admin() -> bool:
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except Exception:
        return False


def main():

    app = QApplication(sys.argv)
    app.setStyleSheet(STYLE)

    if not _is_admin():
        QMessageBox.warning(
            None,
            "⚠️  Yönetici Yetkisi Gerekli",
            "Bu uygulama yönetici yetkisi olmadan çalışıyor.\n\n"
            "Hosts dosyası ve Windows Firewall kuralları için yönetici yetkisi gereklidir.\n\n"
            "Lütfen uygulamayı sağ tıklayıp 'Yönetici olarak çalıştır' ile açın."
        )

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":

    main()
