"""Gráfico de líneas con dos series: peticiones web y de la API por día."""
import matplotlib.pyplot as plt
import pandas as pd

peticiones = pd.read_csv("Tema10/datos/peticiones.csv")
peticiones["fecha"] = pd.to_datetime(peticiones["fecha"])

figura, ejes = plt.subplots(figsize=(8, 4))

# cada llamada a plot() agrega una serie; label alimenta la leyenda
ejes.plot(peticiones["fecha"], peticiones["peticiones_web"], label="Web")
ejes.plot(peticiones["fecha"], peticiones["peticiones_api"], label="API")

ejes.set_title("Peticiones por día")
ejes.set_xlabel("Fecha")
ejes.set_ylabel("Peticiones")
ejes.set_ylim(0, 25000)  # el eje vertical empieza en cero
ejes.grid(True)
ejes.legend()

figura.savefig("Tema10/graficos/peticiones_series.png", dpi=150, bbox_inches="tight")
plt.close(figura)
print("Gráfico guardado en Tema10/graficos/peticiones_series.png")
