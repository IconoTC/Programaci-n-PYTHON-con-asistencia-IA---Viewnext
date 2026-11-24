"""Gráfico de dispersión: tamaño y duración de las copias de seguridad."""
import matplotlib.pyplot as plt
import pandas as pd

copias = pd.read_csv("Tema10/datos/copias.csv")

# se separan las copias por tipo con una máscara booleana
completas = copias[copias["tipo"] == "completa"]
incrementales = copias[copias["tipo"] == "incremental"]
print(len(completas), "completas y", len(incrementales), "incrementales")

figura, ejes = plt.subplots(figsize=(8, 4))
ejes.scatter(completas["tamano_gb"], completas["duracion_minutos"],
             color="#D1495B", marker="s", label="Completa")
ejes.scatter(incrementales["tamano_gb"], incrementales["duracion_minutos"],
             color="#2E86AB", marker="o", label="Incremental")
ejes.set_title("Tamaño y duración de las copias")
ejes.set_xlabel("Tamaño (GB)")
ejes.set_ylabel("Duración (minutos)")
ejes.grid(True)
ejes.legend()

figura.savefig("Tema10/graficos/copias_dispersion.png", dpi=150, bbox_inches="tight")
plt.close(figura)
print("Gráfico guardado en Tema10/graficos/copias_dispersion.png")
