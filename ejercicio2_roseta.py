# ejercicio2_roseta.py
# Tarea práctica - Unidad III
# Generador de rosetas geométricas utilizando el algoritmo de Bresenham.

from PIL import Image
import colorsys
import math
import shutil


def bresenham(pixels, x0, y0, x1, y1, color, ancho, alto):
    """Traza una línea entre dos puntos usando Bresenham para cualquier octante."""
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    error = dx - dy

    while True:
        if 0 <= x0 < ancho and 0 <= y0 < alto:
            pixels[x0, y0] = color

        if x0 == x1 and y0 == y1:
            break

        e2 = 2 * error
        if e2 > -dy:
            error -= dy
            x0 += sx
        if e2 < dx:
            error += dx
            y0 += sy


def generar_puntos_circulo(cx, cy, radio, n):
    """Devuelve n puntos equiespaciados sobre una circunferencia imaginaria."""
    puntos = []
    for i in range(n):
        angulo = 2 * math.pi * i / n
        x = cx + int(radio * math.cos(angulo))
        y = cy + int(radio * math.sin(angulo))
        puntos.append((x, y))
    return puntos


def color_gradiente(p1, p2, cx, cy):
    """Calcula un color RGB según el ángulo del punto medio de cada segmento."""
    mx = (p1[0] + p2[0]) / 2
    my = (p1[1] + p2[1]) / 2
    angulo = math.atan2(my - cy, mx - cx)

    # Normalización del ángulo al intervalo 0..1 para usarlo como matiz HSV.
    tono = (angulo + math.pi) / (2 * math.pi)
    r, g, b = colorsys.hsv_to_rgb(tono, 0.85, 1.0)
    return int(r * 255), int(g * 255), int(b * 255)


def dibujar_roseta(pixels, puntos, ancho, alto):
    """Conecta cada par de puntos y aplica un gradiente visible a las líneas."""
    n = len(puntos)
    cx = ancho // 2
    cy = alto // 2

    for i in range(n):
        for j in range(i + 1, n):
            color = color_gradiente(puntos[i], puntos[j], cx, cy)
            bresenham(
                pixels,
                puntos[i][0],
                puntos[i][1],
                puntos[j][0],
                puntos[j][1],
                color,
                ancho,
                alto,
            )


def generar_roseta(n):
    """Genera una variante de 700x700 píxeles para el valor de N indicado."""
    ancho = alto = 700
    imagen = Image.new("RGB", (ancho, alto), (0, 0, 0))
    pixels = imagen.load()
    puntos = generar_puntos_circulo(350, 350, 300, n)
    dibujar_roseta(pixels, puntos, ancho, alto)

    nombre = f"roseta_{n}.png"
    imagen.save(nombre)
    print(f"Imagen generada correctamente: {nombre} ({n * (n - 1) // 2} líneas)")
    return nombre


def main():
    # Tres variantes requeridas por la consigna.
    for n in (12, 24, 36):
        generar_roseta(n)

    # Alias adicional solicitado en el requisito técnico: roseta.png.
    shutil.copyfile("roseta_24.png", "roseta.png")
    print("También se generó roseta.png como copia de la variante N=24.")


if __name__ == "__main__":
    main()
