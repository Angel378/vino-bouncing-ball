import tkinter as tk

# Window setup
window = tk.Tk()
window.title("FREDMORE VINO - Bouncing Ball")

# Canvas dimensions
WIDTH = 800
HEIGHT = 600
canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT, bg="dark green")  # Start with first color
canvas.pack()

# Ball properties
ball_radius = 100  # Big ball
x = WIDTH // 2
y = HEIGHT // 2
dx = 4
dy = 4

# Background color list
bg_colors = ["dark green", "orange", "gray", "blue", "yellow green", "dark violet"]
current_color_index = 0

# Create black ball
ball = canvas.create_oval(
    x - ball_radius, y - ball_radius,
    x + ball_radius, y + ball_radius,
    fill="black", outline=""
)

# Create name text inside ball
name_text = canvas.create_text(
    x, y,
    text="FREDMORE VINO",
    fill="white",
    font=("Arial", 14, "bold"),
    width=ball_radius * 1.8,
    justify="center"
)

# Function to cycle background color
def change_background_color():
    global current_color_index
    current_color_index = (current_color_index + 1) % len(bg_colors)
    canvas.config(bg=bg_colors[current_color_index])

# Animate the ball
def animate():
    global dx, dy

    # Move ball and text together
    canvas.move(ball, dx, dy)
    canvas.move(name_text, dx, dy)

    # Get current ball position
    left, top, right, bottom = canvas.coords(ball)

    # Check for wall collision
    bounced = False
    if left <= 0 or right >= WIDTH:
        dx = -dx
        bounced = True
    if top <= 0 or bottom >= HEIGHT:
        dy = -dy
        bounced = True

    if bounced:
        change_background_color()

    # Repeat animation
    window.after(20, animate)

# Start animation loop
animate()
window.mainloop()
