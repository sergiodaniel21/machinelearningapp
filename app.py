import streamlit as st
import pandas as pd
from pypmml import Model

# Cargar el modelo PMML
model = Model.load('heartdesease.pmml')

st.title("Predicción de Enfermedad Cardíaca")

# Crear formularios para la entrada de datos
age = st.number_input('Edad', min_value=0, max_value=100)
sex = st.selectbox('Sexo', ['Masculino', 'Femenino'])
cp = st.selectbox('Tipo de Dolor en el Pecho', [0, 1, 2, 3])
trestbps = st.number_input('Presión Arterial en Reposo', min_value=80, max_value=200)
# ... otros campos relevantes

# Convertir los inputs a un DataFrame para el modelo
data = pd.DataFrame({
    'age': [age],
    'sex': [1 if sex == 'Masculino' else 0],
    'cp': [cp],
    'trestbps': [trestbps],
    # ... otros campos
})

# Hacer la predicción
if st.button('Predecir'):
    prediction = model.predict(data)
    result = prediction['Predicted']
    st.write(f"La predicción es: {'Enfermedad Cardíaca' if result[0] == 1 else 'No Enfermedad Cardíaca'}")