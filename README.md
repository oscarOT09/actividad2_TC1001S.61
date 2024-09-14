# Documentación del Juego de la Serpiente con Comida Móvil

Este código implementa un juego sencillo de la serpiente en Python usando la biblioteca `turtle`. El objetivo es mover la serpiente para recolectar comida que se mueve aleatoriamente por la pantalla.

## Descripción del Juego

- **Serpiente**: El jugador controla la dirección de la serpiente usando las flechas del teclado.
- **Comida**: La comida se mueve aleatoriamente en intervalos de tiempo.
- **Objetivo**: Hacer que la serpiente crezca comiendo la comida.
- **Colisión**: El juego termina si la serpiente choca contra los límites del campo o contra sí misma.

## Estructura del Código

### Importación de Módulos

```python
from turtle import *
from random import randrange, choice
from freegames import square, vector
```

- **`turtle`**: Se usa para los gráficos del juego.
- **`random.randrange` y `random.choice`**: Se usan para elegir direcciones y colores aleatorios.
- **`freegames.square`**: Dibuja los segmentos de la serpiente y la comida.
- **`freegames.vector`**: Maneja las posiciones y movimientos de la serpiente y la comida.

### Variables Globales

```python
colors = ['blue', 'green', 'purple', 'yellow', 'orange']
snake_color = choice(colors)
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
food_timer = 0
food_color = choice(colors)
```

- **`colors`**: Lista de colores posibles para la serpiente y la comida.
- **`snake_color`**: Color de la serpiente, elegido aleatoriamente de la lista de colores.
- **`food`**: Posición inicial de la comida.
- **`snake`**: Lista que almacena las posiciones de los segmentos de la serpiente.
- **`aim`**: Dirección actual de la serpiente.
- **`food_timer`**: Temporizador que controla el movimiento de la comida.
- **`food_color`**: Color de la comida, elegido aleatoriamente de la lista de colores.

### Funciones

#### `change(x, y)`

```python
def change(x, y):
    """
    Cambia la dirección de la serpiente.
    """
```

- **Descripción**: Cambia la dirección de la serpiente basándose en las teclas presionadas por el jugador.

#### `inside(head)`

```python
def inside(head):
    """
    Retorna True si la cabeza de la serpiente está dentro de los límites.
    """
```

- **Descripción**: Verifica si la cabeza de la serpiente está dentro del área de juego.

#### `food_move()`

```python
def food_move():
    """
    Mueve la comida en una dirección aleatoria si el temporizador lo permite.
    """
```

- **Descripción**: Mueve la comida en una dirección aleatoria cuando el temporizador alcanza 0. Si la nueva posición está dentro de los límites, la comida se mueve; de lo contrario, se mantiene en su lugar.

#### `move()`

```python
def move():
    """
    Mueve la serpiente hacia adelante un segmento.
    """
```

- **Descripción**: Mueve la serpiente en la dirección actual. Si la serpiente come la comida, esta se reposiciona aleatoriamente, de lo contrario, el último segmento de la serpiente se elimina. La comida también se mueve aleatoriamente si es posible.

### Configuración Inicial

```python
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
```

- **Ventana de juego**: Se configura el tamaño y posición de la ventana.
- **Ocultar la tortuga**: Se oculta el cursor de la tortuga.
- **Desactivar la animación**: Se desactiva la animación de la tortuga para tener control manual de las actualizaciones.
- **Escuchar teclas**: El programa comienza a escuchar las teclas para cambiar la dirección de la serpiente.

### Controles del Juego

```python
onkey(lambda: change(10, 0), 'Right')  # Mover a la derecha
onkey(lambda: change(-10, 0), 'Left')  # Mover a la izquierda
onkey(lambda: change(0, 10), 'Up')  # Mover hacia arriba
onkey(lambda: change(0, -10), 'Down')  # Mover hacia abajo
```

- **Movimiento**: Las flechas del teclado controlan la dirección de la serpiente:
  - Flecha derecha: Mueve la serpiente hacia la derecha.
  - Flecha izquierda: Mueve la serpiente hacia la izquierda.
  - Flecha arriba: Mueve la serpiente hacia arriba.
  - Flecha abajo: Mueve la serpiente hacia abajo.

### Iniciar el Juego

```python
move()
done()
```

- **`move()`**: Inicia el movimiento de la serpiente y la comida.
- **`done()`**: Mantiene la ventana abierta hasta que el usuario decida cerrarla.

---

¡Disfruta del juego mientras controlas la serpiente y recoges la comida!
