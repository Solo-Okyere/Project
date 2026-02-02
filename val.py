import turtle
import math
import colorsys
import random
import time

# --- Setup and User Input ---
name = "Cherry_McFrimps"
try:
    angle_input = 0
except ValueError:
    angle_input = 0

screen = turtle.Screen()
screen.setup(width=900, height=900)
screen.bgcolor("black")
screen.title("For " + name)
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
writer = turtle.Turtle()
writer.hideturtle()

# --- Subtle Background Stars ---
def draw_stars():
    star = turtle.Turtle()
    star.hideturtle()
    star.speed(0)
    star.penup()
    star.color("white")
    for _ in range(80):
        star.goto(random.randint(-450, 450), random.randint(-450, 450))
        opacity = random.random()
        star.dot(random.randint(1, 3))

# --- Mathematical Equation for a Unique Flared Heart ---
# Using a variation: x = 16sin^3(t), y = 13cos(t) - 5cos(2t) - 2cos(3t) - 0.5cos(4t)
def get_heart_coords(angle_rad, size):
    x = size * (16 * math.sin(angle_rad)**3)
    y = size * (13 * math.cos(angle_rad) - 5 * math.cos(2 * angle_rad) - 2 * math.cos(3 * angle_rad) - math.cos(4 * angle_rad))
    return x, y

def draw_glow_heart(size, hue, start_angle):
    """Draws multiple layers to create a neon/glow effect."""
    base_rgb = colorsys.hls_to_rgb(hue, 0.5, 1.0)
    
    # Draw 10 layers of decreasing thickness for the glow
    for i in range(10, 0, -1):
        # Lightness increases as the line gets thinner
        l_val = 0.5 + (0.05 * (10 - i)) 
        rgb = colorsys.hls_to_rgb(hue, l_val, 1.0)
        t.color(rgb)
        t.pensize(i * 1.5) 
        
        t.penup()
        for i_angle in range(0, 361, 2):
            rad = math.radians(i_angle + start_angle)
            x, y = get_heart_coords(rad, size)
            t.goto(x, y)
            if i_angle == 0: t.pendown()
    t.penup()

def type_message(text, x, y):
    writer.goto(x, y)
    writer.color("#D1C4E9") # Soft lavender-purple
    for char in text:
        writer.write(char, move=True, align="left", font=("Georgia", 15, "italic"))
        screen.update()
        time.sleep(0.04)

# --- Execution ---
draw_stars()

# 1. Growth Phase (Drawing the heart 20 times to reach full size)
for g in range(1, 21):
    t.clear()
    current_size = (g / 20) * 15
    # Transition from Blue (0.6) to Purple (0.8)
    current_hue = 0.6 + (g / 20) * 0.15
    draw_glow_heart(current_size, current_hue, angle_input)
    screen.update()
    time.sleep(0.03)

# 2. Heartbeat Animation
phi = 0
for _ in range(80):
    t.clear()
    # Pulse the size slightly
    pulse = 15 + math.sin(phi) * 1.0
    # Pulse the hue slightly between Blue and Purple
    hue_pulse = 0.7 + math.sin(phi * 0.5) * 0.05
    
    draw_glow_heart(pulse, hue_pulse, angle_input)
    
    # Prominent Name
    writer.clear()
    writer.goto(0, -40)
    name_color = colorsys.hls_to_rgb(hue_pulse, 0.8, 1.0)
    writer.color(name_color)
    writer.write(name, align="center", font=("Garamond", 40, "bold"))
    
    phi += 0.15
    screen.update()
    time.sleep(0.04)

# 3. Final Typed Message
time.sleep(1)
writer.clear()
messages = [
    "I didn’t create this to pressure your heart.",
    "I created it to show you how gently I hold it.",
    "If love is a choice, then today I’m choosing you —",
    "and I’d be honored if you would accept me in your life.",
    "I can’t love you less."
]

y_coord = 120
for line in messages:
    type_message(line, -320, y_coord)
    y_coord -= 45
    time.sleep(0.6)

screen.exitonclick()