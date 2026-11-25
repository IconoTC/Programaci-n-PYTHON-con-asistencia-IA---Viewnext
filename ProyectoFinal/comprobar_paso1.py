"""Comprueba inventario_ti/io_datos.py (paso 1 del proyecto final).

Llama a cargar_equipos() con el fichero de datos y con un fichero que no
existe, y revisa el DataFrame que devuelve.
"""
import os
import sys

modulo = os.path.join(os.path.dirname(__file__), "inventario_ti", "io_datos.py")
if not os.path.exists(modulo):
    print("ERROR no existe ProyectoFinal/inventario_ti/io_datos.py")
    sys.exit()
try:
    from inventario_ti.io_datos import cargar_equipos
except Exception as error:
    print("ERROR no se puede importar cargar_equipos:", error)
    sys.exit()

ruta = os.path.join(os.path.dirname(__file__), "datos", "equipos.csv")
try:
    equipos = cargar_equipos(ruta)
except Exception as error:
    print("ERROR cargar_equipos falla con el fichero de datos:", error)
    sys.exit()
if equipos is None or not hasattr(equipos, "shape"):
    print("ERROR cargar_equipos debe devolver un DataFrame")
    sys.exit()
print("OK cargar_equipos devuelve un DataFrame")

estado = "OK" if len(equipos) == 18 else "ERROR"
print(estado, "debe haber 18 filas, hay", len(equipos))
estado = "OK" if equipos.isna().sum().sum() == 0 else "ERROR"
print(estado, "no debe haber valores ausentes")
estado = "OK" if not equipos.duplicated().any() else "ERROR"
print(estado, "no debe haber filas duplicadas")

textos = ["nombre", "servicio", "entorno", "estado"]
try:
    limpios = all(
        (equipos[c] == equipos[c].str.strip()).all() for c in textos
    )
except Exception:
    limpios = False
estado = "OK" if limpios else "ERROR"
print(estado, "no deben quedar espacios sobrantes en las columnas de texto")
try:
    entornos = set(equipos["entorno"])
except Exception:
    entornos = set()
estado = "OK" if entornos == {"prod", "pre"} else "ERROR"
print(estado, "entorno debe estar en minusculas: prod y pre")
try:
    estados = set(equipos["estado"])
except Exception:
    estados = set()
estado = "OK" if estados == {"OK", "AVISO", "ERROR"} else "ERROR"
print(estado, "estado debe estar en mayusculas: OK, AVISO y ERROR")

try:
    resultado = cargar_equipos(ruta + ".no_existe")
    estado = "OK" if resultado is None else "ERROR"
    print(estado, "con un fichero que no existe debe devolver None")
except Exception as error:
    print("ERROR con un fichero que no existe no debe fallar:", error)
