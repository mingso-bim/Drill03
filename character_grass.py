from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
boy = load_image('character.png')

def draw_boy(x, y):
    clear_canvas_now()
    boy.draw_now(x,y)
    delay(0.05)
    
def run_circle():
    print('circle')

    r, cx, cy = 300, 800//2, 600//2
    for degree in range(0, 360, 3):
        theta = math.radians(degree)
        x = r * math.cos(theta) + cx
        y = r * math.sin(theta) + cy
        draw_boy(x, y)

def run_top():
    print('top')
    for x in range(0, 800, 10):
        draw_boy(x, 550)

def run_right():
    print('right')
    for y in range(550, 50, -10):
        draw_boy(790, y)

def run_bottom():
    print('bottom')
    for x in range(790, 10, -10):
        draw_boy(x, 50)

def run_left():
    print('left')
    for y in range(50, 550, 10):
        draw_boy(10, y)

def run_diagonal_up():
    #400, 550
    print('d-up')
    for x in range(0, 400, 10):
        y = 1.375 * x
        draw_boy(x, y)

def run_diagonal_down():
    #790, 50
    print('d-down')
    for x in range(400, 800, 10):
        y = 550 - 1.375 * (x - 400)
        draw_boy(x, y)

def run_rectangle():
    print('rectangle')
    run_top()
    run_right()
    run_bottom()
    run_left()

def run_triangle():
    print('triangle')
    run_bottom()
    run_diagonal_up()
    run_diagonal_down()
    
while True:
    run_circle()
    run_rectangle()
    run_triangle()   

close_canvas()
