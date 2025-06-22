import joblib
import numpy as np
import pandas as pd
import streamlit as st
import os

# Path
APP_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(APP_DIR, "model")

FEATURES_ALL = [
    'Curricular_units_2nd_sem_approved',
    'Curricular_units_2nd_sem_grade',
    'Curricular_units_1st_sem_approved',
    'Curricular_units_1st_sem_grade',
    'Tuition_fees_up_to_date',
    'Scholarship_holder',
    'Curricular_units_2nd_sem_enrolled',
    'Curricular_units_1st_sem_enrolled',
    'Admission_grade',
    'Displaced'
]

FEATURES_BINARY = [
    'Displaced',
    'Scholarship_holder',
    'Tuition_fees_up_to_date'
]

def preproccess_data(user_input: dict) -> pd.DataFrame:
    """
    Prepares user input for prediction by converting binary values and applying scalers.

    Args:
        user_input (dict): Raw input data from the user.

    Returns:
        pd.DataFrame: A single-row DataFrame with scaled feature values.
    """
    data_process = user_input.copy()
    
    # Change Feature for Binary to 1 / 0 
    for features in FEATURES_BINARY:
        data_process[features] = 1 if data_process[features] == 'Ya' else 0
    
    # Load Scalers joblib
    try:
        scalers = {
            features: joblib.load(os.path.join(MODEL_DIR, f"scaler_{features}.joblib"))
            for features in FEATURES_ALL
        }
    except FileNotFoundError as e:
        st.error(f"Error: Scaler File not found. Make sure '{e.filename} is inside the model directory ")
        return None
    
    for features in FEATURES_ALL:
        value = np.array(data_process[features]).reshape(1,-1)
        data_process[features] = scalers[features].transform(value)[0, 0]
        
    return pd.DataFrame([data_process])

# Name Web Page
st.set_page_config(page_title="🎓 Prediksi Kinerja Mahasiswa", layout="wide")

# Header Visual
st.markdown("<h1 style='color:#ffA500;'>🎓 Prediksi Kinerja Mahasiswa</h1>", unsafe_allow_html=True)
st.divider()

st.markdown("## 🎯 Data Akademik Mahasiswa")
st.write("Masukkan data Akademik mahasiswa untuk mendapatkan prediksi probabilitas kelulusan.")

col1, col2 = st.columns(2)

# Dict untuk menyimpan nilai input
user_input = {}

with col1:
    user_input['Curricular_units_2nd_sem_approved'] = st.number_input("SKS Lulus (Semester 2)", min_value=0, max_value=30, value=16)
    user_input['Curricular_units_2nd_sem_grade'] = st.number_input("Nilai rata-rata (Semester 2)", min_value=0.0, max_value=20.0, value=13.5, step=0.1)
    user_input['Curricular_units_1st_sem_approved'] = st.number_input("SKS Lulus (Semester 1)", min_value=0, max_value=30, value=18)
    user_input['Curricular_units_1st_sem_grade'] = st.number_input("Nilai rata-rata (Semester 1)", min_value=0.0, max_value=20.0, step=0.1, value=15.0)
    user_input['Tuition_fees_up_to_date'] = st.selectbox("Uang Kuliah Lunas?", ["Ya", "Tidak"])
    
with col2:
    user_input['Scholarship_holder'] = st.selectbox("Penerima Beasiswa?", ["Tidak", "Ya"])
    user_input['Admission_grade'] = st.number_input("Admission Grade ", min_value=0.0, max_value=200.0, step=0.1, value=145.0)
    user_input['Displaced'] = st.selectbox("Mahasiswa Pindahan (Displaced) :", ["Tidak", "Ya"])
    user_input['Curricular_units_2nd_sem_enrolled'] = st.number_input("SKS Diambil (Semester 2)", min_value=0, max_value=30, value=16)
    user_input['Curricular_units_1st_sem_enrolled'] = st.number_input("SKS Diambil (Semester 1)", min_value=0, max_value=30, value=18)
    
st.divider()

if st.button("Prediksi Sekarang", use_container_width=True, type="primary"):
    try:
        model_path = os.path.join(MODEL_DIR, 'rf_model.pkl')
        model = joblib.load(model_path)
        
        processed_df = preproccess_data(user_input)
        
        if processed_df is not None:
            st.subheader("Data setelah preprocessing : ")
            st.dataframe(processed_df)
            
            # Pastikan urutan kolom sesuai training
            processed_df = processed_df[FEATURES_ALL]
            prediction = model.predict_proba(processed_df)[0][1]
            prediction_percentage = prediction * 100
            
            # Display prediction result
            st.subheader("Hasil Prediksi : ")
            if prediction_percentage >= 50:
                st.success(f" Berpeluang lulus dengan probabilitas {prediction_percentage:.2f}%")
            else:
                st.warning(f"Berisiko tidak lulus dengan probabilitas kelulusan hanya {prediction_percentage:.2f}% ")
                
            st.progress(prediction)
            
    except FileNotFoundError:
        st.error(" Model 'rf_model.pkl' tidak ditemukan di dalam folder model")
    except Exception as e:
        st.error(f" Terjadi kesalahan saat prediksi : {e}")