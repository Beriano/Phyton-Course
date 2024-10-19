#Nivel básico:Verificar si un número es positivo, negativo o cero
#Descripción: Crea un programa que pida al usuario un número y verifique si es positivo, negativo o cero.

#Solicitar al usuario que ingrese el numero del balance de su estado financiero
numero = int(input("Introduce un número: ")) #Entero
#Verificar si el número es positivo, negativo o cero
if numero > 0:
    print("El número es positivo.", numero)
elif numero < 0:
    print("El número es negativo.", numero)
else:
    print("El número es cero.", numero)
    
#Determinar si un estudiante aprobó o no
#Descripción: Crea un programa que pida la calificación de un estudiante y determine si ha aprobado (60 o más) o no.

#Solicitar al usuario que ingrese la calificación del estudiante
calificacion = float(input("Introduce la calificación del estudiante: ")) #Flotante

#Verificar si la calificación es suficiente para aprobar
if calificacion >= 60:
    print("El estudiante ha aprobado.", calificacion)
else:
    print("El estudiante no ha aprobado.", calificacion)


#Nivel intermedio: Comprobar si un número es par o impar
#Descripción: Crea un programa que pida al usuario un número y determine si es par o impar.

#Solicitar al usuario que ingrese un número
numero = int(input("Introduce un número: "))

#Verificar si el número es par o impar
if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")
    
#Descripción: Crea un programa que pida al usuario un número y verifique si está en el rango de -10 a 10 (inclusive).   
#Solicitar al usuario que ingrese un número
numero = int(input("Introduce un número: "))

#Verificar si el número está en el rango de -10 a 10 (inclusive)
if -10 <= numero <= 10:
    print("El número está en el rango de -10 a 10.")
else:
    print("El número no está en el rango de -10 a 10.")

#Nivel Avanzado:
#Clasificación de Números
#Descripción: Crea una función que reciba una lista de números enteros y clasifique cada número como "positivo", "negativo" o "cero". La función debe devolver un diccionario que contenga el conteo de cada categoría.

def clasificar_numeros(lista_numeros):
    #Inicializar el diccionario para contar las categorías
    conteo = {"positivo": 0, "negativo": 0, "cero": 0}
    
    #Clasificar cada número en la lista
    for numero in lista_numeros:
        if numero > 0:
            conteo["positivo"] += 1
        elif numero < 0:
            conteo["negativo"] += 1
        else:
            conteo["cero"] += 1
    
    return conteo

#Ejemplo de lista para iterar
numeros = [3, -2, 0, 7, 10, 0, 2,-9,-2,7,0,13,-20,4] #Lista
resultado = clasificar_numeros(numeros)
print(resultado)

#Utilizar if, elif y else para clasificar los números.Deberá considerar si el número es impar o par, y agregar esta información al diccionario.

def clasificar_numeros(lista_numeros):
    #Inicializar el diccionario para contar las categorías
    conteo = {
        "positivo_par": 0,
        "positivo_impar": 0,
        "negativo_par": 0,
        "negativo_impar": 0,
        "cero": 0
    }
    
    #Clasificar cada número en la lista
    for numero in lista_numeros:
        if numero > 0:
            if numero % 2 == 0:
                conteo["positivo_par"] += 1
            else:
                conteo["positivo_impar"] += 1
        elif numero < 0:
            if numero % 2 == 0:
                conteo["negativo_par"] += 1
            else:
                conteo["negativo_impar"] += 1
        else:
            conteo["cero"] += 1
    
    return conteo

#Ejemplo de lista para iterar
numeros = [3, -2, 0, 7, 10, 0, 2,-9,-2,7,0,13,-20,4] #Lista
resultado = clasificar_numeros(numeros)
print(resultado)

#Cálculo de Tarifas de Envío
#Descripción: Diseña una función que calcule la tarifa de envío basada en el peso del paquete y el destino. La tarifa debe ser calculada usando las siguientes reglas:

    #Menos de 1 kg: $5
    #De 1 a 5 kg: $10
    #Más de 5 kg: $20
    #Si el destino es internacional, sumar un recargo del 50% al costo total.
    #Requisitos: Usa if y else para determinar el costo según el peso. Usa if adicional para comprobar si el envío es internacional y calcular el recargo correspondiente."
    
def calcular_tarifa_envio(peso, es_internacional):
    #Determinar el costo base según el peso
    if peso < 1:
        costo = 5
    elif 1 <= peso <= 5:
        costo = 10
    else:
        costo = 20
    
    #Aplicar recargo si el destino es internacional
    if es_internacional:
        costo *= 1.5
    
    return costo

#Ingresar el peso en kg
peso_paquete = float(input("Introduce el peso del paquete en kg: "))
destino_internacional = input("¿El destino es internacional? (sí/no): ").strip().lower() == "sí"

tarifa = calcular_tarifa_envio(peso_paquete, destino_internacional)
print(f"La tarifa de envío es: ${tarifa:.2f}")