"""Gráficos de barras: incidencias y minutos de interrupción por servicio."""
import matplotlib.pyplot as plt
import pandas as pd

incidencias = pd.read_csv("Tema10/datos/incidencias.csv")

# número de incidencias por servicio, de mayor a menor
por_servicio = incidencias["servicio"].value_counts()
print(por_servicio)

# barras verticales
figura, ejes = plt.subplots(figsize=(8, 4))
ejes.bar(por_servicio.index, por_servicio.values)
ejes.set_title("Incidencias por servicio")
ejes.set_xlabel("Servicio")
ejes.set_ylabel("Incidencias")
figura.savefig("Tema10/graficos/incidencias_servicio.png", dpi=150,
               bbox_inches="tight")
plt.close(figura)

# minutos de interrupción por servicio, de menor a mayor
minutos = incidencias.groupby("servicio")["minutos_interrupcion"].sum()
minutos = minutos.sort_values()
print(minutos)

# barras horizontales: barh() deja los nombres legibles
figura, ejes = plt.subplots(figsize=(8, 4))
ejes.barh(minutos.index, minutos.values)
ejes.set_title("Minutos de interrupción por servicio")
ejes.set_xlabel("Minutos de interrupción")
figura.savefig("Tema10/graficos/minutos_servicio.png", dpi=150, bbox_inches="tight")
plt.close(figura)
print("Gráficos guardados en Tema10/graficos")
