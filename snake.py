from turtle import *
from random import randrange, choice
from freegames import square, vector

colors = ['blue', 'green', 'purple', 'yellow', 'orange']
snake_color = choice(colors)

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
food_timer = 0


colors = ['blue', 'green', 'purple', 'yellow', 'orange']        
food_Color = choice(colors)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190



def food_move():
    food_direction = randrange(0,4)
    food_aim = vector(0,0)
    global food_timer
    if food_timer == 0:
        if food_direction == 0:
            food_aim.x = 10
        elif food_direction == 1:
            food_aim.x = -10
        elif food_direction == 2:
            food_aim.y = 10
        else:
            food_aim.y = -10        
        future_food_location = food.copy()
        future_food_location += food_aim
        if inside(future_food_location):
            food.move(food_aim)
        
        food_timer=5       
    else:
        food_timer-=1


def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, snake_color)

    food_move()
    square(food.x, food.y, 9, food_Color)
    update()
    ontimer(move, 100)

    

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
