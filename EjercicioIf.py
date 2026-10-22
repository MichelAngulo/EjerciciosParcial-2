nombre = ""
edad = 0
nacionalidad = ""

nombre = input("Ingrese su nombre: ") # Esta variable almacena un string ingresado por el usuario
edad = int(input("Ingrese su edad: ")) # Esta variable almacena un entero ingresado
nacionalidad = input("Ingrese su nacionalidad: ") # Esta variable almacena un string ingresado por el usuario

if edad >= 18: # el if va seguido de la condición y dos puntos
    print("Usted es mayor de edad") # si la condición es verdadera se ejecuta este bloque de código
else: