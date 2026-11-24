# Tema 10. Visualización de datos

Ficheros de apoyo del laboratorio del Tema 10.

## Contenido

| Fichero | Descripción |
|---|---|
| `datos/peticiones.csv` | 28 días de peticiones web y de la API: fecha, día de la semana y totales |
| `datos/incidencias.csv` | 40 incidencias: código, fecha, servicio, tipo, gravedad y minutos de interrupción |
| `datos/copias.csv` | 30 copias de seguridad: fecha, servidor, tipo, tamaño y duración |
| `src/primer_grafico.py` | Primer gráfico de líneas guardado en un fichero PNG |
| `src/lineas_series.py` | Dos series con leyenda, límites del eje y cuadrícula |
| `src/barras.py` | Barras verticales y horizontales |
| `src/dispersion.py` | Gráfico de dispersión con dos categorías |
| `src/fechas.py` | Fechas en texto frente a fechas convertidas |
| `src/panel.py` | Dos gráficos en una figura con `subplots(1, 2)` |
| `src/graficos_graves.py` | Filtro con Pandas y gráfico de barras |
| `src/comprobar_filtro.py` | Pruebas de `filtrar_incidencias.py`, que se genera con la IA local |
| `src/comprobar_grafico.py` | Pruebas de `grafico_caidas.py`, que se genera con la IA local |
| `notebooks/10_visualizacion.ipynb` | Mismo código en un notebook |

## Ejecución

Desde la raíz del repositorio y con el entorno virtual activado. Matplotlib se
instala en el primer ejercicio del laboratorio.

```
python Tema10/src/primer_grafico.py
python Tema10/src/lineas_series.py
python Tema10/src/barras.py
python Tema10/src/dispersion.py
python Tema10/src/fechas.py
python Tema10/src/panel.py
python Tema10/src/graficos_graves.py
```

Los scripts leen los datos con rutas `Tema10/datos/...` y guardan las imágenes
en `Tema10/graficos`, por lo que hay que ejecutarlos desde la raíz del
repositorio. El directorio `Tema10/graficos` se crea en el segundo ejercicio
del laboratorio con `mkdir -p`, porque `savefig()` no crea directorios.

Los scripts de comprobación ejecutan el script correspondiente y muestran OK
o ERROR en cada prueba. Antes de crear el script con la IA local muestran
algún ERROR.

```
python Tema10/src/comprobar_filtro.py
python Tema10/src/comprobar_grafico.py
```

Los scripts `filtrar_incidencias.py` y `grafico_caidas.py` no están en el
repositorio. Se generan con la IA local durante el laboratorio y se eliminan
al terminar. El segundo usa el fichero `Tema10/datos/caidas_largas.csv`, que
crea el primero.

El fichero `Tema10/requirements.txt` y las imágenes de `Tema10/graficos` se
generan durante el laboratorio. Los ejercicios propuestos se guardan en
`Tema10/propuestos`.

El notebook se abre en VS Code y se ejecuta con el kernel del entorno
virtual `.venv`.
