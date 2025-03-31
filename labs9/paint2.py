import pygame
import sys
import math

# Initialize pygame
pygame.init()

# Define constants for the screen size and colors
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Colors for buttons
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 0, 0)]  # Red, Green, Blue, Black
COLOR_BUTTONS = [(10 + i * 40, 10, 30, 30) for i in range(len(COLORS))]

# Shapes list with added shapes
SHAPES = ["draw", "rect", "circle", "eraser", "line", "square", "right_triangle", "equilateral_triangle", "rhombus"]
SHAPE_BUTTONS = [(200 + (i % 5) * 160, 10 + (i // 5) * 40, 150, 30) for i in range(len(SHAPES))]  # Place buttons in two rows

# Initialize variables
current_color = BLACK
mode = "draw"
start_pos = None
last_pos = None
brush_size = 5

# Set up the screen and canvas
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint in Pygame")

canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill(WHITE)

# Function to draw the UI with color buttons and shape buttons
def draw_ui():
    font = pygame.font.Font(None, 18)  # Smaller font size to fit text in buttons
    max_width = 0  # Track the maximum width needed for the buttons

    # Color buttons (fixed size)
    for i, rect in enumerate(COLOR_BUTTONS):
        pygame.draw.rect(screen, COLORS[i], rect)

    # Shape buttons (dynamic size based on text length)
    for i, rect in enumerate(SHAPE_BUTTONS):
        text = font.render(SHAPES[i], True, (0, 0, 0))
        text_width, text_height = text.get_size()

        # Draw the button with text inside
        pygame.draw.rect(screen, (200, 200, 200), SHAPE_BUTTONS[i])
        
        # Center the text in the button
        text_rect = text.get_rect(center=(SHAPE_BUTTONS[i][0] + SHAPE_BUTTONS[i][2] // 2, SHAPE_BUTTONS[i][1] + SHAPE_BUTTONS[i][3] // 2))
        screen.blit(text, text_rect)

# Function to draw a square
def draw_square(start_pos, size, color):
    pygame.draw.rect(canvas, color, pygame.Rect(start_pos, (size, size)), 2)

# Function to draw a right triangle
def draw_right_triangle(start_pos, base, height, color):
    points = [start_pos, (start_pos[0] + base, start_pos[1]), (start_pos[0], start_pos[1] - height)]
    pygame.draw.polygon(canvas, color, points, 2)

# Function to draw an equilateral triangle
def draw_equilateral_triangle(start_pos, side_length, color):
    height = math.sqrt(3) / 2 * side_length
    points = [
        start_pos,
        (start_pos[0] + side_length, start_pos[1]),
        (start_pos[0] + side_length / 2, start_pos[1] - height)
    ]
    pygame.draw.polygon(canvas, color, points, 2)

# Function to draw a rhombus
def draw_rhombus(start_pos, diagonal1, diagonal2, color):
    half_d1 = diagonal1 / 2
    half_d2 = diagonal2 / 2
    points = [
        (start_pos[0] - half_d1, start_pos[1]),  # Left point
        (start_pos[0], start_pos[1] - half_d2),  # Top point
        (start_pos[0] + half_d1, start_pos[1]),  # Right point
        (start_pos[0], start_pos[1] + half_d2)   # Bottom point
    ]
    pygame.draw.polygon(canvas, color, points, 2)

# Main game loop
running = True
while running:
    screen.fill(WHITE)
    screen.blit(canvas, (0, 0))  # Draw the canvas on the screen
    draw_ui()  # Draw UI buttons

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            for i, rect in enumerate(COLOR_BUTTONS):
                if pygame.Rect(rect).collidepoint(x, y):
                    current_color = COLORS[i]  # Update the current color when a color button is clicked
            for i, rect in enumerate(SHAPE_BUTTONS):
                if pygame.Rect(rect).collidepoint(x, y):
                    mode = SHAPES[i]  # Update the current mode when a shape button is clicked
            start_pos = event.pos
            last_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            end_pos = event.pos
            if mode == "rect":
                pygame.draw.rect(canvas, current_color, pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])), 2)
            elif mode == "circle":
                radius = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5)
                pygame.draw.circle(canvas, current_color, start_pos, radius, 2)
            elif mode == "line":
                pygame.draw.line(canvas, current_color, start_pos, end_pos, brush_size)
            elif mode == "square":
                size = abs(end_pos[0] - start_pos[0])  # Make square from mouse drag
                draw_square(start_pos, size, current_color)
            elif mode == "right_triangle":
                base = abs(end_pos[0] - start_pos[0])
                height = abs(end_pos[1] - start_pos[1])
                draw_right_triangle(start_pos, base, height, current_color)
            elif mode == "equilateral_triangle":
                side_length = abs(end_pos[0] - start_pos[0])
                draw_equilateral_triangle(start_pos, side_length, current_color)
            elif mode == "rhombus":
                diagonal1 = abs(end_pos[0] - start_pos[0])
                diagonal2 = abs(end_pos[1] - start_pos[1])
                draw_rhombus(start_pos, diagonal1, diagonal2, current_color)
        elif event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0]:
            if mode == "draw":
                pygame.draw.line(canvas, current_color, last_pos, event.pos, brush_size)
                pygame.draw.circle(canvas, current_color, event.pos, brush_size // 2)
                last_pos = event.pos
            elif mode == "eraser":
                pygame.draw.line(canvas, WHITE, last_pos, event.pos, 15)
                pygame.draw.circle(canvas, WHITE, event.pos, 14)
                last_pos = event.pos

    pygame.display.flip()  # Update the screen

pygame.quit()
sys.exit()



