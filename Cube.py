'''
import time
import turtle
from math import cos, sin, radians

start_time = time.time()
screen = turtle.Screen()
screen.setup(1.0, 1.0)

# 3D points for the cube and digits
points = [
    [-100, -100, 100], [100, -100, 100], [100, 100, 100], [-100, 100, 100],
    [-100, -100, -100], [100, -100, -100], [100, 100, -100], [-100, 100, -100]
]

one = [
    [-80, -80, -100], [-80, -60, -100], [-60, -60, -100], [-60, 60, -100],
    [-70, 50, -100], [-80, 60, -100], [-60, 80, -100], [-40, 80, -100],
    [-40, -60, -100], [-20, -60, -100], [-20, -80, -100], [-80, -80, -100]
]

two = [
    [20, -80, -100], [80, -80, -100], [80, -60, -100], [40, -60, -100],
    [80, 40, -100], [80, 60, -100], [60, 80, -100], [40, 80, -100],
    [20, 60, -100], [20, 40, -100], [40, 40, -100], [40, 60, -100],
    [60, 60, -100], [60, 40, -100], [20, -60, -100], [20, -80, -100]
]


def dot_product_projection(x, y, z, matrix):
    x_prime = matrix[0][0] * x + matrix[0][1] * y + matrix[0][2] * z
    y_prime = matrix[1][0] * x + matrix[1][1] * y + matrix[1][2] * z
    return (x_prime, y_prime)

def dot_product_rotation(x, y, z, matrix):
    x_prime = matrix[0][0] * x + matrix[0][1] * y + matrix[0][2] * z
    y_prime = matrix[1][0] * x + matrix[1][1] * y + matrix[1][2] * z
    z_prime = matrix[2][0] * x + matrix[2][1] * y + matrix[2][2] * z
    return (x_prime, y_prime, z_prime)

def draw_shape(points):
    turtle.penup()
    turtle.goto(points[0][0], points[0][1])
    turtle.pendown()
    for point in points[1:]:
        turtle.goto(point[0], point[1])

# Edge colors and other settings
edge_colors = [
    "red", "green", "blue", "yellow",
    "orange", "purple", "cyan", "magenta", 
    "black", "pink", "lime", "brown"
]

angle = 0

while True:
    screen.tracer(0)
    turtle.pensize(5)
    turtle.hideturtle()

    # Rotation matrices
    z_rotation = [
        [cos(angle), -sin(angle), 0],
        [sin(angle), cos(angle), 0],
        [0, 0, 1]
    ]
    y_rotation = [
        [cos(angle), 0, sin(angle)],
        [0, 1, 0],
        [-sin(angle), 0, cos(angle)]
    ]
    x_rotation = [
        [1, 0, 0],
        [0, cos(angle), -sin(angle)],
        [0, sin(angle), cos(angle)]
    ]

    # Rotate points
    rotated_points, rotated_one, rotated_two = [], [], []

    for (x, y, z) in points:
        x_z, y_z, z_z = dot_product_rotation(x, y, z, z_rotation)
        x_y, y_y, z_y = dot_product_rotation(x_z, y_z, z_z, y_rotation)
        rotated_points.append(dot_product_rotation(x_y, y_y, z_y, x_rotation))
    
    for (x, y, z) in one:
        x_z, y_z, z_z = dot_product_rotation(x, y, z, z_rotation)
        x_y, y_y, z_y = dot_product_rotation(x_z, y_z, z_z, y_rotation)
        rotated_one.append(dot_product_rotation(x_y, y_y, z_y, x_rotation))

    for (x, y, z) in two:
        x_z, y_z, z_z = dot_product_rotation(x, y, z, z_rotation)
        x_y, y_y, z_y = dot_product_rotation(x_z, y_z, z_z, y_rotation)
        rotated_two.append(dot_product_rotation(x_y, y_y, z_y, x_rotation))

    # Projection matrix
    projection_matrix = [
        [1, 0, 0],
        [0, 1, 0]
    ]

    projected_points, projected_one, projected_two = [], [], []

    # Project 3D points to 2D
    for (x, y, z) in rotated_points:
        projected_points.append(dot_product_projection(x, y, z, projection_matrix))

    for (x, y, z) in rotated_one:
        projected_one.append(dot_product_projection(x, y, z, projection_matrix))

    for (x, y, z) in rotated_two:
        projected_two.append(dot_product_projection(x, y, z, projection_matrix))

    # Cube edges
    edges = [
        (0, 1), (1, 2), (2, 3), (3, 0), 
        (4, 5), (5, 6), (6, 7), (7, 4), 
        (0, 4), (1, 5), (2, 6), (3, 7)  
    ]

    # Drawing cube
    turtle.penup()
    for i, (start, end) in enumerate(edges):
        turtle.pencolor(edge_colors[i % len(edge_colors)])
        x1, y1 = projected_points[start]
        x2, y2 = projected_points[end]
        turtle.goto(x1, y1)
        turtle.pendown()
        turtle.goto(x2, y2)
        turtle.penup()

    draw_shape(projected_one)
    draw_shape(projected_two)

    screen.update()
    time.sleep(0.04)
    angle += 0.05

    if time.time() - start_time <= 19.5:
        turtle.clearscreen()
    else:
        break

end_time = time.time()
elapsed_time = end_time - start_time
print(f'Time taken: {elapsed_time:.1f} seconds')
'''
import pyautogui
import random
import string
import time

while True:
    random_text = ''.join(random.choices(string.ascii_letters + '();', k=7))  # Random short "code"
    pyautogui.typewrite(random_text, interval=0.2)  # Type with a small interval
    pyautogui.press('enter') 
    time.sleep(random.uniform(100, 300))  # Wait between 10 and 20 seconds before typing again
