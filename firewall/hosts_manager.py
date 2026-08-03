import os
import re
import subprocess

HOSTS_PATH = r"C:\Windows\System32\drivers\etc\hosts"
BLOCK_MARKER_START = "# === IOC_BLOCK_START ==="
BLOCK_MARKER_END   = "# === IOC_BLOCK_END ==="


class HostsManager:
    """
    Windows hosts dosyasını kullanarak domain'leri 0.0.0.0'a yönlendirerek engeller.
    IOC_BLOCK_START / IOC_BLOCK_END etiketleri arasında yönetilir.
    """

    @staticmethod
    def _read() -> str:
        with open(HOSTS_PATH, "r", encoding="utf-8", errors="replace") as f:
            return f.read()

    @staticmethod
    def _write(content: str):
        with open(HOSTS_PATH, "w", encoding="utf-8") as f:
            f.write(content)
        # DNS önbelleğini temizle — değişiklikler hemen geçerli olsun
        subprocess.run(
            ["ipconfig", "/flushdns"],
            capture_output=True, text=True
        )

    @staticmethod
    def _extract_block(content: str) -> list[str]:
        """Mevcut IOC bloğundaki domain'leri döndürür."""
        pattern = re.compile(
            rf"{re.escape(BLOCK_MARKER_START)}(.*?){re.escape(BLOCK_MARKER_END)}",
            re.DOTALL,
        )
        match = pattern.search(content)
        if not match:
            return []
        domains = []
        for line in match.group(1).splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                parts = line.split()
                if len(parts) >= 2:
                    domains.append(parts[1])
        return domains

    @staticmethod
    def _remove_block(content: str) -> str:
        """Mevcut IOC bloğunu içerikten temizler."""
        pattern = re.compile(
            rf"\n?{re.escape(BLOCK_MARKER_START)}.*?{re.escape(BLOCK_MARKER_END)}\n?",
            re.DOTALL,
        )
        return pattern.sub("", content)

    @staticmethod
    def _build_block(domains: set) -> str:
        if not domains:
            return ""
        lines = [BLOCK_MARKER_START]
        for d in sorted(domains):
            lines.append(f"0.0.0.0 {d}")
            lines.append(f"0.0.0.0 www.{d}")
        lines.append(BLOCK_MARKER_END)
        return "\n" + "\n".join(lines) + "\n"

    @classmethod
    def list(self) -> set:
        """Hosts dosyasındaki mevcut IOC domain'lerini döndürür."""
        try:
            content = HostsManager._read()
            return set(HostsManager._extract_block(content))
        except Exception:
            return set()

    @classmethod
    def sync(cls, domains: set) -> dict:
        """
        Verilen domain setini hosts dosyasıyla senkronize eder.
        Döndürür: {"created": int, "deleted": int, "skipped": int}
        """
        try:
            content = cls._read()
        except Exception as e:
            return {"created": 0, "deleted": 0, "skipped": 0, "error": str(e)}

        existing = set(cls._extract_block(content))

        to_add    = domains - existing
        to_remove = existing - domains
        skipped   = existing & domains

        new_domains = (existing | to_add) - to_remove

        clean = cls._remove_block(content)
        new_block = cls._build_block(new_domains)
        new_content = clean.rstrip("\n") + new_block

        try:
            cls._write(new_content)
        except PermissionError:
            return {
                "created": 0,
                "deleted": 0,
                "skipped": len(skipped),
                "error": "Hosts dosyasına yazma izni yok. Uygulamayı yönetici olarak çalıştırın."
            }

        return {
            "created": len(to_add),
            "deleted": len(to_remove),
            "skipped": len(skipped),
        }
