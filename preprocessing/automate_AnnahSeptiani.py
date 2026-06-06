# preprocessing/automate_AnnahSeptiani.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def pipeline_preprocessing(input_path, output_path):
    print("=== Memulai Otomatisasi Preprocessing ===")
    
    # 1. Memuat Dataset
    df = pd.read_csv(input_path)
    
    # 2. Pembersihan Data (Drop Duplicates & Missing Values)
    df = df.drop_duplicates()
    df = df.dropna()
    
    # 3. Memisahkan Fitur dan Target (Kolom target Kaggle bernama 'target')
    X = df.drop(columns=['target'])
    y = df['target']
    
    # 4. Split Data (80:20)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    # 5. Standarisasi Fitur
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Gabungkan kembali hasil preprocessing menjadi satu DataFrame untuk disimpan
    X_train_df = pd.DataFrame(X_train_scaled, columns=X.columns)
    X_train_df['target'] = y_train.values
    
    # 6. Menyimpan hasil bersih ke file baru
    X_train_df.to_csv(output_path, index=False)
    print(f"Sukses! Data bersih berhasil disimpan di: {output_path}")
    
    return X_train_scaled, X_test_scaled, y_train, y_test

if __name__ == "__main__":
    import os
    
    # Mendeteksi lokasi folder tempat script ini berada (folder 'preprocessing')
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    
    # Menyusun jalur absolut ke file heart.csv (keluar ke root folder, lalu cari heart.csv)
    INPUT_PATH = os.path.join(BASE_DIR, '..', 'heart.csv')
    
    # Menyusun jalur hasil akhir di dalam folder 'preprocessing'
    OUTPUT_PATH = os.path.join(BASE_DIR, 'heart_preprocessed.csv')
    
    # Menjalankan fungsi dengan jalur absolut yang aman
    pipeline_preprocessing(INPUT_PATH, OUTPUT_PATH)