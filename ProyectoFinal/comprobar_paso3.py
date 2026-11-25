"""Comprueba inventario_ti/modelos.py (paso 3 del proyecto final).

Crea un objeto Equipo, lo convierte en texto y llama a
equipos_criticos() con equipos de prueba.
"""
import os
import sys

import pandas as pd

modulo = os.path.join(os.path.dirname(__file__), "inventario_ti", "modelos.py")
if not os.path.exists(modulo):
    print("ERROR no existe ProyectoFinal/inventario_ti/modelos.py")
    sys.exit()
try:
    from inventario_ti.modelos import Equipo, equipos_criticos
except Exception as error:
    print("ERROR no se pueden importar Equipo y equipos_criticos:", error)
    sys.exit()

try:
    equipo = Equipo("srv-db-02", "postgresql", "CRITICO")
    estado = "OK" if equipo.nombre == "srv-db-02" else "ERROR"
    print(estado, "Equipo guarda el atributo nombre")
    estado = "OK" if equipo.servicio == "postgresql" else "ERROR"
    print(estado, "Equipo guarda el atributo servicio")
    estado = "OK" if equipo.clasificacion == "CRITICO" else "ERROR"
    print(estado, "Equipo guarda el atributo clasificacion")
    texto = str(equipo)
    estado = "OK" if texto == "srv-db-02 (postgresql): CRITICO" else "ERROR"
    print(estado, "str(equipo) debe ser srv-db-02 (postgresql): CRITICO")
except Exception as error:
    print("ERROR no se puede crear un Equipo con tres datos:", error)
    sys.exit()

equipos = pd.DataFrame(
    [
        ("srv-web-01", "nginx", "NORMAL"),
        ("srv-db-02", "postgresql", "CRITICO"),
        ("srv-app-03", "tomcat", "REVISAR"),
        ("srv-mail-02", "postfix", "CRITICO"),
    ],
    columns=["nombre", "servicio", "clasificacion"],
)
try:
    criticos = equipos_criticos(equipos)
except Exception as error:
    print("ERROR equipos_criticos falla con los equipos de prueba:", error)
    sys.exit()
estado = "OK" if isinstance(criticos, list) else "ERROR"
print(estado, "equipos_criticos debe devolver una lista")
estado = "OK" if len(criticos) == 2 else "ERROR"
print(estado, "debe haber 2 equipos criticos, hay", len(criticos))
tipos = all(isinstance(c, Equipo) for c in criticos)
estado = "OK" if criticos and tipos else "ERROR"
print(estado, "los elementos de la lista deben ser objetos Equipo")
nombres = [getattr(c, "nombre", None) for c in criticos]
estado = "OK" if nombres == ["srv-db-02", "srv-mail-02"] else "ERROR"
print(estado, "deben ser srv-db-02 y srv-mail-02, en ese orden")
