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
    
    def __init__(self, nombre, estado, impacto):
        self.nombre= (Meditacion, RegistroPEC, Asignada)
        self.cumplida = True
        self.incumplida = False
        self.impacto = impacto

    def estado (self):
        self.cumplida = True
        self.incumplida = False
        
    def resumen (self):
        self.resumen = "\n"

 #Marcacion de atributos de las actividades del usuario, una por una    
Meditacion = (Actividad)
print("La primera actividad es la Meditacion")

while True:
    try:
        Estado_Meditacion=(input("Ingresa 'cumplida' si la meditacion se realizó, o 'incumplida' en caso contrario:")).strip().lower()
        if ("cumplida" or "no cumplida") not in Estado_Meditacion:
            print ("solo se aceptan las respuestas 'cumplida' o 'no cumplida'")
    except AttributeError: 
        print("Has introducido una respuesta incorrecta. Ingresa nuevamente tu respuesta entre las opciones 'cumplida' o 'no cumplida'")
    else: 
        print ("El estado de la meditacion para esta semana es:", Estado_Meditacion)
    break

while True:
    try:
        Impacto_Meditacion=(int(input("Asigna un valor de 1 a 10 al impacto de la meditacion en tu mejoría, siendo 10 el valor de máxima mejoría y 1 el de menor:")))
        if Impacto_Meditacion < 1 or Impacto_Meditacion > 10:
            print ("el valor debe estar entre 1 a 10")
    except ValueError: 
        print("Has introducido un dato incorrecto. Ingresa nuevamente tu respuesta de 1 a 10")
    else: 
        print ("El impacto de la meditacion fue:", Impacto_Meditacion)
        break

RegistroPEC = (Actividad)
print("La segunda actividad es el registroPEC")

while True:
    try:
        Estado_RegistroPEC=(input("Ingresa 'cumplida' si el RegistroPEC se realizó, o 'incumplida' en caso contrario:")).strip().lower()
        if ("cumplida" or "no cumplida") not in Estado_RegistroPEC:
            print ("solo se aceptan las respuestas 'cumplida' o 'no cumplida'")
    except AttributeError: 
        print("Has introducido una respuesta incorrecta. Ingresa nuevamente tu respuesta entre las opciones 'cumplida' o 'no cumplida'")
    else: 
        print ("El estado del RegistroPEC para esta semana es:", Estado_RegistroPEC)
        break

while True:
    try:
        Impacto_RegistroPEC=(int(input("Asigna un valor de 1 a 10 al impacto del RegistroPEC en tu mejoría, siendo 10 el valor de máxima mejoría y 1 el de menor:")))
        if Impacto_RegistroPEC < 1 or Impacto_RegistroPEC > 10:
            print ("El valor debe estar entre 1 a 10")
    except ValueError: 
        print("Has introducido un dato incorrecto. Ingresa nuevamente tu respuesta de 1 a 10")
    else: 
        print ("El impacto del RegistroPEC fue:", Impacto_RegistroPEC)
        break

Asignada = (Actividad)
print(("La tercera actividad es"), (Actividad_3))

while True:
    try:
        Estado_Asignada=(input("Ingresa 'cumplida' si la actividad asignada por el terapeuta se realizó, o 'incumplida' en caso contrario:")).strip().lower()
        if ("cumplida" or "no cumplida") not in Estado_Asignada:
            print ("solo se aceptan las respuestas 'cumplida' o 'no cumplida'")
    except AttributeError: 
        print("Has introducido una respuesta incorrecta. Ingresa nuevamente tu respuesta entre lass opciones 'cumplida' o 'no cumplida'")
    else: 
        print ("El estado de la actividad asignada por el terapeuta para esta semana es:", Estado_Asignada)
    break

while True:
    try:
        Impacto_Asignada=(int(input("Asigna un valor de 1 a 10 al impacto de la actividad asignada por el terapeuta en tu mejoría, siendo 10 el valor de máxima mejoría y 1 el de menor:")))
        if Impacto_Asignada < 1 or Impacto_Asignada > 10:
            print ("El valor debe estar entre 1 a 10")
    except ValueError: 
        print("Has introducido un dato incorrecto. Ingresa nuevamente tu respuesta de 1 a 10")
    else: 
        print ("El impacto de la actividad asignada por el terapueta fue:", Impacto_Asignada)
        break

#Resumen
print("A continuación se presentan las actividades cumplidas durante la semana:")

Resumen = ()
print(f"Meditacion:{Estado_Meditacion};  RegistroPEC: {Estado_RegistroPEC}; Asignada: {Estado_Asignada}")

#Eliminacion de tarea
Eliminacion=()
if (Impacto_Asignada) <= 6:
        Opciones.remove(Opciones[2])
        print ("se eliminará la actividad asignada por su terapeuta al no considerarse de impacto para su proceso")

#cierre
print("Debido al impacto positivo en su proceso, las siguientes actividades serán opciones para futuros ejercicios terapeuticos:")
print(Opciones[:])
print("Me alegró haber podido ayudar. Hasta la próxima")
