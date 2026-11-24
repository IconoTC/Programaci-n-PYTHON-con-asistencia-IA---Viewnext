"""Preparar datos con Pandas y dibujar: incidencias graves por servicio."""
import matplotlib.pyplot as plt
import pandas as pd

incidencias = pd.read_csv("Tema10/datos/incidencias.csv")

# cada condición va entre paréntesis para poder combinarlas con &
servicios = ["Correo", "Copias", "VPN", "Web"]
graves = incidencias[
    (incidencias["gravedad"] == "Alta")
    & (incidencias["servicio"].isin(servicios))
]
print(len(graves), "incidencias graves")

# se cuentan antes de dibujar
por_servicio = graves["servicio"].value_counts()
print(por_servicio)

figura, ejes = plt.subplots(figsize=(8, 4))
ejes.bar(por_servicio.index, por_servicio.values)
ejes.set_title("Incidencias de gravedad Alta por servicio")
ejes.set_xlabel("Servicio")
ejes.set_ylabel("Incidencias")

figura.savefig("Tema10/graficos/graves_servicio.png", dpi=150, bbox_inches="tight")
plt.close(figura)
print("Gráfico guardado en Tema10/graficos/graves_servicio.png")
