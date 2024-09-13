from turtle import *
from random import randrange, choice
from freegames import square, vector

# Lista de colores posibles para la serpiente y la comida
colors = ['blue', 'green', 'purple', 'yellow', 'orange']

# Color de la serpiente, elegido aleatoriamente
snake_color = choice(colors)

# Vector que representa la comida y la serpiente
food = vector(0, 0)
snake = [vector(10, 0)]

# Dirección inicial de la serpiente
aim = vector(0, -10)

# Temporizador para mover la comida
food_timer = 0

# Color de la comida, elegido aleatoriamente
food_color = choice(colors)

# Cambiar la dirección de la serpiente.
def change(x, y):
    aim.x = x
    aim.y = y

# Retornar True si la cabeza de la serpiente está dentro de los límites.
def inside(head):
    return -200 < head.x < 190 and -200 < head.y < 190

# Mover la comida en una dirección aleatoria si el temporizador lo permite.
def food_move():
    global food_timer
    food_direction = randrange(0, 4)  # Dirección aleatoria (0: derecha, 1: izquierda, 2: arriba, 3: abajo)
    food_aim = vector(0, 0)  # Inicializar vector para la dirección de la comida
    
    if food_timer == 0:  # Si el temporizador ha llegado a 0, mover la comida
        if food_direction == 0:  # Mover a la derecha
            food_aim.x = 10
        elif food_direction == 1:  # Mover a la izquierda
            food_aim.x = -10
        elif food_direction == 2:  # Mover hacia arriba
            food_aim.y = 10
        else:  # Mover hacia abajo
            food_aim.y = -10
        
        # Comprobar si la nueva posición de la comida está dentro de los límites
        future_food_location = food.copy()
        future_food_location += food_aim
        if inside(future_food_location):
            food.move(food_aim)
        
        # Reiniciar el temporizador
        food_timer = 5
    else:
        food_timer -= 1  # Reducir el temporizador

# Mover la serpiente hacia adelante un segmento.
def move():
    head = snake[-1].copy()  # Copiar la cabeza de la serpiente
    head.move(aim)  # Mover la cabeza en la dirección actual

    # Terminar el juego si la cabeza está fuera de los límites o si toca el cuerpo de la serpiente
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)  # Añadir la nueva posición de la cabeza a la serpiente

    # Si la cabeza de la serpiente llega a la comida, generar nueva comida
    if head == food:
        print('Snake length:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)  # Eliminar la cola de la serpiente si no comió

    clear()  # Limpiar la pantalla para redibujar

    # Dibujar el cuerpo de la serpiente
    for body in snake:
        square(body.x, body.y, 9, snake_color)

    # Mover y dibujar la comida
    food_move()
    square(food.x, food.y, 9, food_color)

    update()  # Actualizar la pantalla
    ontimer(move, 100)  # Llamar a la función de movimiento después de 100ms

# Configuración de la ventana
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()

# Controles para cambiar la dirección de la serpiente
onkey(lambda: change(10, 0), 'Right')  # Mover a la derecha
onkey(lambda: change(-10, 0), 'Left')  # Mover a la izquierda
onkey(lambda: change(0, 10), 'Up')  # Mover hacia arriba
onkey(lambda: change(0, -10), 'Down')  # Mover hacia abajo

# Iniciar el movimiento de la serpiente
move()
done()
