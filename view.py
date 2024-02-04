from controller import *

#crear objeto de la clase personacontroller
obj=EmpleadoController()
#crear objeto de tipo persona
e1=obj.crearEmpleado(1,'123-45-6789', 'Juan', 'Perez', 'M','2001/08/11' 1500.0)
#imprimir datos
print('--------------------')
print(e1.mostrarDatos())
print('--------------------')
p1=obj.crearEmpleado(2,'234-938-3838','Juana Perez','F','2000/8/10',1600)
#imprimir datos
print('--------------------')
print(p1.mostrarDatos())
print('--------------------')
a1=obj.crearEmpleado(3,'254-93-1938','Luis Garcia','M','Python','1995/5/17',1600)
#imprimir datos
print('--------------------')
print(a1.mostrarDatos())
print('--------------------')



