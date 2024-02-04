from model import *
from util import *

class EmpleadoController:
    def __init__(self):
        pass
    
    # metodo crea objeto de tipo persona
    def crearEmpleado(self,tipo,ns,nom,apel,sx,v1,v2):
        self.per=None
        match tipo:
            case Opcion.EmpleadoAsalariado.value:
                
                self.per=EmpleadoAsalariado(ns,nom,apel,sx,v1,v2)
            case Opcion.EmpleadoPorHoras.value:
                
                self.per=EmpleadoPorHoras(ns,nom,apel,sx,v1,v2)
            case Opcion.EmpleadoporComision.value:
            
                self.per=EmpleadoporComision(ns,nom,apel,sx,v1,v2)
        return self.per
    
                