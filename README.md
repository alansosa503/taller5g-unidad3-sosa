# Taller de Programación de 5.ª Generación I — Unidad III

**Universidad:** Universidad Americana  
**Carrera:** Ingeniería Informática — 9.º semestre  
**Alumno:** Alan Gustavo Sosa Britez  
**Docente:** Prof. Mgtr. Alberto F. Giménez Méndez  

## Tarea práctica

**Tema:** Conversión por rastreo — implementación y extensión de los algoritmos DDA y Bresenham.

El repositorio contiene la resolución de los dos ejercicios de la Unidad III. El primer ejercicio construye una composición geométrica de una casa utilizando el algoritmo DDA. El segundo genera rosetas geométricas conectando puntos sobre una circunferencia mediante el algoritmo de Bresenham.

## Archivos principales

- `ejercicio1_casa.py` — composición geométrica usando DDA.
- `ejercicio2_roseta.py` — generador de rosetas usando Bresenham.
- `casa.png` — salida del Ejercicio 1.
- `roseta_12.png` — roseta con N=12.
- `roseta_24.png` — roseta con N=24.
- `roseta_36.png` — roseta con N=36.
- `roseta.png` — copia de la variante N=24 como salida adicional.

## Requisitos

- Python 3
- Pillow

Instalación de Pillow:

```bash
pip install pillow
```

## Ejecución

```bash
python ejercicio1_casa.py
python ejercicio2_roseta.py
```

Los scripts generan automáticamente las imágenes PNG en la misma carpeta.

## Algoritmos utilizados

### DDA
Se utiliza para rasterizar los segmentos que componen la casa: cuerpo, techo, puerta, ventanas, sol, piso y elementos adicionales.

### Bresenham
Se utiliza para unir programáticamente los puntos distribuidos sobre una circunferencia imaginaria y formar las rosetas geométricas.
