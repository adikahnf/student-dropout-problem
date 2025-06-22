# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout.

Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

### Permasalahan Bisnis
1. Mengidentifikasi siswa yang berpotensi melakukan dropout

### Cakupan Proyek
Proyek ini mencakup beberapa tahapan seperti :
1. Pengumpulan dan pembersihan data dari dataset Jaya Jaya Institut
2. Pengembangan model machine learning untuk mendeteksi siswa yang berpotensi melakukan dropout
3. Pembuatan business dashboard untuk memantau perkembangan siswa
4. Pembuatan web untuk menggunakan sistem machine learning

### Persiapan

Sumber data: [Dataset Jaya Jaya Institut][https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance]

Setup environment:

1. Setup Notebook :
- Setup Pip
```
pip install virtualenv
```
- Create a Virtual Environment
```
cd my-project
virtualenv --python C:\Path\To\Python\python.exe venv
```
- Activate The Environment
```
.\venv\Scripts\activate
```
- Install requirements :
```
pip install -r requirements.txt
```

2. Menjalankan Streamlit
```
streamlit run app.py
```

3. Menjalankan Dashboard
- Install Metabase versi 0.46.4
```
docker pull metabase/metabase:v0.46.4
``` 
- Menjalankan container metabase :
```
docker run -p 3000:3000 --name metabase metabase/metabase::v0.46.4
```
- Membuka Metabase menggunakan URL :
```
http://localhost:3000/setup
```
- Login Metabase menggunakan :
```
username: root@mail.com
password: root123
```

## Business Dashboard
Jelaskan tentang business dashboard yang telah dibuat. Jika ada, sertakan juga link untuk mengakses dashboard tersebut.

## Menjalankan Sistem Machine Learning
Jelaskan cara menjalankan protoype sistem machine learning yang telah dibuat. Selain itu, sertakan juga link untuk mengakses prototype tersebut.

```

```

## Conclusion
Jelaskan konklusi dari proyek yang dikerjakan.

### Rekomendasi Action Items
Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.
- action item 1
- action item 2
