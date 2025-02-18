# Importamos nuestras herramientas mágicas especiales
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import time

# Configuramos nuestra página mágica para que sea grande y bonita
st.set_page_config(
    page_title="Dashboard Educativo Avanzado",
    page_icon="🎓",
    layout="ultrawide",
    initial_sidebar_state="expanded"
)

# Hacemos que todo se vea más bonito con colores suaves y especiales
st.markdown("""
    <style>
    .main {
        background-color: #E8F5E9;
    }
    .css-1d391kg {
        background-color: #f5f5f5;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }
    .stMetric {
        background-color: white;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }
    .sidebar .sidebar-content {
        background-color: #4CAF50;
    }
    </style>
    """, unsafe_allow_html=True)

# Creamos una barra lateral más sofisticada
with st.sidebar:
    st.title("🎯 Panel de Control")
    
    # Agregamos un selector de fecha
    fecha_seleccionada = st.date_input(
        "Selecciona una fecha",
        datetime.now()
    )
    
    # Agregamos un selector de modo
    modo = st.select_slider(
        "Modo de visualización",
        options=["Básico", "Intermedio", "Avanzado"]
    )
    
    # Creamos un filtro de actividades
    actividades_disponibles = ["Todas", "Pintura", "Música", "Matemáticas", "Lectura", "Juegos"]
    actividad_seleccionada = st.multiselect(
        "Filtrar por actividad",
        actividades_disponibles,
        default="Todas"
    )
    
    # Agregamos un medidor de progreso
    progreso_total = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        progreso_total.progress(i + 1)

# Creamos el contenido principal
st.title("🌟 Dashboard Educativo Interactivo")

# Primera fila de métricas
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="✨ Puntos Totales",
        value="784",
        delta="54 nuevos",
        delta_color="normal"
    )

with col2:
    st.metric(
        label="👥 Nuevos Estudiantes",
        value="54",
        delta="+12%",
        delta_color="normal"
    )

with col3:
    st.metric(
        label="📚 Actividades Completadas",
        value="32",
        delta="-2",
        delta_color="inverse"
    )

with col4:
    st.metric(
        label="⭐ Índice de Participación",
        value="86%",
        delta="+5%"
    )

# Creamos una sección para la analítica avanzada
st.subheader("📊 Análisis de Rendimiento")

# Creamos dos columnas para gráficos
graf_col1, graf_col2 = st.columns(2)

with graf_col1:
    # Datos para el gráfico de línea
    datos_tendencia = pd.DataFrame({
        'Fecha': pd.date_range(start='2024-01-01', periods=30),
        'Actividad': np.random.randint(50, 100, 30),
        'Participación': np.random.randint(70, 100, 30)
    })
    
    fig_linea = px.line(
        datos_tendencia,
        x='Fecha',
        y=['Actividad', 'Participación'],
        title='Tendencias de Participación',
        template='plotly_white'
    )
    fig_linea.update_traces(line_width=3)
    st.plotly_chart(fig_linea, use_container_width=True)

with graf_col2:
    # Datos para el gráfico de radar
    categorias = ['Creatividad', 'Colaboración', 'Concentración', 'Comunicación', 'Curiosidad']
    valores = np.random.randint(70, 100, 5)
    
    fig_radar = go.Figure()
    fig_radar.add_trace(go.Scatterpolar(
        r=valores,
        theta=categorias,
        fill='toself',
        name='Habilidades'
    ))
    fig_radar.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )
        ),
        title='Desarrollo de Habilidades'
    )
    st.plotly_chart(fig_radar, use_container_width=True)

# Creamos una sección para los estudiantes del día
st.subheader("👨‍🎨 Estudiantes Destacados del Día")

# Datos de estudiantes más detallados
estudiantes = pd.DataFrame({
    'Nombre': ['Sarah Hudson', 'Dakota Smith', 'John Lane'],
    'Hora': ['10:00 am', '11:15 am', '12:30 pm'],
    'Actividad': ['Pintura Creativa', 'Música Avanzada', 'Matemáticas Divertidas'],
    'Progreso': [95, 88, 92],
    'Estado': ['En clase', 'Próximo', 'Pendiente']
})

# Mostramos los estudiantes en tarjetas interactivas
for i, estudiante in estudiantes.iterrows():
    col_est1, col_est2, col_est3 = st.columns([1, 2, 1])
    
    with col_est1:
        st.image(f"https://api.dicebear.com/7.x/avataaars/svg?seed={i}", width=80)
    
    with col_est2:
        st.markdown(f"### {estudiante['Nombre']}")
        st.write(f"🕒 {estudiante['Hora']} | 📚 {estudiante['Actividad']}")
        progress_bar = st.progress(estudiante['Progreso']/100)
        
    with col_est3:
        if estudiante['Estado'] == 'En clase':
            st.success(estudiante['Estado'])
        elif estudiante['Estado'] == 'Próximo':
            st.warning(estudiante['Estado'])
        else:
            st.info(estudiante['Estado'])
    
    st.divider()

# Agregamos una sección de eventos
st.subheader("📅 Próximos Eventos")

# Creamos datos de eventos
eventos = [
    {"tipo": "Reunión de equipo", "fecha": "Hoy, 3:00 PM", "participantes": 3},
    {"tipo": "Clase de arte", "fecha": "Mañana, 10:00 AM", "participantes": 2},
    {"tipo": "Evaluación mensual", "fecha": "Viernes, 2:00 PM", "participantes": 4}
]

# Mostramos los eventos en una tabla interactiva
tabla_eventos = pd.DataFrame(eventos)
st.table(tabla_eventos.style.highlight_max(axis=0))

# Agregamos un chat de soporte simulado
with st.expander("💬 Chat de Soporte"):
    st.write("Conversación de ejemplo:")
    st.info("👩‍🏫 Profesora: ¡Hola! ¿En qué puedo ayudarte hoy?")
    st.text_input("Escribe tu mensaje aquí...")
