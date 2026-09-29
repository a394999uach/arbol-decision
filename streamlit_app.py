import streamlit as st

st.title("Clasificación del Clima - Árbol de Decisión")


temperatura = st.number_input("Temperatura (°C)", value=28)
humedad = st.number_input("Humedad (%)", value=60)
llueve = st.checkbox("¿Llueve?", value=True)


if st.button("Clasificar Clima"):
    
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

    
    st.write("### Resultado de la clasificación:")
    st.success(clasificacion)
