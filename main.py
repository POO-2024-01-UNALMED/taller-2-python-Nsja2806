class Asiento:
    def __init__(self,color,precio,registro):
        self.color=color
        self.precio=precio
        self.registro=registro
    
    def cambiarColor(self,color):
        if ((color=="amarillo") or (color=="verde") or (color=="negro") or (color=="blanco") or (color=="rojo")):
            self.color=color

class Auto:
    cantidadCreados=0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo=modelo
        self.precio=precio
        self.precio=asientos
        self.marca=marca
        self.motor=motor
        self.registro=registro
        self.asientos=asientos
        

    def cantidadAsientos(self):
        ca=00 #se define la variable ca como cantidad de asientos
        for i in self.asientos:
            if i!=None:
                ca+=1
        return ca

    def verificarIntegridad(self):
        if (self.registro!=self.motor.registro):
            return "Las piezas no son originales"
        for i in self.asientos:
            if i!=None:
                if (self.registro!=i.registro):
                    return "Las piezas no son originales"
        return "Auto original"
    
class Motor:
    def __init__(self,numeroCilindros,tipo, registro):
        self.numeroCilindros=numeroCilindros
        self.tipo=tipo
        self.registro=registro
    
    def cambiarRegistro(self,registro):
        self.registro=registro
    
    def asignarTipo(self,tipo):
        if ((tipo=="electrico") or (tipo=="gasolina")):
            self.tipo=tipo
        

            
