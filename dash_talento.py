import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from datetime import datetime

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("Dashboard")
st.sidebar.title("Sidebar")
st.sidebar.markdown("## Menú")
menu = st.sidebar.radio("", ["Inicio", "Datos", "Visualización", "Configuración"])
