# Primero, invitamos a nuestros amigos (las libreras) a jugar
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from datetime import datetime

# Le ponemos un nombre bonito a nuestra ventana mágica
st.set_page_config(
    page_title="Mi Tablero Mágico",
    page_icon="🌟",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Hacemos que todo se vea más bonito con colores suaves
st.markdown("""
    <style>
    .main {
        background-color: #E8F5E9;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# Creamos el título de nuestro tablero mágico
st.title("🎨 Mi Tablero Mágico")

# Creamos un menú divertido en el lado izquierdo
st.sidebar.title("🎯 Panel de Control")
menu = st.sidebar.radio("", ["🏠 Inicio", "📊 Estadísticas", "👥 Amiguitos", "⚙️ Ajustes"])

# Creamos datos de ejemplo para nuestros amiguitos
amiguitos = pd.DataFrame({
    'Nombre': ['Sarah Hudson', 'Dakota Smith', 'John Lane'],
    'Hora': ['10:00 am', '11:15 am', '12:30 pm'],
    'Actividad': ['Pintura', 'Música', 'Juegos']
})

# Ahora vamos a mostrar diferentes cosas según lo que elijamos en el menú
if menu == "🏠 Inicio":
    # Creamos tres columnas para mostrar información
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="✨ Puntos Mágicos", value="784", delta="54 nuevos")
    
    with col2:
        st.metric(label="🎨 Actividades", value="32", delta="-2")
    
    with col3:
        st.metric(label="🌟 Progreso", value="86%", delta="8%")
    
    # Creamos una gráfica bonita
    st.subheader("📈 Nuestro Progreso")
    datos_grafica = pd.DataFrame({
        'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'],
        'Puntos': [30, 45, 35, 50, 40]
    })
    fig = px.line(datos_grafica, x='Mes', y='Puntos', 
                  line_shape='spline', 
                  markers=True)
    fig.update_traces(line_color='#4CAF50')
    st.plotly_chart(fig, use_container_width=True)

elif menu == "👥 Amiguitos":
    st.subheader("👧👦 Amiguitos de Hoy")
    for _, amiguito in amiguitos.iterrows():
        col1, col2 = st.columns([1, 3])
        with col1:
            st.image("https://api.dicebear.com/7.x/avataaars/svg", width=50)
        with col2:
            st.write(f"**{amiguito['Nombre']}**")
            st.write(f"🕐 {amiguito['Hora']} - {amiguito['Actividad']}")
        st.divider()

elif menu == "📊 Estadísticas":
    st.subheader("📊 Nuestras Actividades")
    actividades = pd.DataFrame({
        'Actividad': ['Pintura', 'Música', 'Juegos', 'Lectura'],
        'Tiempo': [45, 30, 60, 25]
    })
    fig = px.bar(actividades, x='Actividad', y='Tiempo',
                 color='Tiempo',
                 color_continuous_scale=['lightgreen', 'green'])
    st.plotly_chart(fig, use_container_width=True)
