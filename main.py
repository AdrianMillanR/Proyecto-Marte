import turtle
import random
import time


class agente():
    bandera = False
    indicador = -1
    fin_de_llevar = False
    indicador2 = 0

    def __init__(self, objeto, estado):
        self.objeto = objeto
        self.estado = estado

    def establecer_recurso(self, recurso_a_llevar):
        self.recurso_a_llevar = recurso_a_llevar

    def llevar_recurso(self, zonas_conocidas):
        global unidades_nave
        # si estamos en el lugar donde encontramos el recurso y ya no hay recurso, reseteamos variables e indicamos que termiamos de llevar el recurso
        if (self.recurso_a_llevar.unidades < 1 and self.indicador == -1):
            self.estado = "explorando"
            self.bandera = False
            self.fin_de_llevar = True
        # si el indicador indica que estamos donde encontramos el recurso, le restamos unidades al recurso y activamos la bandera false
        if (self.indicador == -1):
            self.recurso_a_llevar.unidades -= 1
            self.bandera = False
        # si estamos al principio ponemos bandera en "true"
        if (self.indicador == -((len(zonas_conocidas)))):
            unidades_nave += 1
            self.bandera = True
        # si las unidades del recurso llegan a 0 lo borramos y lo eliminamos
        if (self.recurso_a_llevar.unidades == 0 and self.indicador == -1):
            self.recurso_a_llevar.objeto.color("black")
            for i in recursos:
                if (i.objeto == self.recurso_a_llevar.objeto):
                    recursos.remove(i)
        # si bandera es false estamos en el camino de vuelta asi que se le resta al indicador para la siguiente iteración
        if (self.bandera == False):
            self.indicador -= 1
        # si bandera es true estamos en el camino de ida asi que se le suma al indicador para la siguiente iteración
        if (self.bandera == True):
            self.indicador += 1
        # nos movemos a la coordenada siguiente de nuestro arreglo, definida por la variable "indicador"
        if (self.fin_de_llevar == False):
            x = zonas_conocidas[self.indicador].coordenadax
            y = zonas_conocidas[self.indicador].coordenaday
            self.objeto.setx(x)
            self.objeto.sety(y)
        if (self.fin_de_llevar == True):
            self.fin_de_llevar = False
            self.indicador = -1
        time.sleep(0.5)

    def volver_a_la_nave(self, zonas_conocidas):
        if (self.indicador2 > 0):
            self.indicador2 -= 1
            x = zonas_conocidas[self.indicador2].coordenadax
            y = zonas_conocidas[self.indicador2].coordenaday
            self.objeto.setx(x)
            self.objeto.sety(y)
            time.sleep(0.5)
        else:
            self.estado = "en la nave"


# listas para registrar coordenadas que los robots han recorrido, de los obstaculos y de los recursos
zonas_conocidas1 = []
zonas_conocidas2 = []
zonas_conocidas3 = []
zonas_conocidas4 = []
zonas_conocidas_general = []
obstaculos = []
recursos = []
unidades_nave = 0
# inicializamos compoenntes
planeta = turtle.Screen()
nave = turtle.Turtle()
robot1 = turtle.Turtle()
robot1.speed(0)
robot1.shape("square")
robot1.color("white")
robot1.penup()
robot1.goto(-200, 200)
robot1.pendown()
r1 = agente(robot1, "explorando")
robot2 = turtle.Turtle()
robot2.speed(0)
robot2.shape("square")
robot2.color("orange")
robot2.penup()
robot2.goto(-200, 200)
robot2.pendown()
r2 = agente(robot2, "explorando")
robot3 = turtle.Turtle()
robot3.speed(0)
robot3.shape("square")
robot3.color("green")
robot3.penup()
robot3.goto(-200, 200)
robot3.pendown()
r3 = agente(robot3, "explorando")
robot4 = turtle.Turtle()
robot4.speed(0)
robot4.shape("square")
robot4.color("yellow")
robot4.penup()
robot4.goto(-200, 200)
robot4.pendown()
r4 = agente(robot4, "explorando")


class obstaculo():
    def __init__(self, coordenadax, coordenaday):
        self.coordenadax = coordenadax
        self.coordenaday = coordenaday


class recurso():
    def __init__(self, objeto, unidades):
        self.objeto = objeto
        self.unidades = unidades


class Zonas():
    def __init__(self, coordenadax, coordenaday):
        self.coordenadax = coordenadax
        self.coordenaday = coordenaday


def iniciar_componentes():
    planeta.bgcolor("black")
    planeta.setup(width=420, height=420)
    nave.shape("square")
    nave.color("blue")
    nave.penup()
    nave.goto(-200, 200)
    nave.pendown()
    crearrecurso("recurso1", 2, 0, 0)
    crearrecurso("recurso2", 3, -100, 0)
    crearrecurso("recurso3", 4, 180, 20)
    crearrecurso("recurso4", 1, 20, -60)
    crearrecurso("recurso5", 5, -0, 120)
    crearrecurso("recurso6", 5, 0, 40)
    crearrecurso("recurso7", 4, 0, -180)
    crearrecurso("recurso8", 3, 120, -20)
    crearrecurso("recurso9", 3, -180, -180)
    crearrecurso("recurso10", 1, 180, -180)
    crearrecurso("recurso11", 3, 180, 180)
    crearrecurso("recurso12", 2, -160, -100)
    crearrecurso("recurso12", 3, -180, 40)
    crearrecurso("recurso13", 1, 180, -40)
    crearrecurso("recurso14", 4, 40, 180)

    crearobstaculo("obstaculo1", -100, 100)
    crearobstaculo("obstaculo2", -100, 80)
    crearobstaculo("obstaculo3", -100, 60)
    crearobstaculo("obstaculo4", -100, 40)
    crearobstaculo("obstaculo5", -100, 20)
    crearobstaculo("obstaculo6", -80, 120)
    crearobstaculo("obstaculo7", -60, 120)
    crearobstaculo("obstaculo8", -40, 20)
    crearobstaculo("obstaculo9", -40, 40)
    crearobstaculo("obstaculo10", -40, 60)
    crearobstaculo("obstaculo11", -40, 80)
    crearobstaculo("obstaculo12", -40, 100)
    crearobstaculo("obstaculo13", -100, 120)
    crearobstaculo("obstaculo14", -40, 120)

    crearobstaculo("obstaculo15", 100, 0)
    crearobstaculo("obstaculo16", 100, 20)
    crearobstaculo("obstaculo17", 100, 40)
    crearobstaculo("obstaculo18", 100, 60)
    crearobstaculo("obstaculo19", 100, 80)
    crearobstaculo("obstaculo20", 100, 100)

    crearobstaculo("obstaculo21", -60, -100)
    crearobstaculo("obstaculo22", -40, -100)
    crearobstaculo("obstaculo23", -20, -100)
    crearobstaculo("obstaculo24", 0, -100)
    crearobstaculo("obstaculo25", 20, -100)
    crearobstaculo("obstaculo26", 40, -100)
    crearobstaculo("obstaculo27", 60, -100)
    crearobstaculo("obstaculo28", 80, -100)
    crearobstaculo("obstaculo29", 100, -100)
    crearobstaculo("obstaculo30", 120, -100)

    crearobstaculo("obstaculo31", -180, -40)
    crearobstaculo("obstaculo31", -180, -60)
    crearobstaculo("obstaculo31", -160, -40)

    turtle.title('Exploración en Marte')


def crearobstaculo(nombreobstaculo, x, y):
    nombreobstaculo = turtle.Turtle()
    nombreobstaculo.shape("square")
    nombreobstaculo.color("gray")
    nombreobstaculo.penup()
    nombreobstaculo.goto(x, y)
    o = obstaculo(nombreobstaculo.xcor(), nombreobstaculo.ycor())
    obstaculos.append(o)


def crearrecurso(nombrerecurso, unidades, x, y):
    nombrerecurso = turtle.Turtle()
    nombrerecurso.shape("circle")
    nombrerecurso.color("red")
    nombrerecurso.penup()
    nombrerecurso.goto(x, y)
    r = recurso(nombrerecurso, unidades)
    recursos.append(r)


# guardamos ubicacion de origen como zona conocida para los robots
z = Zonas(-200, 200)
zonas_conocidas1.append(z)
zonas_conocidas2.append(z)
zonas_conocidas3.append(z)
zonas_conocidas4.append(z)
zonas_conocidas_general.append(z)


# definimos funciones para el movimiento
def arriba(robot, zonas_conocidas):
    y = robot.objeto.ycor()
    robot.objeto.sety(y + 20)
    # validamos que no haya recurso en la nueva posicion
    for i in recursos:
        # si sí hay recurso lo llevamos a la nave
        if (robot.objeto.distance(i.objeto) < 20):
            robot.estado = "llevando recurso"
            robot.establecer_recurso(i)


def derecha(robot, zonas_conocidas):
    x = robot.objeto.xcor()
    robot.objeto.setx(x + 20)
    for i in recursos:
        if (robot.objeto.distance(i.objeto) < 20):
            robot.estado = "llevando recurso"
            robot.establecer_recurso(i)


def abajo(robot, zonas_conocidas):
    y = robot.objeto.ycor()
    robot.objeto.sety(y - 20)
    for i in recursos:
        if (robot.objeto.distance(i.objeto) < 20):
            robot.estado = "llevando recurso"
            robot.establecer_recurso(i)


def izquierda(robot, zonas_conocidas):
    x = robot.objeto.xcor()
    robot.objeto.setx(x - 20)
    for i in recursos:
        if (robot.objeto.distance(i.objeto) < 20):
            robot.estado = "llevando recurso"
            robot.establecer_recurso(i)


# definimos funciones para comprobar que podemos movernos hacia los lados
def comprobar_arriba(x, y, zonas_conocidas):
    y += 20
    bandera = True
    # validamos que no sea una zona ya explorada o que haya un obstaculo o que se salga del mapa
    for i in zonas_conocidas:
        if (i.coordenadax == x and i.coordenaday == y):
            bandera = False
    for i in obstaculos:
        if (i.coordenadax == x and i.coordenaday == y):
            bandera = False
    if (y > 200):
        bandera = False
    return bandera;


def comprobar_abajo(x, y, zonas_conocidas):
    y -= 20
    bandera = True
    for i in zonas_conocidas:
        if (i.coordenadax == x and i.coordenaday == y):
            bandera = False
    for i in obstaculos:
        if (i.coordenadax == x and i.coordenaday == y):
            bandera = False
    if (y < (-200)):
        bandera = False
    return bandera;


def comprobar_izquierda(x, y, zonas_conocidas):
    x -= 20
    bandera = True
    for i in zonas_conocidas:
        if (i.coordenadax == x and i.coordenaday == y):
            bandera = False
    for i in obstaculos:
        if (i.coordenadax == x and i.coordenaday == y):
            bandera = False
    if (x < (-200)):
        bandera = False
    return bandera;


def comprobar_derecha(x, y, zonas_conocidas):
    x += 20
    bandera = True
    for i in zonas_conocidas:
        if (i.coordenadax == x and i.coordenaday == y):
            bandera = False
    for i in obstaculos:
        if (i.coordenadax == x and i.coordenaday == y):
            bandera = False
    if (x > 200):
        bandera = False
    return bandera;


# validamos especificamente si hay obstaculos alrededor
def obstaculo_arriba(x, y):
    y += 20
    bandera = True
    for i in obstaculos:
        if (i.coordenadax == x and i.coordenaday == y):
            bandera = False
    return bandera;


def obstaculo_abajo(x, y):
    y -= 20
    bandera = True
    for i in obstaculos:
        if (i.coordenadax == x and i.coordenaday == y):
            bandera = False
    return bandera;


def obstaculo_izquierda(x, y):
    x -= 20
    bandera = True
    for i in obstaculos:
        if (i.coordenadax == x and i.coordenaday == y):
            bandera = False
    return bandera;


def obstaculo_derecha(x, y):
    x += 20
    bandera = True
    for i in obstaculos:
        if (i.coordenadax == x and i.coordenaday == y):
            bandera = False
    return bandera;


# definimos función de exploración
def explorar(robot, zonas_conocidas):
    aleatorio = random.randrange(4)
    x = robot.objeto.xcor()
    y = robot.objeto.ycor()
    bandera = False
    # comprobamos movimientos y guardamos el resultado en variables
    zona_arriba = comprobar_arriba(x, y, zonas_conocidas_general)
    zona_abajo = comprobar_abajo(x, y, zonas_conocidas_general)
    zona_derecha = comprobar_derecha(x, y, zonas_conocidas_general)
    zona_izquierda = comprobar_izquierda(x, y, zonas_conocidas_general)
    # lo mismo con obstaculos
    obstaculo_arr = obstaculo_arriba(x, y)
    obstaculo_aba = obstaculo_abajo(x, y)
    obstaculo_izq = obstaculo_izquierda(x, y)
    obstaculo_der = obstaculo_derecha(x, y)
    # si no se puede mover se rompe la regla de "no pasar por zonas conocidas"
    if (zona_abajo == False and zona_arriba == False and zona_derecha == False and zona_izquierda == False):
        zona_abajo = True;
        zona_arriba = True;
        zona_derecha = True;
        zona_izquierda = True;
        # si sí se puede mover solo validamos que no sea una zona conocida y que no se salga del mapa y que no haya obstaculo
    if (aleatorio == 0 and y < 199 and zona_arriba and obstaculo_arr):
        arriba(robot, zonas_conocidas)
        bandera = True
    if (aleatorio == 1 and y > (-199) and zona_abajo and obstaculo_aba):
        abajo(robot, zonas_conocidas)
        bandera = True
    if (aleatorio == 2 and x > (-199) and zona_izquierda and obstaculo_izq):
        izquierda(robot, zonas_conocidas)
        bandera = True
    if (aleatorio == 3 and x < 199 and zona_derecha and obstaculo_der):
        derecha(robot, zonas_conocidas)
        bandera = True
        # si se movió termina el turno y se guarda la nueva zona conocida
    if (bandera == True):
        z = Zonas(robot.objeto.xcor(), robot.objeto.ycor())
        zonas_conocidas.append(z)
        zonas_conocidas_general.append(z)
        time.sleep(0.3)
        # de lo contrario se vuelve a mover
    else:
        explorar(robot, zonas_conocidas)


iniciar_componentes()
time.sleep(2)
while (unidades_nave < 25):
    print("agente 1 (blanco),   estado: " + r1.estado)
    print("agente 2 (naranja),  estado: " + r2.estado)
    print("agente 3 (verde),    estado: " + r3.estado)
    print("agente 4 (amarillo), estado: " + r4.estado)
    print("nave (azul), unidades: " + str(unidades_nave))
    if (r1.estado == "llevando recurso"):
        r1.llevar_recurso(zonas_conocidas1)
    else:
        explorar(r1, zonas_conocidas1)

    if (r2.estado == "llevando recurso"):
        r2.llevar_recurso(zonas_conocidas2)
    else:
        explorar(r2, zonas_conocidas2)

    if (r3.estado == "llevando recurso"):
        r3.llevar_recurso(zonas_conocidas3)
    else:
        explorar(r3, zonas_conocidas3)

    if (r4.estado == "llevando recurso"):
        r4.llevar_recurso(zonas_conocidas4)
    else:
        explorar(r4, zonas_conocidas4)

r1.estado = "volviendo a la nave"
r2.estado = "volviendo a la nave"
r3.estado = "volviendo a la nave"
r4.estado = "volviendo a la nave"

for i in range(len(zonas_conocidas1)):
    if zonas_conocidas1[i].coordenadax == r1.objeto.xcor() and zonas_conocidas1[i].coordenaday == r1.objeto.ycor():
        r1.indicador2 = i
        break

for i in range(len(zonas_conocidas2)):
    if zonas_conocidas2[i].coordenadax == r2.objeto.xcor() and zonas_conocidas2[i].coordenaday == r2.objeto.ycor():
        r2.indicador2 = i
        break

for i in range(len(zonas_conocidas3)):
    if zonas_conocidas3[i].coordenadax == r3.objeto.xcor() and zonas_conocidas3[i].coordenaday == r3.objeto.ycor():
        r3.indicador2 = i
        break

for i in range(len(zonas_conocidas4)):
    if zonas_conocidas4[i].coordenadax == r4.objeto.xcor() and zonas_conocidas4[i].coordenaday == r4.objeto.ycor():
        r4.indicador2 = i
        break

while (
        r1.estado == "volviendo a la nave" or r2.estado == "volviendo a la nave" or r3.estado == "volviendo a la nave" or r3.estado == "volviendo a la nave"):
    print("agente 1 (blanco),   estado: " + r1.estado)
    print("agente 2 (naranja),  estado: " + r2.estado)
    print("agente 3 (verde),    estado: " + r3.estado)
    print("agente 4 (amarillo), estado: " + r4.estado)
    print("nave (azul), unidades: " + str(unidades_nave))
    r1.volver_a_la_nave(zonas_conocidas1)
    r2.volver_a_la_nave(zonas_conocidas2)
    r3.volver_a_la_nave(zonas_conocidas3)
    r4.volver_a_la_nave(zonas_conocidas4)

print("agente 1 (blanco),   estado: " + r1.estado)
print("agente 2 (naranja),  estado: " + r2.estado)
print("agente 3 (verde),    estado: " + r3.estado)
print("agente 4 (amarillo), estado: " + r4.estado)
print("nave (azul), unidades: " + str(unidades_nave))
turtle.title('Recursos encontrados')
time.sleep(1)
turtle.title('Despegue en 5')
time.sleep(1)
turtle.title('Despegue en 4')
time.sleep(1)
turtle.title('Despegue en 3')
time.sleep(1)
turtle.title('Despegue en 2')
time.sleep(1)
turtle.title('Despegue en 1')