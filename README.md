# Tugas 4 – Selenium WebDriver (Python) – OrangeHRM Demo

Proyek ini menguji https://opensource-demo.orangehrmlive.com (login `Admin` / `admin123`)
memakai **Selenium WebDriver + Python + pytest**.

| Syarat tugas | Dipenuhi oleh |
|---|---|
| WebDriver (Python) yang scalable | Page Object Model di folder `pages/`, tes di folder `tests/`, pengaturan di `settings.py` |
| Eksekusi paralel dengan Selenium Grid | `docker-compose.yml` (Hub + Node) dan `pytest -n 3 --grid-url ...` |
| Integrasi CI/CD | `.github/workflows/tests.yml` (GitHub Actions, 2 job) |
| Pelaporan lengkap | Laporan HTML `reports/report.html` + screenshot otomatis saat tes gagal |

## Struktur

```
tugas4_orangehrm/
├── pages/            <- Page Object (BasePage, LoginPage, MainPage, AdminPage, PimPage, BuzzPage)
├── tests/            <- 94 tes stabil sesuai Tugas3_OrangeHRM.side
├── conftest.py       <- membuat browser, login, screenshot saat gagal
├── settings.py       <- URL, username, password, timeout
├── pytest.ini        <- opsi pytest (reruns, laporan HTML)
├── docker-compose.yml
└── .github/workflows/tests.yml
```

## 1. Persiapan (sekali saja)

Yang harus sudah terpasang: **Python 3.10+**, **Google Chrome**, dan (untuk Grid) **Docker Desktop**.

```bash
cd tugas4_orangehrm
python -m venv .venv

# aktifkan venv
source .venv/bin/activate          # Mac / Linux
.venv\Scripts\Activate.ps1         # Windows PowerShell  (kalau ditolak: Set-ExecutionPolicy -Scope Process Bypass)
.venv\Scripts\activate.bat         # Windows CMD

pip install -r requirements.txt
```

Selenium 4 mengunduh ChromeDriver sendiri (Selenium Manager), jadi tidak perlu instal driver manual.

## 2. Coba satu tes dulu (WAJIB sebelum rekam)

```bash
pytest tests/test_login.py::test_login_valid
```

Chrome tampil secara default, jadi kamu akan melihat browser terbuka, login, lalu tertutup
(tambahkan `--headless` kalau ingin browser disembunyikan). Kalau hasilnya hijau (`1 passed`), lanjut.
Kalau error, salin pesan errornya dan kirim ke saya.

## 3. Menjalankan semua tes

```bash
pytest                       # berurutan, 1 browser
pytest -m smoke              # hanya tes cepat
pytest -n 3                  # PARALEL, 3 browser sekaligus (pytest-xdist)
pytest -n 3 --headless       # paralel tanpa jendela
pytest -k login              # hanya tes yang namanya mengandung "login"
```

Setelah selesai buka `reports/report.html` di browser.

## 4. Selenium Grid (Docker)

```bash
docker compose up -d                       # nyalakan Hub + Node Chrome
```
Buka http://localhost:4444/ui/ — tunggu sampai ada 1 Node berstatus UP.

```bash
pytest -n 3 --grid-url http://localhost:4444
```
Di halaman `/ui` kamu bisa melihat sesi berjalan bersamaan (maks. 3).

```bash
docker compose down                        # matikan
```

Tanpa Docker? Alternatif memakai file jar:
`java -jar selenium-server-<versi>.jar standalone --max-sessions 3` lalu pakai `--grid-url http://localhost:4444`.

## 5. CI/CD dengan GitHub Actions

1. Buat repository baru di GitHub.
2. Dari folder proyek:
   ```bash
   git init
   git add .
   git commit -m "Tugas 4 Selenium WebDriver"
   git branch -M main
   git remote add origin https://github.com/<username>/<repo>.git
   git push -u origin main
   ```
3. Buka tab **Actions** di GitHub. Dua job akan berjalan otomatis:
   - **Paralel di Chrome (headless)**
   - **Paralel lewat Selenium Grid**
4. Laporan HTML bisa diunduh dari bagian **Artifacts** pada run tersebut.

## 6. Pelaporan

- `reports/report.html` – ringkasan lulus/gagal, durasi, dan screenshot untuk tes yang gagal.
- `reports/screenshots/` – file PNG screenshot.
- Tes yang gagal diulang otomatis 1x (`--reruns 1`) karena situs demo publik kadang lambat.

## Pemecahan masalah

- **Banyak tes gagal karena timeout** – demo publik sedang lambat atau banyak orang memakainya. Naikkan
  `TIMEOUT` (contoh `TIMEOUT=20 pytest`) atau kurangi paralel (`-n 2`).
- **Teks/menu berbahasa lain** – demo ini kadang berganti bahasa. Locator proyek ini memakai URL/atribut
  supaya tahan, tapi jika ada tes yang gagal karena itu, kirim screenshot-nya ke saya.
- **Docker di Mac M1/M2/M3** – ganti image node di `docker-compose.yml` menjadi `selenium/node-chromium:latest`.
- **`pytest` tidak dikenal** – venv belum aktif; ulangi langkah aktivasi.
- **Data tes** – tes tambah-karyawan membuat lalu menghapus data sendiri, tetapi bila tes berhenti di tengah,
  satu karyawan `Tugas4 Selenium...` mungkin tertinggal di situs demo (aman diabaikan).
