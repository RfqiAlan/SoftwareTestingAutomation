# Panduan Rekam Video Tugas 4

Target durasi: **6–10 menit**. Rekam layar (OBS / Zoom / Xbox Game Bar) dengan suara kamu sendiri.
Unggah ke YouTube (Unlisted boleh), lalu kirim link-nya ke LMS Sikola.

## Sebelum mulai rekam (cek satu per satu)

- [ ] `pytest tests/test_login.py::test_login_valid` sudah hijau
- [ ] `pytest -m smoke` sudah hijau (atau paham kenapa ada yang gagal)
- [ ] Docker Desktop menyala, lalu `docker compose up -d` sudah dicoba dan `http://localhost:4444/ui` menampilkan 1 Node
- [ ] Proyek sudah di-push ke GitHub dan tab **Actions** sudah pernah hijau minimal sekali
- [ ] Tutup notifikasi, tab pribadi, dan file lain yang tidak perlu terlihat
- [ ] Font terminal dan editor cukup besar untuk dibaca di video

## Urutan rekaman + naskah singkat

### 1. Pembukaan (±30 detik)
Tampilkan editor dengan struktur folder.
> "Halo, saya [nama], [NIM], Prodi Sistem Informasi UNHAS. Ini Tugas 4 Selenium WebDriver menggunakan Python dan pytest untuk menguji OrangeHRM demo."

### 2. Struktur proyek (±1 menit)
Buka folder `pages/`, `tests/`, `conftest.py`, `settings.py`.
> "Saya memakai Page Object Model. Setiap halaman punya kelas sendiri di folder pages, tes ada di folder tests. Dengan begini kode mudah dirawat dan dikembangkan."

Buka satu file Page Object (misalnya `login_page.py`) dan satu file tes (`test_login.py`) sebentar.

### 3. Jalankan tes biasa (±1 menit)
```bash
pytest tests/test_login.py
```
Biarkan browser terlihat membuka dan mengisi form.
> "Ini eksekusi biasa, satu browser, berurutan."

### 4. Selenium Grid (±1,5 menit)
```bash
docker compose up -d
```
Buka `http://localhost:4444/ui/` di browser dan tunjukkan Node Chrome.
> "Ini Selenium Grid: satu Hub dan satu Node Chrome yang bisa menjalankan sampai 3 sesi sekaligus."

### 5. Eksekusi paralel lewat Grid (±2 menit)
```bash
pytest -n 3 --grid-url http://localhost:4444
```
Kembali ke halaman `/ui/` dan tunjukkan sesi-sesi yang berjalan bersamaan.
> "Dengan pytest-xdist tiga tes berjalan bersamaan di Grid, sehingga total waktu lebih singkat."

Setelah selesai, matikan Grid:
```bash
docker compose down
```

### 6. Laporan (±1 menit)
Buka `reports/report.html` di browser. Tunjukkan ringkasan lulus/gagal, durasi, dan (jika ada) screenshot tes yang gagal.
> "Laporan HTML dibuat otomatis. Jika tes gagal, screenshot otomatis ditempel ke laporan."

### 7. CI/CD GitHub Actions (±1,5 menit)
Buka repository GitHub → tab **Actions** → run terakhir. Tunjukkan dua job hijau dan bagian Artifacts.
> "Setiap push ke GitHub, workflow ini otomatis menjalankan tes secara paralel di Chrome headless dan lewat Selenium Grid, lalu menyimpan laporan sebagai artifact."

### 8. Penutup (±20 detik)
> "Kesimpulannya, proyek ini memenuhi WebDriver Python yang scalable, eksekusi paralel dengan Selenium Grid, integrasi CI/CD, dan pelaporan lengkap. Terima kasih."

## Tips

- Jika satu-dua tes merah karena demo lambat, itu wajar; jelaskan bahwa situs demo publik dan ada fitur `--reruns`.
  Lebih baik rekam sekali ulang sampai hijau, atau tunjukkan laporan apa adanya sambil dijelaskan.
- Jangan terburu-buru; jeda 1–2 detik setelah setiap perintah supaya hasilnya terbaca.
- Setelah upload, pastikan link YouTube bisa dibuka tanpa login sebelum dikirim ke Sikola.
