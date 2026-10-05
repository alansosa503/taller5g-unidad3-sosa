# ejercicio1_casa.py
# Tarea práctica - Unidad III
# Composición geométrica utilizando el algoritmo DDA.

from PIL import Image
import math


def dda(pixels, x0, y0, x1, y1, color, ancho, alto):
    """Traza una línea entre (x0, y0) y (x1, y1) usando DDA."""
    dx = x1 - x0
    dy = y1 - y0
    pasos = max(abs(dx), abs(dy))

    # Si ambos puntos coinciden, se pinta un único píxel.
    if pasos == 0:
        if 0 <= x0 < ancho and 0 <= y0 < alto:
            pixels[x0, y0] = color
        return

    incremento_x = dx / pasos
    incremento_y = dy / pasos
    x = float(x0)
    y = float(y0)

    for _ in range(pasos + 1):
        px = round(x)
        py = round(y)
        if 0 <= px < ancho and 0 <= py < alto:
            pixels[px, py] = color
        x += incremento_x
        y += incremento_y


def dibujar_rectangulo(pixels, x0, y0, x1, y1, color, ancho, alto):
    """Dibuja un rectángulo mediante cuatro llamadas a DDA."""
    dda(pixels, x0, y0, x1, y0, color, ancho, alto)
    dda(pixels, x1, y0, x1, y1, color, ancho, alto)
    dda(pixels, x1, y1, x0, y1, color, ancho, alto)
    dda(pixels, x0, y1, x0, y0, color, ancho, alto)


def dibujar_triangulo(pixels, p1, p2, p3, color, ancho, alto):
    """Dibuja un triángulo conectando sus tres vértices con DDA."""
    dda(pixels, p1[0], p1[1], p2[0], p2[1], color, ancho, alto)
    dda(pixels, p2[0], p2[1], p3[0], p3[1], color, ancho, alto)
    dda(pixels, p3[0], p3[1], p1[0], p1[1], color, ancho, alto)


def dibujar_sol(pixels, cx, cy, radio, n_rayos, color, ancho, alto):
    """Representa el sol con rayos que parten de un punto central."""
    for i in range(n_rayos):
        angulo = 2 * math.pi * i / n_rayos
        x1 = cx + int(radio * math.cos(angulo))
        y1 = cy + int(radio * math.sin(angulo))
        dda(pixels, cx, cy, x1, y1, color, ancho, alto)


def dibujar_ventana(pixels, x0, y0, tam, color, ancho, alto):
    """Dibuja una ventana cuadrada y agrega dos divisiones internas."""
    dibujar_rectangulo(pixels, x0, y0, x0 + tam, y0 + tam, color, ancho, alto)
    medio_x = x0 + tam // 2
    medio_y = y0 + tam // 2
    dda(pixels, medio_x, y0, medio_x, y0 + tam, color, ancho, alto)
    dda(pixels, x0, medio_y, x0 + tam, medio_y, color, ancho, alto)


def dibujar_arbol(pixels, x, y_base, color_tronco, color_copa, ancho, alto):
    """Extensión voluntaria: árbol formado por tronco rectangular y copa triangular."""
    dibujar_rectangulo(pixels, x, y_base - 70, x + 25, y_base, color_tronco, ancho, alto)
    dibujar_triangulo(
        pixels,
        (x - 35, y_base - 60),
        (x + 12, y_base - 145),
        (x + 60, y_base - 60),
        color_copa,
        ancho,
        alto,
    )


def dibujar_humo(pixels, x, y, color, ancho, alto):
    """Extensión voluntaria: humo de chimenea mediante líneas cortas."""
    segmentos = [
        ((x, y), (x + 10, y - 12)),
        ((x + 10, y - 12), (x + 2, y - 25)),
        ((x + 2, y - 25), (x + 14, y - 38)),
    ]
    for inicio, fin in segmentos:
        dda(pixels, inicio[0], inicio[1], fin[0], fin[1], color, ancho, alto)


def main():
    ancho, alto = 600, 500

    # Fondo celeste para representar el cielo.
    imagen = Image.new("RGB", (ancho, alto), (200, 230, 255))
    pixels = imagen.load()

    # Paleta de colores: se usan más de cuatro colores diferentes.
    azul = (30, 90, 180)
    rojo = (190, 45, 45)
    marron = (120, 70, 35)
    amarillo = (245, 190, 35)
    verde = (35, 135, 65)
    blanco = (250, 250, 250)
    gris = (105, 105, 105)

    # 1) Cuerpo de la casa.
    dibujar_rectangulo(pixels, 170, 220, 430, 410, azul, ancho, alto)

    # 2) Techo triangular.
    dibujar_triangulo(pixels, (145, 220), (300, 105), (455, 220), rojo, ancho, alto)

    # Chimenea y humo (extensión voluntaria).
    dibujar_rectangulo(pixels, 365, 135, 395, 205, marron, ancho, alto)
    dibujar_humo(pixels, 380, 135, gris, ancho, alto)

    # 3) Puerta rectangular.
    dibujar_rectangulo(pixels, 270, 315, 330, 410, marron, ancho, alto)

    # 4) Dos ventanas cuadradas.
    dibujar_ventana(pixels, 205, 270, 55, blanco, ancho, alto)
    dibujar_ventana(pixels, 340, 270, 55, blanco, ancho, alto)

    # 5) Sol con 12 rayos en la esquina superior izquierda.
    dibujar_sol(pixels, 85, 85, 55, 12, amarillo, ancho, alto)

    # 6) Línea de piso atravesando toda la imagen.
    dda(pixels, 0, 410, ancho - 1, 410, verde, ancho, alto)

    # Árbol como extensión voluntaria.
    dibujar_arbol(pixels, 70, 410, marron, verde, ancho, alto)

    # Detalle simple de picaporte.
    dda(pixels, 318, 363, 322, 363, amarillo, ancho, alto)

    imagen.save("casa.png")
    print("Imagen generada correctamente: casa.png")


if __name__ == "__main__":
    main()
