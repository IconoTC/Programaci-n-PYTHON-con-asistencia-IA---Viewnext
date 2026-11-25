"""Diagnostico de inventario TI: carga, clasifica, informa y dibuja.

Uso: python ProyectoFinal/main.py [ruta_del_csv]
"""
import sys
from pathlib import Path

from inventario_ti.analisis import clasificar
from inventario_ti.graficos import grafico_clasificacion
from inventario_ti.io_datos import cargar_equipos
from inventario_ti.modelos import equipos_criticos
from inventario_ti.reportes import generar_informe

CSV_POR_DEFECTO = "ProyectoFinal/datos/equipos.csv"
SALIDA = Path("ProyectoFinal/salida")


def main(ruta_csv):
    """Ejecuta el diagnostico completo y devuelve el codigo de salida."""
    equipos = cargar_equipos(ruta_csv)
    if equipos is None:
        print("No se puede continuar sin datos")
        return 1
    equipos = clasificar(equipos)
    SALIDA.mkdir(parents=True, exist_ok=True)
    generar_informe(equipos, SALIDA / "informe.txt")
    grafico_clasificacion(equipos, SALIDA / "clasificacion.png")
    criticos = equipos_criticos(equipos)
    print("Equipos analizados:", len(equipos))
    print("Equipos críticos:", len(criticos))
    for equipo in criticos:
        print(" ", equipo)
    print("Informe y gráfico guardados en", SALIDA)
    return 0


if __name__ == "__main__":
    ruta = sys.argv[1] if len(sys.argv) > 1 else CSV_POR_DEFECTO
    sys.exit(main(ruta))
