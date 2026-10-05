# ejercicio2_roseta.py
from PIL import Image
import math
import colorsys


def bresenham(pixels, x0, y0, x1, y1, color, ancho, alto):
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
    puntos = []
    for i in range(n):
        angulo = 2 * math.pi * i / n
        x = cx + int(radio * math.cos(angulo))
        y = cy + int(radio * math.sin(angulo))
        puntos.append((x, y))
    return puntos


def color_gradiente(i, j, n):
    tono = ((i + j) % n) / n
    r, g, b = colorsys.hsv_to_rgb(tono, 0.8, 0.95)
    return (int(r * 255), int(g * 255), int(b * 255))


def dibujar_roseta(pixels, puntos, ancho, alto):
    n = len(puntos)
    for i in range(n):
        for j in range(i + 1, n):
            color = color_gradiente(i, j, n)
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


def generar_roseta(n, nombre_archivo):
    ancho = alto = 700
    imagen = Image.new("RGB", (ancho, alto), "white")
    pixels = imagen.load()
    puntos = generar_puntos_circulo(350, 350, 300, n)
    dibujar_roseta(pixels, puntos, ancho, alto)
    imagen.save(nombre_archivo)
    print(f"{nombre_archivo} generada correctamente con N={n}.")


def main():
    for n in [12, 24, 36]:
        generar_roseta(n, f"roseta_{n}.png")

    # Salida adicional solicitada en el enunciado base.
    generar_roseta(24, "roseta.png")


if __name__ == "__main__":
    main()
