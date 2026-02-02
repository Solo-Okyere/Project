import turtle
import math
import colorsys
import random
import time

# --- Setup and User Input ---
name = "Cherry_McFrimps"
try:
    # A subtle prompt as requested
    start_angle_val = 0
except ValueError:
    start_angle_val = 0

screen = turtle.Screen()
screen.setup(width=900, height=900)
screen.bgcolor("black")
screen.title("A Gift for " + name)
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

# --- Functions ---

def get_corazon(n, size):
    """The mathematical heart equation."""
    x = 16 * math.sin(n) ** 3
    y = (13 * math.cos(n) - 5 * math.cos(2 * n) - 2 * math.cos(3 * n) - math.cos(4 * n))
    return x * size, y * size

def draw_stars():
    star_pen = turtle.Turtle()
    star_pen.hideturtle()
    star_pen.penup()
    star_pen.color("white")
    for _ in range(70):
        star_pen.goto(random.randint(-450, 450), random.randint(-450, 450))
        star_pen.dot(random.randint(1, 2))

def draw_petal():
    """Adds a small floating purple dot to simulate a petal."""
    p = turtle.Turtle()
    p.hideturtle()
    p.penup()
    p.color("#4B0082")
    p.goto(random.randint(-400, 400), random.randint(-400, 400))
    p.dot(random.randint(3, 6))

def animated_type(message, x, y):
    """Types out text with a gentle delay."""
    writer.goto(x, y)
    writer.color("#F4F4FD") # Soft lavender
    for char in message:
        writer.write(char, move=True, align="left", font=("Georgia", 14, "italic"))
        screen.update()
        time.sleep(0.05)

# --- Execution ---

draw_stars()

# 1. THE GROWTH PHASE (Drawing 17 nested hearts like your code)
# We draw them one by one to create the expansion effect.
for i in range(1, 18):
    # Adjust hue based on the layer index (Blue to Purple)
    hue = 0.6 + 0.2 * math.sin(i / 3)
    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
    t.color(r, g, b)
    t.pensize(2)
    
    t.penup()
    # We draw the full circle for each layer
    for n_val in range(0, 630, 10): # 0 to 2*pi roughly
        n_rad = (n_val / 100) + math.radians(start_angle_val)
        x, y = get_corazon(n_rad, i)
        t.goto(x, y)
        if n_val == 0:
            t.pendown()
    
    draw_petal()
    screen.update()
    time.sleep(0.1)

# 2. THE HEARTBEAT & NAME REVEAL
# We pulse the entire nested structure slightly.
for pulse_step in range(40):
    t.clear()
    pulse_factor = 1.0 + (math.sin(pulse_step * 0.2) * 0.05)
    
    for i in range(1, 18):
        hue = 0.6 + 0.2 * math.sin((i + pulse_step) / 5)
        r, g, b = colorsys.hsv_to_rgb(hue, 0.8, 1)
        t.color(r, g, b)
        
        t.penup()
        for n_val in range(0, 630, 15):
            n_rad = (n_val / 100) + math.radians(start_angle_val)
            x, y = get_corazon(n_rad, i * pulse_factor)
            t.goto(x, y)
            if n_val == 0: t.pendown()
            
    # Display her name in the center/bottom
    writer.clear()
    writer.goto(0, -50)
    writer.color("white")
    writer.write(name, align="center", font=("Times New Roman", 32, "bold"))
    
    screen.update()
    time.sleep(0.05)

# 3. THE FINAL MESSAGE (Animated Typing)
time.sleep(1)
writer.clear()

lines = [
    "I didn’t create this to pressure your heart.",
    "I created it to show you how gently I hold it.",
    "If love is a choice, then today I’m choosing you",
    "and I’d be honored if you would accept me in your life.",
    "I can’t love you less."
]

y_pos = 120
for line in lines:
    animated_type(line, -300, y_pos)
    y_pos -= 45
    time.sleep(0.5)

screen.exitonclick()