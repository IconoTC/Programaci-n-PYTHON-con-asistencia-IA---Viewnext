"""Comprueba inventario_ti/reportes.py (paso 4 del proyecto final).

Llama a generar_informe() con equipos de prueba y busca en el fichero
que escribe el total, las clasificaciones y los entornos.
"""
import os
import re
import sys
import tempfile

import pandas as pd

modulo = os.path.join(os.path.dirname(__file__), "inventario_ti", "reportes.py")
if not os.path.exists(modulo):
    print("ERROR no existe ProyectoFinal/inventario_ti/reportes.py")
    sys.exit()
try:
    from inventario_ti.reportes import generar_informe
except Exception as error:
    print("ERROR no se puede importar generar_informe:", error)
    sys.exit()

equipos = pd.DataFrame(
    [
        ("NORMAL", "prod"),
        ("NORMAL", "pre"),
        ("REVISAR", "prod"),
        ("REVISAR", "prod"),
        ("CRITICO", "prod"),
        ("CRITICO", "pre"),
        ("CRITICO", "pre"),
    ],
    columns=["clasificacion", "entorno"],
)
informe = os.path.join(tempfile.mkdtemp(), "informe.txt")
try:
    generar_informe(equipos, informe)
except Exception as error:
    print("ERROR generar_informe falla con los equipos de prueba:", error)
    sys.exit()
if not os.path.exists(informe):
    print("ERROR generar_informe debe escribir el fichero de la ruta")
    sys.exit()
print("OK generar_informe escribe el fichero")
with open(informe, encoding="utf-8") as fichero:
    lineas = fichero.read().splitlines()


def numero_de(etiqueta):
    """Numero que sigue a etiqueta y dos puntos en alguna linea."""
    for linea in lineas:
        m = re.match(r"\s*" + etiqueta + r"\s*:\s*(\d+)", linea, re.I)
        if m:
            return int(m.group(1))
    return None


esperados = [
    ("Total de equipos", 7),
    ("NORMAL", 2),
    ("REVISAR", 2),
    ("CRITICO", 3),
    ("prod", 4),
    ("pre", 3),
]
for etiqueta, cantidad in esperados:
    estado = "OK" if numero_de(etiqueta) == cantidad else "ERROR"
    print(estado, "debe aparecer la linea", "%s: %d" % (etiqueta, cantidad))
