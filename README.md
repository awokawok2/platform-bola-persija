## Step by Step Implementasi Checklist
1. **Inisialisasi Proyek Django**
   - Membuat virtual environment: `python -m venv env`
   - Mengaktifkan virtual environment: `env\Scripts\activate` 
   - Install Django: `pip install django`
   - Membuat project: `django-admin startproject platform-bola-persija .`
   - Membuat app: `py manage.py main`

2. **Buat Aplikasi main**
   - Tambahkan `main` ke dalam `INSTALLED_APPS` di `settings.py`.

3. **Routing**
   - Menambahkan `path('', include('main.urls'))` di `urls.py` project utama.
   - Membuat file `urls.py` di `main`
  
4. **Menghubungkan Model dengan Template**
   - Membuat file `models.py` di `main`
   - menambahkan atribut di dalam `models.py`

5. **Views**
   - Membuat fungsi `show_main` di `views.py` untuk merender template HTML.

6. **Template**
   - Buat folder `templates/` di dalam `main`.
   - Menambahkan `main.html` yang akan menampilkan konten tersebut di website.

7. **Deployment**
   - Setup repository GitHub.
   - Deploy ke Pacil Web Service
  
  ---

  ## Request Client berbasis Django: urls.py, views.py, models.py, dan berkas HTML.

  ---

  ## Peran `settings.py` dalam proyek Django
  1. Manajemen Aplikasi
  2. Pengaturan Lokasi temolate HTML
  3. Pengaturan file statis (CSS, JS)
  4. Menentukan middleware

---

## Cara mihrasi database di Django bekerja
- Ubah model `models.py`
- `py manage.py makemigrations` → menghasilkan file instruksi migrasi
- `py manage.py migrate` → menerapkan ke database
- Django simpan status migrasi di tabel django_migrations agar tidak dobel

---

## Alasan Django digunakan oleh pemula
Django dipilih sebagai materi untuk pemula karena menyediakan lingkungan belajar yang lengkap, terstruktur, aman, dan relevan dengan praktik industri. Framework ini memberi banyak fitur bawaan (ORM, admin panel, autentikasi, keamanan), dokumentasi yang kuat, serta pola arsitektur MVT yang mudah dipahami. Dengan begitu, pemula bisa fokus memahami konsep inti pengembangan web tanpa terbebani oleh detail teknis yang rumit.

---
## Feedback untuk ASDOS
selama menjalani perkuliahan 2 minggu belum ada masalah,  ASDOS sangat baik dalam membantukan mahasiswa yang sedang berkendala saat menjalani tutorial. Semoga kakak tetap semangat mengajari kita

---

Raditya Amoret - 2406495735 - PBP D
