import turtle
import math
import colorsys
import random
import time

# --- Setup and User Input ---
name = "Cherry_McFrimps"
try:
    start_angle = 0
except ValueError:
    start_angle = 0

screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("A Gift for You")
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

# --- Subtle Background Stars ---
star = turtle.Turtle()
star.hideturtle()
star.penup()
star.color("white")
for _ in range(50):
    star.goto(random.randint(-400, 400), random.randint(-400, 400))
    star.dot(random.randint(1, 3))

# --- Functions ---
def heart_x(t, size):
    return size * 16 * math.sin(t)**3

def heart_y(t, size):
    return size * (13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t))

def draw_petals():
    # Simple logic for a few floating "petals"
    star.color("#4B0082") # Deep purple/indigo
    for _ in range(5):
        star.goto(random.randint(-350, 350), random.randint(-350, 350))
        star.dot(random.randint(4, 8))

def fade_text(message, y_offset, font_size=14):
    writer.goto(0, y_offset)
    writer.color("#8A2BE2") # Blue-Violet
    writer.write(message, align="center", font=("Georgia", font_size, "italic"))
    screen.update()

# --- Main Animation Loop ---
heartbeat_scale = 0
phi = 0  # Phase for heartbeat

for i in range(150):  # Run for a set duration
    t.clear()
    
    # Calculate pulse: smooth transition between 13 and 15 scale
    pulse = 14 + math.sin(phi) * 1.5
    phi += 0.1
    
    # Smooth Color Transition (Blue to Purple)
    # colorsys.hls_to_rgb(hue, lightness, saturation)
    # Blue is ~0.66, Purple is ~0.75
    hue = 0.66 + (math.sin(phi * 0.5) + 1) * 0.05 
    rgb = colorsys.hls_to_rgb(hue, 0.5, 0.8)
    t.color(rgb)
    
    t.penup()
    # Draw heart line
    for angle in range(0, 361):
        # Adjusting for user's starting angle
        rad = math.radians(angle + start_angle)
        x = heart_x(rad, pulse)
        y = heart_y(rad, pulse)
        t.goto(x, y)
        if angle == 0:
            t.pendown()
    
    # Fade in name once heart is established
    if i > 20:
        writer.clear()
        writer.goto(0, -20)
        writer.color(rgb)
        writer.write(name, align="center", font=("Times New Roman", 24, "normal"))
    
    if i % 10 == 0:
        draw_petals()

    screen.update()
    time.sleep(0.05)

# --- Final Message ---
time.sleep(1)
writer.clear()
lines = [
    "I didn’t create this to pressure your heart.",
    "I created it to show you how gently I hold it.",
    "If love is a choice, then today I’m choosing you —",
    "and I’d be honored if one day you choose me to be yours.",
    "I can’t love you less."
]

y_pos = 60
for line in lines:
    fade_text(line, y_pos)
    y_pos -= 35
    time.sleep(1.5)

screen.exitonclick()