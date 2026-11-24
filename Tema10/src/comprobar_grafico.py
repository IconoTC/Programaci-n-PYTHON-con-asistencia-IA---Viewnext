"""Comprueba grafico_caidas.py (Tema 10).

Ejecuta el script con el backend Agg, que dibuja sin abrir ventanas, y
anota la figura en el momento en que el script la guarda con savefig.
Despues revisa esa figura: las barras, sus alturas, el titulo y los
rotulos de los ejes. No compara el aspecto de la imagen.
"""
import os
import runpy
import sys
import traceback

import matplotlib

matplotlib.use("Agg")
import pandas as pd
from matplotlib.figure import Figure

script = os.path.join(os.path.dirname(__file__), "grafico_caidas.py")
imagen = "Tema10/graficos/caidas_largas.png"
if not os.path.exists(script):
    print("ERROR no existe Tema10/src/grafico_caidas.py, hay que crearlo")
    sys.exit()
if os.path.exists(imagen):
    os.remove(imagen)

# cada vez que se llame a savefig se anota la figura y su nombre de fichero
guardadas = []
guardar_original = Figure.savefig


def guardar_y_anotar(self, nombre, *argumentos, **opciones):
    guardadas.append((self, str(nombre).replace("\\", "/")))
    return guardar_original(self, nombre, *argumentos, **opciones)


Figure.savefig = guardar_y_anotar

error = None
try:
    runpy.run_path(script, run_name="__main__")
except (Exception, SystemExit):
    error = traceback.format_exc().strip().splitlines()[-1]
if error:
    print("ERROR el script falla:", error)
else:
    print("OK el script se ejecuta sin errores")

existe = os.path.exists(imagen) and os.path.getsize(imagen) > 0
estado = "OK" if existe else "ERROR"
print(estado, "debe guardar la imagen", imagen)

figuras = [figura for figura, nombre in guardadas if nombre.endswith(imagen)]
if not figuras or not figuras[-1].axes:
    print("ERROR debe guardar con savefig una figura con ejes")
    sys.exit()
ejes = figuras[-1].axes[0]

with open(script, encoding="utf-8") as fichero:
    codigo = fichero.read()
estado = "OK" if "plt.subplots(" in codigo else "ERROR"
print(estado, "debe crear la figura con plt.subplots()")

# filas que cumplen las condiciones, calculadas desde el fichero de datos
incidencias = pd.read_csv("Tema10/datos/incidencias.csv")
caidas = incidencias[
    (incidencias["servicio"].isin(["Correo", "VPN"]))
    & (incidencias["tipo"] == "Caída")
    & (incidencias["minutos_interrupcion"] > 60)
]
alturas = [barra.get_height() for barra in ejes.patches]
estado = "OK" if len(alturas) == len(caidas) else "ERROR"
print(estado, "debe haber una barra por fila,", len(caidas))
esperadas = sorted(caidas["minutos_interrupcion"].tolist())
estado = "OK" if sorted(alturas) == esperadas else "ERROR"
print(estado, "la altura de cada barra es minutos_interrupcion")
etiquetas = [marca.get_text() for marca in ejes.get_xticklabels()]
codigos = caidas["codigo"].tolist()
estado = "OK" if all(c in etiquetas for c in codigos) else "ERROR"
print(estado, "el eje horizontal debe mostrar los codigos")
titulo = ejes.get_title().lower()
estado = "OK" if "caídas de más de 60 minutos" in titulo else "ERROR"
print(estado, "el titulo debe ser Caídas de más de 60 minutos")
estado = "OK" if "código" in ejes.get_xlabel().lower() else "ERROR"
print(estado, "el rotulo del eje horizontal debe ser Código")
estado = "OK" if "minutos de interrupción" in ejes.get_ylabel().lower() else "ERROR"
print(estado, "el rotulo del eje vertical debe ser Minutos de interrupción")
