# ejercicio1_casa.py
from PIL import Image
import math


def dda(pixels, x0, y0, x1, y1, color, ancho, alto):
    dx = x1 - x0
    dy = y1 - y0
    pasos = max(abs(dx), abs(dy))

    if pasos == 0:
        if 0 <= x0 < ancho and 0 <= y0 < alto:
            pixels[x0, y0] = color
        return

    x_incremento = dx / pasos
    y_incremento = dy / pasos

    x = x0
    y = y0

    for _ in range(pasos + 1):
        xi = round(x)
        yi = round(y)
        if 0 <= xi < ancho and 0 <= yi < alto:
            pixels[xi, yi] = color
        x += x_incremento
        y += y_incremento


def dibujar_rectangulo(pixels, x0, y0, x1, y1, color, ancho, alto):
    dda(pixels, x0, y0, x1, y0, color, ancho, alto)
    dda(pixels, x1, y0, x1, y1, color, ancho, alto)
    dda(pixels, x1, y1, x0, y1, color, ancho, alto)
    dda(pixels, x0, y1, x0, y0, color, ancho, alto)


def dibujar_triangulo(pixels, p1, p2, p3, color, ancho, alto):
    dda(pixels, p1[0], p1[1], p2[0], p2[1], color, ancho, alto)
    dda(pixels, p2[0], p2[1], p3[0], p3[1], color, ancho, alto)
    dda(pixels, p3[0], p3[1], p1[0], p1[1], color, ancho, alto)


def dibujar_ventana(pixels, x0, y0, tamano, color, ancho, alto):
    x1 = x0 + tamano
    y1 = y0 + tamano
    dibujar_rectangulo(pixels, x0, y0, x1, y1, color, ancho, alto)
    dda(pixels, x0 + tamano // 2, y0, x0 + tamano // 2, y1, color, ancho, alto)
    dda(pixels, x0, y0 + tamano // 2, x1, y0 + tamano // 2, color, ancho, alto)


def dibujar_sol(pixels, cx, cy, radio, n_rayos, color, ancho, alto):
    for i in range(n_rayos):
        angulo = 2 * math.pi * i / n_rayos
        x1 = cx + int(radio * math.cos(angulo))
        y1 = cy + int(radio * math.sin(angulo))
        dda(pixels, cx, cy, x1, y1, color, ancho, alto)


def dibujar_arbol(pixels, x, suelo_y, color_tronco, color_copa, ancho, alto):
    dibujar_rectangulo(pixels, x, suelo_y - 50, x + 22, suelo_y, color_tronco, ancho, alto)
    dibujar_triangulo(
        pixels,
        (x - 30, suelo_y - 50),
        (x + 11, suelo_y - 120),
        (x + 52, suelo_y - 50),
        color_copa,
        ancho,
        alto,
    )


def dibujar_chimenea_y_humo(pixels, x, y, ancho, alto):
    color_chimenea = (110, 110, 110)
    color_humo = (150, 150, 150)
    dibujar_rectangulo(pixels, x, y, x + 25, y + 60, color_chimenea, ancho, alto)
    dda(pixels, x + 12, y, x + 6, y - 12, color_humo, ancho, alto)
    dda(pixels, x + 6, y - 12, x + 16, y - 24, color_humo, ancho, alto)
    dda(pixels, x + 16, y - 24, x + 10, y - 36, color_humo, ancho, alto)


def main():
    ancho, alto = 600, 500
    imagen = Image.new("RGB", (ancho, alto), (200, 230, 255))
    pixels = imagen.load()

    color_casa = (70, 120, 170)
    color_techo = (170, 80, 80)
    color_puerta = (120, 90, 60)
    color_ventana = (245, 245, 255)
    color_sol = (255, 210, 40)
    color_piso = (70, 150, 80)

    suelo_y = 400

    dibujar_rectangulo(pixels, 220, 240, 440, suelo_y, color_casa, ancho, alto)
    dibujar_triangulo(pixels, (200, 240), (330, 140), (460, 240), color_techo, ancho, alto)
    dibujar_rectangulo(pixels, 300, 330, 350, suelo_y, color_puerta, ancho, alto)
    dibujar_ventana(pixels, 250, 280, 50, color_ventana, ancho, alto)
    dibujar_ventana(pixels, 370, 280, 50, color_ventana, ancho, alto)
    dibujar_sol(pixels, 100, 90, 50, 12, color_sol, ancho, alto)
    dda(pixels, 0, suelo_y, ancho - 1, suelo_y, color_piso, ancho, alto)

    dibujar_arbol(pixels, 90, suelo_y, (130, 90, 50), (70, 160, 80), ancho, alto)
    dibujar_chimenea_y_humo(pixels, 385, 165, ancho, alto)

    imagen.save("casa.png")
    print("Imagen casa.png generada correctamente.")


if __name__ == "__main__":
    main()
