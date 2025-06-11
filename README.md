# Capstone_Project_LAI25

# Laporan Proyek - LAI25-SM015

## Domain Proyek

Pertanian merupakan sektor vital yang memegang peranan penting dalam menjaga ketahanan pangan dan mendukung perekonomian nasional Indonesia [Ratu Syra Quirinno]. Namun, Salah satu tantangan utama yang dihadapi para petani adalah kesulitan dalam mendeteksi penyakit daun tanaman secara dini karena metode tradisional yang mengandalkan pengamatan visual sering memakan waktu, rentan kesalahan, dan bergantung pada pengalaman individu [Ardi]. Penyakit daun dapat menurunkan hasil panen secara signifikan apabila tidak ditangani dengan cepat dan tepat.

Proyek ini bertujuan untuk mengembangkan sistem deteksi otomatis berbasis teknologi dengan menggunakan algoritma MobileNetV1 yang mampu mengidentifikasi penyakit daun pada lima jenis tanaman utama, yaitu tomat, cabai, kentang, terong, dan labu. Model ini dilatih menggunakan dataset beranotasi gambar daun dan mampu mengenali 31 jenis penyakit daun tanaman, termasuk daun sehat.

Dengan memanfaatkan teknologi deep learning yang di-deploy melalui Streamlit, sistem ini dapat memberikan prediksi instan dari gambar daun yang diunggah. Hal ini memungkinkan petani untuk mengambil tindakan cepat dalam penanganan penyakit dan meminimalkan kerugian panen.

## Business Understanding

Pada bagian ini, kamu perlu menjelaskan proses klarifikasi masalah.

Bagian laporan ini mencakup:

### Problem Statements

Pernyataan masalah latar belakang:
- Proyek ini dimulai dari pengamatan langsung terhadap kondisi di lapangan, di mana masih banyak petani yang belum memahami jenis-jenis penyakit tanaman dan cara mengidentifikasinya dengan bantuan teknologi digital.


### Goals

Tujuan dari proyek ini adalah membangun sistem deteksi penyakit daun tanaman berbasis algoritma MobileNetV1 yang mampu mengklasifikasikan kondisi daun dari gambar secara otomatis. Sistem ini dapat diakses melalui web dengan memanfaatkan framework Streamlit.

Langkah-Langkah Proyek:

1. Pengumpulan dataset dari lima jenis tanaman utama: tomat, cabai, kentang, terong, dan labu.

2. Preprocessing data seperti penggabungan kategori, resize gambar, dan pembagian data ke dalam subset (train, validation, test).

3. Pelatihan model menggunakan arsitektur MobileNetV1 dengan hyperparameter yang disesuaikan.

4. Evaluasi model menggunakan metrik akurasi dan f1-score.

5. Deploy model ke dalam sistem berbasis Streamlit untuk prediksi gambar daun secara langsung oleh pengguna.

## Data Understanding
Dataset terdiri dari tanaman Cabai, Tomat, Terong, Kentang, dan Labu. Masing-masing berisi 300 data pada setiap penyakit tanaman.

Cabai
[Link Dataset Cabai](https://github.com/ulfa03/Chili-Leaf-Disease-Dataset/tree/main)
1. DaunSehat
2. LeafCurl
3. Yellowwiss


Kentang 
[Link Dataset Kentang](https://www.kaggle.com/datasets/nirmalsankalana/potato-leaf-disease-dataset)
1. Bacteria 
2. Fungi 
3. Healthy 
4. Nematode 
5. Pest 
6. Phytopthora 
7. Virus 


Labu 
[Link Datase Labu](https://www.kaggle.com/datasets/tahmidmir/pumpkin-leaf-diseases-dataset-from-bangladesh)
1. Bacterial Leaf Spot
2. Downy Mildew
3. Healthy Leaf
4. Mosaic Disease
5. Powdery Mildew


Tomat
[Link Dataset Tomat](https://www.kaggle.com/datasets/charuchaudhry/plantvillage-tomato-leaf-dataset)
1. Bacterial Spot 
2. Early Blight
3. Late Blight 
4. Leaf Mold 
5. Septoria Leaf Spot 
6. Spider Mites 
7. Target Spot
8. Yellow Leaf Curl Virus 
9. Mosaic Virus 
10. Healthy 


Terong
[Link Dataset Terong 1](https://www.kaggle.com/datasets/kamalmoha/eggplant-disease-recognition-dataset)
[Link Dataset Terong 2](https://www.kaggle.com/datasets/researchforus/eggplant-leaf-disease-dataset)
1. Healthy Leaf Terong
2. Leaf Spot Disease
3. White Mold Disease
4. Insect Pest Disease
5. Mosaic Virus Disease
6. Wilt Disease



## Data Preparation

**Langkah-langkah yang dilakukan :**

* Penggabungan seluruh data penyakit daun ke dalam satu struktur folder.
* Pembagian data ke dalam subset train, validation, dan test untuk tahap pengujian model.

## Modeling

**Model yg diujikan :**

MobileNet 

## Evaluation

**Hasil Evaluasi model :**

**MobileNet** 

Batch size : 32
| Model             | precision |  recall | f1-score |
| ----------------- | --------- | ------- | -------- |
| accuracy          |           |         |   0.82   |
| macro avg         |   0.86    |  0.82   |   0.82   |
| weughted avg      |   0.86    |  0.82   |   0.82   |

**Hasil Deploy**

Untuk mempermudah para petani dan pengguna umum dalam mendeteksi penyakit daun tanaman, kami telah menyediakan aplikasi berbasis web yaitu Streamlit Cloud yang dapat diakses secara gratis melalui internet.
Berikut adalah langkah-langkah penggunaannya:
1. Buka Aplikasi
   Akses aplikasi deteksi melalui tautan berikut:
   
   ```
   https://deteksipenyakittanaman.streamlit.app/
   ```
   (Tautan ini akan diarahkan langsung ke aplikasi deteksi penyakit daun berbasis gambar.)
   
2. Unggah Gambar Daun
   - Klik tombol "Browse files"
   - Pilih gambar daun tanaman dari galeri
     
3. Lihat Hasil Deteksi

   Setelah gambar diunggah:
   - Sistem akan menampilkan jenis penyakit
   - Menampilkan tingkat akurasi prediksi
   - Jika daun sehat, akan muncul keterangan seperti: “Healthy Leaf”
  
5. Peringatan Dini

   Jika terdeteksi gejala penyakit:
   - Sistem akan memberikan peringatan dini
   - Anda bisa mengambil tindakan lebih lanjut seperti menyemprot pestisida atau berkonsultasi dengan penyuluh pertanian
   
Gambar di bawah ini adalah contoh hasil penggunaan sistem tersebut.
![hasil streamlit](https://i.ibb.co/B5zgyNvh/Whats-App-Image-2025-06-11-at-15-07-56-d2f8e7a5.jpg) 


## Conclusion
Proyek ini telah berhasil membangun sistem deteksi otomatis penyakit daun tanaman menggunakan model MobileNetV1, yang terintegrasi dalam antarmuka web melalui framework Streamlit. Sistem ini mampu mengklasifikasikan kondisi daun dari 5 jenis tanaman pertanian utama (tomat, cabai, kentang, terong, dan labu), mencakup hingga 31 jenis penyakit daun termasuk kategori daun sehat.

Model MobileNetV1 dipilih karena keunggulannya, yang mencapai akurasi evaluasi sebesar 82%, dengan precision dan f1-score yang juga tinggi. Sistem kemudian di-deploy secara online dan dapat memberikan hasil prediksi secara real-time dari gambar daun yang diunggah pengguna.

Pengujian dari hasil deploy menunjukkan sistem dapat memberikan hasil prediksi dan tingkat akurasi dari gambar daun, serta notifikasi jika penyakit terdeteksi. Hal ini menunjukkan bahwa sistem memiliki potensi besar untuk membantu petani mendeteksi penyakit tanaman lebih awal, mengambil tindakan pencegahan yang tepat, dan pada akhirnya meningkatkan produktivitas serta ketahanan pangan.

Dengan sistem ini, diharapkan dapat terjadi transformasi digital di sektor pertanian yang memberdayakan petani lokal melalui teknologi cerdas yang mudah diakses dan digunakan.



## Referensi

1. http://jurnal.um-tapsel.ac.id/index.php/nusantara/article/view/16814
2. https://pertanian.uma.ac.id/2025/01/08/penerapan-machine-learning-dalam-mendeteksi-penyakit-tanaman-secara-dini/
