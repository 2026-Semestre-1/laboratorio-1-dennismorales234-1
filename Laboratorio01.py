"""
nombre: calculadora
entradas:operacion, op1, op2
salidas:
restriciones: los parametros debe ser enteros
        los operadores deben ser enteros
        suma debe ser 1
        resta debe ser 2
        multiplicacion debe ser 3
        division debe ser 4
"""

def calculadora(operacion, op1, op2):
     # Verifica que el parámetro sea entero
    if not isinstance(op1, int):
        return "Error: El parámetro num debe ser de tipo entero"
    
     # Verifica que el parámetro sea entero
    if not isinstance(op2, int):
        return "Error: El parámetro num debe ser de tipo entero"
    
    if  operacion == 1:
        return op1 + op2
    elif operacion == 2:
        return op1 - op2
    elif operacion == 3:
        return op1 * op2
    elif operacion == 4:
        return op1 / op2
"""
Nombre:contadordigitos
Entradas:num,digitos
restricciones
    Ambos parámetros deben ser de tipo entero
    el párametro llamado digito debe ser menor a 10 y mayor igual a 0
    se espera que la salida retorne el número de veces que el dígito aparece en el número
"""
def contadorDigitos(num, digito):

     # Verifica que el parámetro sea entero
    if not isinstance(num, int):
        return "Error: El parámetro num debe ser de tipo entero"

    # Verifica que digito sea entero
    if not isinstance(digito, int):
        return "Error: El parámetro digito debe ser de tipo entero"

    # Verifica que digito sea menor a 10
    if abs(digito) >= 10:
        return "Error: El parámetro digito debe ser un valor menor a 10"

    num = abs(num)
    digito = abs(digito)

    contador = 0

    # Caso especial
    if num == 0 and digito == 0:
        return 1

    # Recorre los dígitos del número
    while num > 0:
        if num % 10 == digito:
            contador += 1
        num = num // 10

    return contador
"""
nombre:sumatoria_v2
entradas: inicio, fin, distancia, excepcion
salidas:
restriciones: los parametros deben ser enteros
    Solo el parámeetro distancia podría ser negativo
    Los párametros distancia y excepcion debe ser menor a 10 y mayor a 0.
    Los valores de inicio y fin deben ser positivos
    Si la distancia es un número negativo, el valor de fin debe ser menor a inicio
    Si la distancia es un número positivo, el valor de fin debe ser mayor a inicio
    Si excepcion es igual a cero, se debe ignorar este valor, lo contrario,
todo número dentro de la secuencia entre inicio y ** final** sea divisible por esta excepcion debe omitirse
en la suma
"""
def sumatoria_V2(inicio, fin, distancia, excepcion):
      # Verifica que el parámetro sea entero
    if not isinstance(inicio, int):
        return "Error: El parámetro num debe ser de tipo entero"

    # Verifica que parámetro sea entero
    if not isinstance(fin, int):
        return "Error: El parámetro digito debe ser de tipo entero"
      # Verifica que el parámetro sea entero
    if not isinstance(distancia, int):
        return "Error: El parámetro num debe ser de tipo entero"

    # Verifica que parámetro sea entero
    if not isinstance(excepcion, int):
        return "Error: El parámetro digito debe ser de tipo entero"
    if inicio < 0 and fin < 0 and excepcion:
        return "Error tiene un numero negativo"
    
    
