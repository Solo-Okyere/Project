import turtle
import math
import colorsys
import time

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
turtle.bgcolor("black")
t.width(2)
turtle.colormode(1.0)

def corazon(n):
    x = 16 * math.sin(n) ** 3
    y = (
        13 * math.cos(n)
        - 5 * math.cos(2 * n)
        - 2 * math.cos(3 * n)
        - math.cos(4 * n)
    )
    return x, y

# ===== GLOWING HEART =====
t.penup()

for i in range(1, 18):
    t.goto(0, 0)
    t.pendown()

    # Smooth blue ↔ purple transition
    hue = 0.6 + 0.2 * math.sin(i / 3)
    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
    t.color(r, g, b)

    for n in range(0, 100, 2):
        x, y = corazon(n / 10)
        t.goto(x * i, y * i)

    t.penup()
    time.sleep(0.05)

turtle.done()


