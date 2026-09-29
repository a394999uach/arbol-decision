import streamlit as st

temperatura = 28
humedad = 60
llueve = True

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

print(clasificacion)
