#clase principal
class Empleado:
    #constructor
    def __init__(self,numero_seguro_social,nombre,apellido,sexo,fecha):
        self.__numero_seguro_social=numero_seguro_social
        self.__nombre=nombre
        self.__apellido=apellido
        self.__sexo=sexo
        self.__fecha=fecha
    
    def registrar(self):
        pass    
    def mostrarDatos(self):
    
        return f'\nnumero_seguro_social :{self.__numero_seguro_social}\nNombre :{self.__nombre}\nApellido :{self.__apellido}\nSexo :{self.__sexo}\nFecha :{self.__fecha}'
    

#end class
#clases heredadas
class EmpleadoAsalariado(Empleado):
    #constructor
    def __init__(self, numero_seguro_social, nombre,apellido, sexo,fecha,salario_semanal):
        super().__init__(numero_seguro_social,nombre,apellido,sexo,fecha)
        self.__salario_semanal=salario_semanal
        
    def registrar(self):
        self.__salario_semanal=float(input('Ingrese el salario semanal: '))
    #redefinr metodo mostrardatos de la clase Empleado
    def mostrarDatos(self):
        print(f'\nBoleta de pago para {self.__nombre}{self.__apellido}')
        print(f'Numero de seguro social: {self.__numero_seguro_social}')
        print(f'Salario semanal: ${self.__salario_semanal}')
#end class                    

class EmpleadoPorHoras(Empleado):
    #constructor
    def __init__(self, numero_seguro_social, nombre,apellido, sexo,fecha,sueldo_hora,horas_trabajadas):
        super().__init__(self.__numero_seguro_social,nombre,apellido,sexo,fecha)
        self.__sueldo_hora=sueldo_hora
        self.__horas_trabajadas=horas_trabajadas
    def registrar(self):
        self.__sueldo_hora=float(input('Ingrese el sueldo por hora: '))
        self.__horas_trabajadas=float(input('Ingrese el numero de horas trabajadas: '))    
            
    #redefinr metodo mostrardatos de la clase empleado
    def mostrarDatos(self):
        print(f'\nBoleta de pago para {self.__nombre} {self.__apellido}')
        print(f'Numero de seguro social: {self.__numero_seguro_social}')
        print(f'Sueldo por hora: ${self.__sueldo_hora}')
        print(f'Horas trabajadas: {self.__horas_trabajadas} horas')
        print(f'Total a pagar: ${self.__sueldo_hora*self.__horas_trabajadas}')      
              
#end class                    

class EmpleadoporComision(Empleado):
    #constructor
    def __init__(self, numero_seguro_social, nombre, apellido, sexo, fecha, venta_bruta, tasa_comision):
        super().__init__(numero_seguro_social, nombre, apellido, sexo, fecha)
        self.venta_bruta = venta_bruta
        self.tasa_comision = tasa_comision

    def registrar(self):
        self.venta_bruta = float(input("Ingrese la venta bruta: "))
        self.tasa_comision = float(input("Ingrese la tasa de comisión (%): "))

    def mostrar(self):
        print(f"\nBoleta de pago para {self.nombre} {self.apellido}")
        print(f"Número de Seguro Social: {self.numero_seguro_social}")
        print(f"Venta Bruta: ${self.venta_bruta}")
        print(f"Tasa de Comisión: {self.tasa_comision}%")
        print(f"Total a pagar: ${self.venta_bruta * (self.tasa_comision / 100)}") 
#end class 
