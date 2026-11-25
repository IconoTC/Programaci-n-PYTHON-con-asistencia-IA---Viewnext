"""Comprueba inventario_ti/analisis.py (paso 2 del proyecto final).

Llama a clasificar() con equipos de prueba cuyo resultado se conoce,
incluidos los valores que justo llegan a cada umbral.
"""
import os
import sys

import pandas as pd

modulo = os.path.join(os.path.dirname(__file__), "inventario_ti", "analisis.py")
if not os.path.exists(modulo):
    print("ERROR no existe ProyectoFinal/inventario_ti/analisis.py")
    sys.exit()
try:
    from inventario_ti.analisis import clasificar
except Exception as error:
    print("ERROR no se puede importar clasificar:", error)
    sys.exit()

# estado, cpu, memoria, disco y clasificacion que debe resultar
casos = [
    ("OK", 40, 50, 60, "NORMAL"),
    ("OK", 69, 79, 79, "NORMAL"),
    ("OK", 70, 50, 50, "REVISAR"),
    ("OK", 50, 80, 50, "REVISAR"),
    ("OK", 50, 50, 80, "REVISAR"),
    ("AVISO", 10, 10, 10, "REVISAR"),
    ("OK", 85, 50, 50, "CRITICO"),
    ("OK", 50, 90, 50, "CRITICO"),
    ("OK", 50, 50, 90, "CRITICO"),
    ("ERROR", 10, 10, 10, "CRITICO"),
    ("AVISO", 90, 50, 50, "CRITICO"),
]
equipos = pd.DataFrame(
    casos, columns=["estado", "cpu", "memoria", "disco", "esperado"]
)
try:
    resultado = clasificar(equipos[["estado", "cpu", "memoria", "disco"]])
except Exception as error:
    print("ERROR clasificar falla con los equipos de prueba:", error)
    sys.exit()
if "clasificacion" not in getattr(resultado, "columns", []):
    print("ERROR clasificar debe devolver el DataFrame con la columna clasificacion")
    sys.exit()
print("OK clasificar devuelve la columna clasificacion")

descripciones = [
    "valores por debajo de los umbrales: NORMAL",
    "valores justo por debajo de los umbrales de aviso: NORMAL",
    "cpu 70: REVISAR",
    "memoria 80: REVISAR",
    "disco 80: REVISAR",
    "estado AVISO: REVISAR",
    "cpu 85: CRITICO",
    "memoria 90: CRITICO",
    "disco 90: CRITICO",
    "estado ERROR: CRITICO",
    "estado AVISO con cpu 90: CRITICO",
]
obtenidos = list(resultado["clasificacion"])
for descripcion, esperado, obtenido in zip(
    descripciones, equipos["esperado"], obtenidos
):
    estado = "OK" if obtenido == esperado else "ERROR"
    print(estado, descripcion)
