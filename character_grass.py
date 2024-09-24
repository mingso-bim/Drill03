from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
boy = load_image('character.png')

def draw_boy(x, y):
    clear_canvas_now()
    boy.draw_now(x,y)
    delay(0.1)
    
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
    for x in range(0, 800, 100):
        draw_boy(x, 550)
    pass

def run_right():
    print('right')
    pass

def run_bottom():
    print('bottom')
    pass

def run_left():
    print('left')
    pass

def run_rectangle():
    print('rectangle')
    run_top()
    run_right()
    run_bottom()
    run_left()



    
while True:
    #run_circle()
    run_rectangle()
    break

    

close_canvas()
