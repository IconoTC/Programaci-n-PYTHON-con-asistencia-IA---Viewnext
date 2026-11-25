"""Comprueba inventario_ti/graficos.py (paso 5 del proyecto final).

Llama a grafico_clasificacion() con el backend Agg, que dibuja sin abrir
ventanas, y anota la figura en el momento en que se guarda con savefig.
Despues revisa las barras, el titulo y los rotulos de los ejes.
"""
import os
import sys
import tempfile

import matplotlib

matplotlib.use("Agg")
import pandas as pd
from matplotlib.figure import Figure

modulo = os.path.join(os.path.dirname(__file__), "inventario_ti", "graficos.py")
if not os.path.exists(modulo):
    print("ERROR no existe ProyectoFinal/inventario_ti/graficos.py")
    sys.exit()
try:
    from inventario_ti.graficos import grafico_clasificacion
except Exception as error:
    print("ERROR no se puede importar grafico_clasificacion:", error)
    sys.exit()

guardadas = []
guardar_original = Figure.savefig


def guardar_y_anotar(self, nombre, *argumentos, **opciones):
    guardadas.append(self)
    return guardar_original(self, nombre, *argumentos, **opciones)


Figure.savefig = guardar_y_anotar

equipos = pd.DataFrame(
    {"clasificacion": ["NORMAL"] * 4 + ["REVISAR"] * 2 + ["CRITICO"] * 3}
)
imagen = os.path.join(tempfile.mkdtemp(), "clasificacion.png")
try:
    grafico_clasificacion(equipos, imagen)
except Exception as error:
    print("ERROR grafico_clasificacion falla con los equipos de prueba:", error)
    sys.exit()
existe = os.path.exists(imagen) and os.path.getsize(imagen) > 0
estado = "OK" if existe else "ERROR"
print(estado, "debe guardar la imagen en la ruta indicada")
if not guardadas or not guardadas[-1].axes:
    print("ERROR debe guardar con savefig una figura con ejes")
    sys.exit()
ejes = guardadas[-1].axes[0]

with open(modulo, encoding="utf-8") as fichero:
    codigo = fichero.read()
estado = "OK" if "plt.subplots(" in codigo else "ERROR"
print(estado, "debe crear la figura con plt.subplots()")

alturas = sorted(barra.get_height() for barra in ejes.patches)
estado = "OK" if len(alturas) == 3 else "ERROR"
print(estado, "debe haber una barra por cada clasificacion, 3")
estado = "OK" if alturas == [2, 3, 4] else "ERROR"
print(estado, "las alturas de las barras deben ser 4, 2 y 3 equipos")
etiquetas = [marca.get_text() for marca in ejes.get_xticklabels()]
estado = "OK" if {"NORMAL", "REVISAR", "CRITICO"} <= set(etiquetas) else "ERROR"
print(estado, "el eje horizontal debe mostrar NORMAL, REVISAR y CRITICO")
estado = "OK" if "equipos por clasificación" in ejes.get_title().lower() else "ERROR"
print(estado, "el titulo debe ser Equipos por clasificación")
estado = "OK" if "clasificación" in ejes.get_xlabel().lower() else "ERROR"
print(estado, "el rotulo del eje horizontal debe ser Clasificación")
estado = "OK" if "equipos" in ejes.get_ylabel().lower() else "ERROR"
print(estado, "el rotulo del eje vertical debe ser Equipos")
