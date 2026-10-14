"""Pengaturan terpusat. Bisa diubah lewat environment variable tanpa edit kode."""
import os

BASE_URL = os.getenv("BASE_URL", "https://opensource-demo.orangehrmlive.com")
APP_PATH = "/web/index.php"
USERNAME = os.getenv("OHRM_USERNAME", "Admin")
PASSWORD = os.getenv("OHRM_PASSWORD", "admin123")
TIMEOUT = int(os.getenv("TIMEOUT", "10"))


def url(path: str = "") -> str:
    """Bangun URL lengkap, contoh: url('/auth/login') atau url('/web/index.php/auth/login')."""
    if path.startswith(APP_PATH):
        return BASE_URL.rstrip("/") + path
    return BASE_URL.rstrip("/") + APP_PATH + path
