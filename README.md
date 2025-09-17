Link: https://raditya-amoret-platformbolapersija.pbp.cs.ui.ac.id
---
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
   ![alt text](https://www.raystec.com/assets/img/rays/pythondjango.png)
   1. `urls.py` → mencocokkan URL dengan fungsi view.
   2. `views.py` → logika utama; ambil data dari model, lalu pilih template.
   3. `models.py` → definisi data & interaksi dengan database.
   4. `Template HTML` → menyajikan data ke user dalam bentuk antarmuka.
      
  ---

  ## Peran `settings.py` dalam proyek Django
  1. Manajemen Aplikasi
  2. Pengaturan Lokasi temolate HTML
  3. Pengaturan file statis (CSS, JS)
  4. Menentukan middleware

---

## Cara migrasi database di Django bekerja
- Ubah model `models.py`
- `py manage.py makemigrations` → menghasilkan file instruksi migrasi
- `py manage.py migrate` → menerapkan ke database
- Django simpan status migrasi di tabel django_migrations agar tidak dobel

---

## Alasan Django digunakan oleh pemula
Django dipilih sebagai materi untuk pemula karena menyediakan lingkungan belajar yang lengkap, terstruktur, aman, dan relevan dengan praktik industri. Framework ini memberi banyak fitur bawaan (ORM, admin panel, autentikasi, keamanan), dokumentasi yang kuat, serta pola arsitektur MVT yang mudah dipahami. Dengan begitu, pemula bisa fokus memahami konsep inti pengembangan web tanpa terbebani oleh detail teknis yang rumit.

---
## Feedback untuk Asdos di tutorial 1
selama menjalani perkuliahan 2 minggu belum ada masalah,  ASDOS sangat baik dalam membantukan mahasiswa yang sedang berkendala saat menjalani tutorial. Semoga kakak tetap semangat mengajari kita

---

## Alasan data delivery diperlukan dalam implentasi sebuah platform
1. Keamanan dan Reliabilitas: data delivery mencakup enkripsi, autentikasi, dan mekanisme retry
2. Ketersidiaan Informasi: agar interaksi berjalan lancar, data yang dibutuhkan setiap pihak harus tersedia tepat waktu karena platfrom dapat meilbatkan baynyak pengguna
3. Konsistensi dan Sinkronisasi: data delivery membantu menjaga konsistensi data antara berbagai modul (misalnya profil pengguna, transaksi, inventori)

---

## Perbandingan XML dan JSON
1. Struktur dan Sintaks
   - XML menggunakan tag <tag>...</tag> yang lebih verbose (panjang).
   - JSON menggunakan pasangan kunci–nilai ("key": "value") yang ringkas dan lebih mudah dibaca.

2. Keterbacaan (Readability)
   - XML lebih mirip dokumen dengan banyak atribut dan nested tags → bagus untuk data dengan struktur kompleks, tapi lebih sulit dipahami cepat.
   - JSON lebih sederhana dan mirip dengan struktur objek di bahasa pemrograman modern (JavaScript, Python, Java).

3. Ukuran Data
   - XML lebih berat karena banyak tag pembuka dan penutup.
   - JSON lebih ringan → ukuran file lebih kecil → lebih cepat dikirim lewat jaringan.

---

## Penjelasan Fungsi is_valid()
- Keamanan data → mencegah input yang tidak sesuai (misalnya SQL injection, email tidak valid, nilai kosong pada field wajib).
- Konsistensi data → memastikan data yang masuk ke database sudah benar sesuai dengan model/aturan bisnis.
- User experience → error yang ditemukan bisa ditampilkan kembali ke pengguna sehingga mereka tahu apa yang salah.

---

## Penjelasan csrf_token
csrf_token adalah Cross-Site Request Forgery token, Token ini di-generate secara otomatis oleh Django untuk mencegah serangan berbahaya, seperti:
- Melindungi form dari serangan CSRF → memastikan request POST benar-benar datang dari user yang sedang login, bukan dari situs berbahaya.
- Memvalidasi keaslian request → saat form dikirim, Django akan memeriksa apakah token yang dikirim user sama dengan token yang disimpan server.
- Menambah lapisan keamanan selain autentikasi dan otorisasi.

Jika csrf_token tidak ada, aplikasi akan rentan terhadap serangan CSRF. Penyerang bisa memaksa pengguna yang sedang login untuk melakukan aksi berbahaya tanpa mereka sadari. Hal ini dapat dimanfaatkan untuk mencuri informasi sensitif, melakukan transaksi keuangan ilegal, mengambil alih akun, mengubah konfigurasi, atau bahkan merusak reputasi pengguna maupun organisasi.

---

## Feedback untuk Asdos di tutorial 2

Menurut saya tidak ada masalah, intstruksi yag diberikan oleh ASDOS dalam tutorial 2 sudah cukup jelas dan dapat diphami

---
## Step by Step Implementasi Checklist tugas 2
1. Skeleton Views / Template Dasar
   - Buat folder `templates` di direktori root proyek.
   - Tambahkan berkas `base.html` di templates/ dengan struktur `template dasar` (header, body, block meta, block content).
   - Di `settings.py`, pada variabel TEMPLATES, tambahkan `BASE_DIR / templates` ke DIRS dan pastikan `APP_DIRS` bernilai `True`.
   - Di `main/templates/main.html`, ubah agar me-extend base.html dan letakkan konten ke dalam `{% block content %}`.






Raditya Amoret - 2406495735 - PBP D
