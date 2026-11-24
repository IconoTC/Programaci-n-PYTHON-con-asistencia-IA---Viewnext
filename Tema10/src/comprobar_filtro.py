"""Comprueba filtrar_incidencias.py (Tema 10).

Ejecuta el script, revisa lo que muestra y comprueba que guarda las
filas en Tema10/datos/caidas_largas.csv.
"""
import csv
import os
import re
import subprocess
import sys

script = os.path.join(os.path.dirname(__file__), "filtrar_incidencias.py")
fichero_csv = "Tema10/datos/caidas_largas.csv"
if not os.path.exists(script):
    print("ERROR no existe Tema10/src/filtrar_incidencias.py, hay que crearlo")
    sys.exit()
if os.path.exists(fichero_csv):
    os.remove(fichero_csv)
resultado = subprocess.run(
    [sys.executable, script], capture_output=True, text=True
)
salida = resultado.stdout

# codigos de las incidencias que cumplen las tres condiciones,
# de mayor a menor minutos_interrupcion
esperados = ["I001", "I019", "I030", "I003", "I007"]
for codigo in esperados:
    estado = "OK" if codigo in salida else "ERROR"
    print(estado, "debe aparecer", codigo)

# incidencias que se quedan fuera por no cumplir alguna condicion
descartados = ["I002", "I008", "I021", "I023", "I032"]
sobran = [codigo for codigo in descartados if codigo in salida]
if sobran:
    print("ERROR no debe aparecer", sobran[0])
else:
    print("OK no aparecen incidencias que no cumplen las condiciones")

posiciones = [salida.find(codigo) for codigo in esperados]
ordenadas = -1 not in posiciones and posiciones == sorted(posiciones)
estado = "OK" if ordenadas else "ERROR"
print(estado, "deben salir de mayor a menor minutos_interrupcion")

# lineas que no son filas de la tabla, donde debe aparecer el total
otras = [x for x in salida.splitlines() if not re.search(r"I\d{3}", x)]
total = any(re.search(r"\b5\b", linea) for linea in otras)
estado = "OK" if total else "ERROR"
print(estado, "debe indicar que son 5 filas")

# fichero con las filas filtradas
if not os.path.exists(fichero_csv):
    print("ERROR debe guardar las filas en", fichero_csv)
else:
    with open(fichero_csv, encoding="utf-8", newline="") as fichero:
        lector = csv.DictReader(fichero)
        columnas = lector.fieldnames or []
        filas = list(lector)
    print("OK existe", fichero_csv)
    guardados = [fila.get("codigo") for fila in filas]
    estado = "OK" if guardados == esperados else "ERROR"
    print(estado, "el fichero debe tener las 5 filas ordenadas")
    estado = "OK" if "minutos_interrupcion" in columnas else "ERROR"
    print(estado, "el fichero debe tener la columna minutos_interrupcion")

with open(script, encoding="utf-8") as fichero:
    codigo = fichero.read()
estado = "OK" if "import pandas" in codigo else "ERROR"
print(estado, "debe importar pandas")
atajo = re.search(r"iterrows|\.apply\(|\.query\(", codigo)
estado = "ERROR" if atajo else "OK"
print(estado, "no debe usar iterrows, apply ni query")
estado = "OK" if "Traceback" not in resultado.stderr else "ERROR"
print(estado, "no debe aparecer un traceback")
