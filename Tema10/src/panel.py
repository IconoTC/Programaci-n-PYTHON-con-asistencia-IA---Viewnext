"""Panel con dos gráficos en una misma figura."""
import matplotlib.pyplot as plt
import pandas as pd

peticiones = pd.read_csv("Tema10/datos/peticiones.csv")
peticiones["fecha"] = pd.to_datetime(peticiones["fecha"])
incidencias = pd.read_csv("Tema10/datos/incidencias.csv")
por_tipo = incidencias["tipo"].value_counts()

# subplots(1, 2) crea una fila con dos ejes; ejes es una lista de dos
figura, ejes = plt.subplots(1, 2, figsize=(10, 4))

ejes[0].plot(peticiones["fecha"], peticiones["peticiones_web"])
ejes[0].set_title("Peticiones web por día")
ejes[0].tick_params(axis="x", rotation=45)

ejes[1].bar(por_tipo.index, por_tipo.values)
ejes[1].set_title("Incidencias por tipo")

figura.tight_layout()  # evita que se solapen los textos
figura.savefig("Tema10/graficos/panel.png", dpi=150, bbox_inches="tight")
plt.close(figura)
print("Panel guardado en Tema10/graficos/panel.png")
