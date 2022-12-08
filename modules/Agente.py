import time

class Agente:
    bandera = False
    indicador = -1
    fin_de_llevar = False
    indicador2 = 0

    def __init__(self, objeto, estado):
        self.objeto = objeto
        self.estado = estado

    def establecer_recurso(self, recurso_a_llevar):
        self.recurso_a_llevar = recurso_a_llevar

    def llevar_recurso(self, zonas_conocidas, recursos, nave):

        if self.recurso_a_llevar.unidades < 1 and self.indicador == -1:
            self.estado = "explorando"
            self.bandera = False
            self.fin_de_llevar = True

        if self.indicador == -1:
            self.recurso_a_llevar.unidades -= 1
            self.bandera = False
        # si estamos al principio ponemos bandera en "true"
        if self.indicador == -(len(zonas_conocidas)):
            nave.unidades += 1
            self.bandera = True
        # si las unidades del recurso llegan a 0 lo borramos y lo eliminamos
        if self.recurso_a_llevar.unidades == 0 and self.indicador == -1:
            self.recurso_a_llevar.objeto.color("black")
            for i in recursos:
                if i.objeto == self.recurso_a_llevar.objeto:
                    recursos.remove(i)
        # si bandera es false estamos en camino de vuelta asi que se le resta al indicador para la siguiente iteración
        if not self.bandera:
            self.indicador -= 1
        # si bandera es true estamos en el camino de ida asi que se le suma al indicador para la siguiente iteración
        if self.bandera:
            self.indicador += 1
        # nos movemos a la coordenada siguiente de nuestro arreglo, definida por la variable "indicador"
        if not self.fin_de_llevar:
            x = zonas_conocidas[self.indicador].coordenadax
            y = zonas_conocidas[self.indicador].coordenaday
            self.objeto.setx(x)
            self.objeto.sety(y)
        if self.fin_de_llevar:
            self.fin_de_llevar = False
            self.indicador = -1
        time.sleep(0.5)

    def volver_a_la_nave(self, zonas_conocidas):
        if self.indicador2 > 0:
            self.indicador2 -= 1
            x = zonas_conocidas[self.indicador2].coordenadax
            y = zonas_conocidas[self.indicador2].coordenaday
            self.objeto.setx(x)
            self.objeto.sety(y)
            time.sleep(0.5)
        else:
            self.estado = "en la nave"