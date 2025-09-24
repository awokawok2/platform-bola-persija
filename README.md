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
## Step by Step Implementasi Checklist tugas 2
Oke, aku sudah sekalian ubah semua nama file, fungsi, variabel, dan model dari **news → product**. Berikut hasil final checklist-nya:

---

## Step by Step Implementasi Checklist

1. **Skeleton Views / Template Dasar**

   * Buat folder `templates/` di direktori root proyek.
   * Tambahkan berkas `base.html` di `templates/` dengan struktur template dasar (header, body, block meta, block content).
   * Di `settings.py`, pada variabel `TEMPLATES`, tambahkan `BASE_DIR / 'templates'` ke `DIRS` dan pastikan `APP_DIRS` bernilai `True`.
   * Di `main/templates/main.html`, ubah agar me-*extend* `base.html` dan letakkan konten ke dalam `{% block content %}`.

2. **Membuat Form Input dan Tampilkan Data Product**

   * Buat file `forms.py` di app `main`.
   * Definisikan `ProductForm` menggunakan `ModelForm`, set `model = Product` dan `fields = ["title", "content", "category", "thumbnail", "is_featured"]`.
   * Di `views.py`:

     * Tambah fungsi `show_main` yang mengambil semua data `Product` dan kirim ke template `main.html`.
     * Tambah fungsi `create_product` untuk menampilkan form, menerima `POST`, validasi dan menyimpan data, lalu redirect.
     * Tambah fungsi `show_product` untuk detail produk berdasarkan `id` dengan `get_object_or_404` dan menambah view count.
   * Di `urls.py` untuk app `main`:

     * Import `show_main`, `create_product`, `show_product`.
     * Tambahkan path:

       * `'' → show_main`
       * `'create-product/' → create_product`
       * `'product/<str:id>/' → show_product`
   * Update template `main.html` agar menampilkan daftar produk (`product_list`), tombol/link untuk menambah produk, dan menampilkan elemen-elemen produk seperti judul, kategori, tanggal, thumbnail, cuplikan konten, link "Read More".

3. **Buat Template untuk Form Input & Detail Produk**

   * Buat `create_product.html` di `main/templates/`:

     * Extend `base.html`.
     * Tampilkan form dengan method POST, csrf token, dan `form.as_table`.
   * Buat `product_detail.html` di `main/templates/`:

     * Extend `base.html`.
     * Tampilkan tombol kembali ke daftar produk, judul, kategori, status-featured/hot jika ada, tanggal, views, thumbnail jika tersedia, konten lengkap.

4. **Konfigurasi CSRF untuk Deployment**

   * Di `settings.py` root proyek, tambahkan URL deployment kamu ke dalam `CSRF_TRUSTED_ORIGINS` setelah `ALLOWED_HOSTS`, sertakan protokol `https://`.

5. **Run Server & Tes Fungsi Form / Detail**

   * Jalankan `python manage.py runserver`.
   * Buka `http://localhost:8000/` di browser, tes menambahkan produk via halaman form, dan klik "Read More" untuk melihat detail produk. Harusnya data tampil seperti yang diharapkan.

6. **Data Delivery: XML dan JSON**

   * **XML Semua Data**

     * Di `views.py`, import `HttpResponse` dan `serializers`.
     * Buat fungsi `show_xml(request)` yang mengambil semua `Product`, serialisasi ke XML, lalu `return HttpResponse(xml_data, content_type="application/xml")`.
     * Tambahkan route di `urls.py`, misalnya `path('xml/', show_xml, name='show_xml')`.
   * **JSON Semua Data**

     * Buat fungsi `show_json(request)` yang mengambil semua `Product`, serialisasi ke JSON, lalu `return HttpResponse(json_data, content_type="application/json")`.
     * Tambahkan route `path('json/', show_json, name='show_json')`.

7. **Data Berdasarkan ID dalam Format XML/JSON**

   * Tambahkan dua fungsi di `views.py`:

     * `show_xml_by_id(request, product_id)`: ambil data dengan `filter(pk=product_id)`, serialisasi ke XML, handler untuk data tidak ditemukan (status 404).
     * `show_json_by_id(request, product_id)`: ambil dengan `get(pk=product_id)` atau `filter`, serialisasi, dan juga tangani jika `DoesNotExist` → status 404.
   * Tambahkan route di `urls.py`:

     * `path('xml/<str:product_id>/', show_xml_by_id, name='show_xml_by_id')`
     * `path('json/<str:product_id>/', show_json_by_id, name='show_json_by_id')`.

8. **Testing dengan Postman**

   * Pastikan server berjalan.
   * Di Postman, buat request `GET` ke endpoints seperti `/xml/`, `/json/` dan juga `/xml/<product_id>/`, `/json/<product_id>/`.
   * Send request → periksa responsenya apakah format dan data-nya sudah sesuai (XML/JSON).

9. **Penutup & Deploy**

   * Setelah semua selesai, pastikan tampilan situs sesuai yang diharapkan.
   * Struktur direktori lokal dan repositori GitHub diupdate.
   * Commit perubahan, push ke GitHub dan PWS.

---

## Feedback untuk Asdos di tutorial 2

Menurut saya tidak ada masalah, intstruksi yag diberikan oleh ASDOS dalam tutorial 2 sudah cukup jelas dan dapat diphami

Screenshot Postman
1. XML:
   ![Alt text](https://i.ibb.co.com/vvXP72wf/Postman-xml.png)
3. XML by ID:
   ![Alt text]()
5. JSON:
   ![Alt text](https://i.ibb.co.com/W4S9fr9N/image.png)
7. JSON by ID:
   ![Alt text]()

---
## TUGAS 4

## Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.

Django AuthenticationForm adalah form bawaan Django yang digunakan untuk menangani proses autentikasi pengguna. Form ini menyediakan field untuk username dan password, serta melakukan validasi kredensial terhadap database pengguna.

Kelebihan:
- Siap pakai - Tidak perlu membuat form manual dari scratch
- Validasi otomatis - Memeriksa kredensial secara otomatis
- Keamanan terintegrasi - Sudah menerapkan best practices security
- Kustomisasi mudah - Bisa di-extend untuk menambah fungsionalitas
- Terintegrasi dengan User model - Langsung bekerja dengan model User Django

Kekurangan:
- Terbatas secara default - Hanya handle username/password
- Kurang fleksibel - Untuk kebutuhan kompleks butuh kustomisasi
- Tampilan dasar - UI/UX perlu disesuaikan dengan desain aplikasi

---
##  Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
Perbedaan:
- Autentikasi: Proses verifikasi identitas pengguna (siapa Anda?)
- Otorisasi: Proses menentukan hak akses pengguna (apa yang boleh Anda lakukan?)

---

Contoh Autentikasi:
from django.contrib.auth import authenticate, login  

def login_view(request):  
&nbsp;&nbsp;&nbsp;&nbsp; username = request.POST['username']  
&nbsp;&nbsp;&nbsp;&nbsp; password = request.POST['password']  
&nbsp;&nbsp;&nbsp;&nbsp; user = authenticate(request, username=username, password=password)  
&nbsp;&nbsp;&nbsp;&nbsp; if user is not None:  
&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; login(request, user)  # Autentikasi berhasil  

---

Contoh Otoritasi:
from django.contrib.auth.decorators import login_required, permission_required

@login_required
def protected_view(request):  
&nbsp;&nbsp;&nbsp;&nbsp; # Hanya untuk user yang sudah login  
&nbsp;&nbsp;&nbsp;&nbsp; pass  

@permission_required('app.delete_item')  
def delete_view(request):  
&nbsp;&nbsp;&nbsp;&nbsp; # Hanya untuk user dengan permission tertentu  
&nbsp;&nbsp;&nbsp;&nbsp; pass  

---
## Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
Kelebihan Session:
- Aman - Data disimpan di server
- Kapasitas besar - Dapat menyimpan data yang kompleks
- Terkontrol - Server memiliki kendali penuh

Kekurangan Session:
- Beban server - Menyimpan data di memori/database server
- Scalability issues - Bermasalah pada aplikasi terdistribusi

Kelebihan Cookies:
- Ringan untuk server - Data disimpan di client
- Persisten - Dapat bertahan lama
- Client-side storage - Mengurangi beban server

Kekurangan Cookies:
- Size terbatas - Maksimal 4KB per cookie
- Rentan keamanan - Dapat dimodifikasi oleh client
- Privacy concerns - Diatur oleh berbagai regulasi

---
## Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
Risiko Potensial:
- Cross-Site Scripting (XSS) - Pencurian cookie melalui JavaScript
- Cross-Site Request Forgery (CSRF) - Eksploitasi session pengguna
- Man-in-the-Middle - Intercept cookie melalui jaringan tidak aman
- Cookie Theft - Pencurian melalui berbagai vektor

Cara Django menangani:
- Gembok JavaScript (HttpOnly)
- Kode rahasia (CSRF Token)
- Koneksi aman (HTTPS Only)
- Batas waktu (Session Expiry)


Raditya Amoret - 2406495735 - PBP D
