"""Fechas en el eje horizontal: texto frente a fechas convertidas."""
import matplotlib.pyplot as plt
import pandas as pd

peticiones = pd.read_csv("Tema10/datos/peticiones.csv")
print(peticiones["fecha"].dtype)

# con fechas en texto, Matplotlib dibuja una etiqueta por cada valor
figura, ejes = plt.subplots(figsize=(8, 4))
ejes.plot(peticiones["fecha"], peticiones["peticiones_web"])
ejes.set_title("Fechas como texto")
figura.savefig("Tema10/graficos/fechas_texto.png", dpi=150, bbox_inches="tight")
plt.close(figura)

# con fechas convertidas, elige sola las marcas del eje
peticiones["fecha"] = pd.to_datetime(peticiones["fecha"])
print(peticiones["fecha"].dtype)

figura, ejes = plt.subplots(figsize=(8, 4))
ejes.plot(peticiones["fecha"], peticiones["peticiones_web"])
ejes.set_title("Fechas convertidas")
ejes.tick_params(axis="x", rotation=45)  # etiquetas inclinadas
figura.savefig("Tema10/graficos/fechas_convertidas.png", dpi=150,
               bbox_inches="tight")
plt.close(figura)
print("Gráficos guardados en Tema10/graficos")
