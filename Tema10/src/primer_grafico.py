"""Primer gráfico del Tema 10: peticiones web por día."""
import matplotlib.pyplot as plt
import pandas as pd

peticiones = pd.read_csv("Tema10/datos/peticiones.csv")
peticiones["fecha"] = pd.to_datetime(peticiones["fecha"])

# la figura es la imagen completa y los ejes son el área donde se dibuja
figura, ejes = plt.subplots(figsize=(8, 4))
ejes.plot(peticiones["fecha"], peticiones["peticiones_web"])
ejes.set_title("Peticiones web por día")
ejes.set_xlabel("Fecha")
ejes.set_ylabel("Peticiones")

figura.savefig("Tema10/graficos/peticiones_web.png")
plt.close(figura)
print("Gráfico guardado en Tema10/graficos/peticiones_web.png")
