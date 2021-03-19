###Codigo de Juego de Tiro Parabolico
###Equipo 2: José Arnoldo Rositas, Sergio Cárdenas, Pablo Yesaki

###Comentario de Prueba

###importando herramientas necesarias
from random import randrange
from turtle import *
from freegames import vector

###Establecer los cuerpos del juego (la bola y su dirección)
ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

###Funcion para Interacción con el juego
def tap(x, y):
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 300) / 25
        speed.y = (y + 300) / 25

###Funcion que se asegura de que la bola este dentro de la pantalla
def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

###Funcion para crear los cuerpos y definir su comportamiento
def draw():
    "Draw ball and targets."
    clear()
    
    ###Definir color y figura del target
    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    ###Definir color y figura del proyectil
    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

###Función para definir el movimiento de los objetos
def move():
    "Move ball and targets."
    
    ###Definir posicion del Target
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    ###Movimiento Horizontal del Target
    for target in targets:
        target.x -= 3
        
          ###Movimiento del proyectil
    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

        
    dupe = targets.copy()
    targets.clear()

    ###Destrucción de target por el proyectil
    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    ### Función para terminar el juego ###
    for target in targets:
        if not inside(target):
    ### Ubicacion que aparece la bola una vez que sale de la pantalla        
           target.x=200


    ### Definir la velocidad del juego ###
    ontimer(move, 30)


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()


