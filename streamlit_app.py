import streamlit as st

import streamlit as st

st.title("Clasificación del Clima - Árbol de Decisión")

# 1. Capturar los valores mediante la interfaz (reemplaza las variables fijas)
temperatura = st.number_input("Temperatura (°C)", value=28)
humedad = st.number_input("Humedad (%)", value=60)
llueve = st.checkbox("¿Llueve?", value=True)

# Botón para ejecutar la clasificación
if st.button("Clasificar Clima"):
    # 2. Lógica de tu árbol de decisión
    if temperatura >= 30:
        if humedad >= 70:
            clasificacion = "Calor húmedo"
        else:
            clasificacion = "Calor seco"
    elif temperatura >= 15:
        if llueve:
            clasificacion = "Templado lluvioso"
        else:
            clasificacion = "Templado"
    else:
        clasificacion = "Frío"

    # 3. Mostrar el resultado en pantalla (reemplaza a print)
    st.write("### Resultado de la clasificación:")
    st.success(clasificacion)
