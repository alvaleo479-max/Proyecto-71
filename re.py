import pandas as pd
import plotly_express as px
import streamlit as st
st.header("Cuadro de Mandos: Analisis del Mercado de Vehiculos^")
st.write("Bienvenido/a. Utiliza esta aplicacion para explorar el conjunto de datos de anuncios de venta de coches")
try:
    car_data=pd.read_csv("vehicles_us.csv")
except FileNotFoundError:
    st.error("No se encontro el archivo (vehicles_us.csv). Asegurate de que este en el directorio correcto.")
    st.stop()
st.subheader("Exploracion Mediante Botones")
hist_button=st.button("Construir Histograma (Odometro)")
if hist_button:
       st.write("Creacion de un histograma para la columna odometro:")
       fig_hist=px.histogram(car_data, x="odometer", title="Distribucion de Kilometraje (Odometro)")
       st.plotly_chart(fig_hist, use_container_width=True)
scatter_button=st.button("Construir Grafico de Dispercion (Precio vs Odometro)")
if scatter_button:
    st.write("Creacion de un grafico de dispercion:")
    fig_scatter=px.scatter(car_data, x="odometer", y="price", title="Precio vs Kilometraje")
    st.plotly_chart(fig_scatter, use_container_width=True)
st.subheader("Exploracion Mediante Casillas de Verificacion (Checkbox)")
build_histogram=st.checkbox("Mostrar Histograma de Tipo de Vehiculo...")
if build_histogram:
       st.write("Construyendo Histograma Dependiendo del Tipo de Vehiculo..")
       fig_check_hist=px.histogram(car_data, x="type", title=("Cantidad de Vehiculos por Tipo"))
       st.plotly_chart(fig_check_hist, use_container_width=True)
build_scatter=st.checkbox("Mostrar Dispercion de Año vs Precio")
if build_scatter:
     st.write("Construyendo grafico de dispercion basado en el año del modelo...")
     fig_check_scatter=px.scatter(car_data, x="model_year", y="price", color="condition", title="Precio vs Año del Modelo")
     st.plotly_chart(fig_check_scatter, use_container_width=True)