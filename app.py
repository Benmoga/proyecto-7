import streamlit as st
import pandas as pd
import plotly.express as px

# Ruta del dataset
df = pd.read_csv('vehicles_us.csv')

# Encabezado de la aplicación
st.header('Análisis Exploratorio de Vehículos')

if st.button('Generar Histograma'):
    fig = px.histogram(df, x='price', title="Distribución de Precios de Vehículos")
    st.write(fig)
    st.plotly_chart(fig, key='histograma')

# Botón para el gráfico de dispersión
if st.button('Generar Gráfico de Dispersión'):
    fig2 = px.scatter(df, x='odometer', y='price', title="Gráfico de Dispersión Odometro Vs Precio")
    st.write(fig2)
    st.plotly_chart(fig2, key='dispersion')

        
    