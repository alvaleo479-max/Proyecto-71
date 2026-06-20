import streamlit as st
import plotly_express as px
import pandas as pd

# 1. Configuración de la página (Debe ser lo primero de Streamlit)
st.set_page_config(page_title="Panel EDA - vehicles-us.csv", layout="wide")

# 2. Definición de funciones y caché
@st.cache_data
def load_data(path):
    return pd.read_csv(path)

DATA_PATH = "vehicles_us.csv"

# 3. Título de la aplicación
st.header("Análisis Exploratorio del Dataset")

# 4. Carga de datos con manejo de errores
try:
    data = load_data(DATA_PATH)
    
    # Mostrar una vista previa de los datos de forma interactiva
    st.subheader("Vista previa de los datos")
    st.dataframe(data.head())
    
except Exception as e:
    st.error(f"Error al cargar el archivo de datos: {e}")
    st.stop()

# 5. Separación de columnas (Ahora 'data' ya existe con seguridad)
num_cols = data.select_dtypes(include="number").columns.tolist()
cat_cols = data.select_dtypes(exclude="number").columns.tolist()

# Validar si hay columnas numéricas para graficar
if not num_cols:
    st.error("No se encontraron columnas numéricas en el dataset. Agrega columnas numéricas para graficar.")
    st.stop()

# --- ESPACIO PARA GRÁFICAS (COMPLETADO) ---

st.markdown("---")
st.subheader("Visualizaciones Interactivas")

# Crear dos columnas en la interfaz para poner controles y gráficos
col1, col2 = st.columns(2)

with col1:
    st.markdown("### Distribución de Variables Numéricas")
    # Selector de columna para el histograma
    selected_num = st.selectbox("Selecciona una variable numérica:", num_cols)
    
    # Generar histograma con Plotly Express
    fig_hist = px.histogram(data, x=selected_num, title=f"Histograma de {selected_num}", template="plotly_dark")
    st.plotly_chart(fig_hist, use_container_width=True)

with col2:
    st.markdown("### Relación entre Variables")
    if len(num_cols) >= 2:
        # Selectores para un gráfico de dispersión
        x_axis = st.selectbox("Eje X (Numérico):", num_cols, index=0)
        y_axis = st.selectbox("Eje Y (Numérico):", num_cols, index=min(1, len(num_cols)-1))
        
        # Selector opcional de color basado en columnas categóricas (si existen)
        color_col = None
        if cat_cols:
            color_col = st.selectbox("Color por (Categoría):", [None] + cat_cols)
        
        # Generar gráfico de dispersión
        fig_scatter = px.scatter(data, x=x_axis, y=y_axis, color=color_col, title=f"{x_axis} vs {y_axis}", template="plotly_dark")
        st.plotly_chart(fig_scatter, use_container_width=True)
    else:
        st.warning("Se necesitan al menos 2 columnas numéricas para mostrar un gráfico de dispersión.")