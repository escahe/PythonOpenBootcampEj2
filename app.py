class Alumno:
    nombre,nota = None,None
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota

    def imprimirDatos(self):
        print('Nombre:',self.nombre)
        print('Nota:',self.nota)
        print('Estado: Aprobado') if self.nota >= 3.5 else print('Estado: Desaprobado')

a1 = Alumno('Esteban Cabarcas',5)
a2 = Alumno('Bob Itto',2)
print()
a1.imprimirDatos()
print()
a2.imprimirDatos()
