#Trabajo Final por Claudia Susana Silva Fernández, curso Python 2024

#Programación para el registro de ejercicios terapeuticos en casa

print ("A continuación encontrará las opciones de ejercicios terapeuticos a aplicar:")

Opciones = ["1.Meditacion", 
            "2.RegistroPEC", 
            "3.Otra, asignada por el terapeuta"]

print(Opciones[:])

"""la cuarta actividad es asignada por el terapeuta,
siendo diferente cada semana. ¿cuál fue la actividad 3 de esta semana?"""
#habilita el ingreso de respuesta al usuario

while True:
    try:
        Actividad_3 = (str(input("Ingresa la actividad 3 asignada por el terapeuta:")))
        break
    except ValueError:
        print("Has introducido un dato incorrecto. Ingresa nuevamente tu respuesta")

#se anida la última respuesta en la lista de Opciones

Opciones = ["1.Meditacion", "2.RegistroPEC", "3.Otra, asignada por el terapeuta"]
Opciones [2] = "3."+Actividad_3
print(Opciones[:])

class Actividad():
#características de evaluación de las actividades
    
    def __init__(self):
        self.nombre= nombre
        self.cumplida = True
        self.incumplida = False
        self.impacto = impacto

        def estado (self):
        self.cumplida = True
        self.incumplida = False

#Marcacion de atributos de las actividades por el usuario    
Meditacion = (Actividad)
print("La primera actividad es la Meditacion")

Estado_Meditacion=(input("Ingresa 'cumplida' si la meditacion se realizó, o 'incumplida' en caso contrario:")).strip().lower()
while True:
    try:
        Impacto_Meditacion=(int(input("Asigna un valor de 1 a 10 al impacto de la meditacion en tu mejoría, siendo 10 el valor de máxima mejoría y 1 el de menor:")))
        break
    except ValueError: 
        print("Has introducido un dato incorrecto. Ingresa nuevamente tu respuesta de 1 a 10")

RegistroPEC = (Actividad)
print("La segundaa actividad es el registroPEC")

Estado_RegistroPEC=(input("Ingresa 'cumplida' si el registroPEC se realizó, o 'incumplida' en caso contrario:")).strip().lower()
while True:
    try:
        Impacto_RegistroPEC=(int(input("Asigna un valor de 1 a 10 al impacto deL registroPEC en tu mejoría, siendo 10 el valor de máxima mejoría y 1 el de menor:")))
        break
    except ValueError: 
        print("Has introducido un dato incorrecto. Ingresa nuevamente tu respuesta de 1 a 10")

Asignada = (Actividad)
print (("La tercera actividad es"), (Actividad_3))

Estado_Asignada=(input("Ingresa 'cumplida' si la tercera actividad se realizó, o 'incumplida' en caso contrario:")).strip().lower()
while True:
    try:
        Impacto_Asignada=(int(input("Asigna un valor de 1 a 10 al impacto de la tercera actividad en tu mejoría, siendo 10 el valor de máxima mejoría y 1 el de menor:")))
        break
    except ValueError: 
        print("Has introducido un dato incorrecto. Ingresa nuevamente tu respuesta de 1 a 10")
        
Resumen = ()
print("La sintesis del seguimiento de sus actividad terapeuticas de las semana es")
print (("meditacion:") + (Estado_Meditacion) + ("con un impacto de") + (Impacto_Meditacion))
        

        break
    except AttributeError: 
        print("Has introducido un dato incorrecto. Ingresa nuevamente tu respuesta de 1 a 10")

while Impacto_Meditacion <= 5:
    print("el impacto es bajo")
if Impacto_Meditacion >= 6:
    print("el impacto es moderado")


    except AttributeError: 
        print("Has introducido una opción de respuesta incorrecta. Ingresa nuevamente tu respuesta entre 'cumplida' o 'no cumplida'")
    else: 
        print ("el estado de la meditacion para esta semana es:", Estado_Meditacion)
        break
   