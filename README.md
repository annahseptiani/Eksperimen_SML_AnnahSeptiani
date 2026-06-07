# Proyek Eksperimen SML, Monitoring, dan Logging - Annah Septiani

## 📋 1. Informasi dan Dokumentasi Dataset
Proyek ini menggunakan dataset klinis untuk memprediksi risiko penyakit jantung pada pasien.

* **Sumber Dataset:** [UCI Heart Disease Dataset / Kaggle Heart Disease Link](https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset) 
* **Deskripsi Dataset:** Dataset ini terdiri dari fitur-fitur medis pasien seperti usia, jenis kelamin, tipe nyeri dada, tekanan darah, kolesterol, hingga hasil elektrokardiografi.
* **Jumlah Data:** Mengandung 303 baris data 
* **Variabel Target:** Kolom `target` (0 = Sehat/Risiko Rendah, 1 = Sakit/Risiko Tinggi).

## ⚙️ 2. Struktur Berkas Preprocessing Data
Seluruh tahap pembersihan dan transformasi data telah diimplementasikan secara sistematis pada folder `preprocessing/`:
* **`preprocessing/Eksperimen_AnnahSeptiani.ipynb`**: Berkas notebook untuk analisis awal dan eksperimen preprocessing secara manual.
* **`preprocessing/automate_AnnahSeptiani.py`**: Berkas script Python untuk melakukan otomasi preprocessing data secara modular.
* **`preprocessing/heart_preprocessed.csv`**: Berkas dataset hasil akhir yang telah bersih dan siap digunakan untuk pelatihan model.
