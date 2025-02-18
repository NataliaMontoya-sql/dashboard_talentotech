# Librerías
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from datetime import datetime

# Configuración de la página.
st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

# Headers
st.title("Dashboard")
st.sidebar.title("Sidebar")

# Datos random
np.random.seed(42)
data = pd.DataFrame({
    'Fecha': pd.date_range(start='2024-01-01', periods=100, freq = "D"),
    'Ventas': np.random.randint(100, 1000, size=100),
    'Precio': np.random.uniform(10, 100, size=100),
    'Producto': np.random.choice(['A', 'B', 'C'], size=100),
    'Ciudad': np.random.choice(['Madrid', 'Barcelona', 'Valencia'], size=100),
    'Cliente': np.random.choice(['Cliente1', 'Cliente2', 'Cliente3'], size=100)
})

# SideBar Setting & menu setting with .radio.
st.sidebar.markdown("## Menú")
menu = st.sidebar.radio("", ["Inicio", "Datos", "Visualización", "Configuración"])

# Imprimir datos generados
if menu == "Datos":
    st.subheader("Datos Generados 📎")
    st.dataframe(data)

elif menu == "Visualización":
    #Settle headers
    st.header("Visualización")
    
    # Gráfico de líneas para ventas
    st.subheader("Gráfico de líneas")
    fig, ax = plt.subplots()
    ax.plot(data['Fecha'], data['Ventas'], color='pink')
    st.pyplot(fig)
    
    #Gráfico de barras de precio y producto.
    st.subheader("Gráfico de barras")
    fig, ax = plt.subplots()
    ax.bar(data['Producto'], data['Precio'])
    st.pyplot(fig)
    
    #Filtrar ventas
    
