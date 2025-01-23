import pickle
import numpy as py
import streamlit as st 

model = pickle.load(open('Penyakit-jantung.sav', 'rb'))

st.title('Prediksi Penyakit Jantung')

col1, col2, col3 = st.columns(3)

with col1: 
    age = st.text_input('Umur')
with col2:
    sex = st.text_input('Jenis Kelamin')
with col3:
    cp = st.text_input('Jenis Nyeri')
with col1:
    trestbps = st.text_input('Tekanan Darah')
with col2:
    chol = st.text_input('Nilai Kolesterol')
with col3:
    fbs = st.text_input('Gula Darah')
with col1:
    restecg = st.text_input('Hasil Elektrokadiografi')
with col2:
    thalach = st.text_input('Detak Jantung Maksimum')
with col3:
    exang = st.text_input('Indukso Angina')
with col1:
    oldpeak = st.text_input('ST Depression')
with col2:
    slope = st.text_input('Slope')
with col3:
    ca = st.text_input('Nilai CA')
with col1:
    thal = st.text_input('Nilai Thal')
    
heart_diagnosis = ''

if st.button('Hasil Prediksi Penyakit Jantung'):
    try:
        age = float(age)
        sex = int(sex)
        cp = int(cp)
        trestbps = float(trestbps)
        chol = float(chol)
        fbs = int(fbs)
        restecg = int(restecg)
        thalach = float(thalach)
        exang = int(exang)
        oldpeak = float(oldpeak)
        slope = int(slope)
        ca = int(ca)
        thal = int(thal)
        
        heart_prediction = model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
    
        if (heart_prediction[0]==1):
            heart_diagnosis = 'Pasien Terkena Penyakit Jantung'
        else:
            heart_diagnosis = 'Pasien Tidak Terkena Penyakit Jantung'    
        st.success(heart_diagnosis)
    except ValueError:
        st.error("Masukkan semua nilai sebagai angka yang valid.")