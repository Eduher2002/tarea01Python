# -*- coding: utf-8 -*-
"""
Created on Sun Apr 27 09:03:41 2025

@author: andhe
"""
   
#%%
############# EJERCICIO 1: PAR O IMPAR #############
"""Alumno: Eduardo Hernández Hernández
   Tarea 01 de Fundamentos de Python 2025"""

# Se pedirá un número entero al usuario y se determinará si es par o impar
print("Este programa determina si un número entero es par o impar.\n")
numero = input("Escribe un número entero en el sistema decimal:\t") # pide numero al usuario

if type(eval(numero)) == int : # Evalua si el numero ingresado es entero
    numero_entero = int(numero) # ya que si es un entero, se guarda en la variable numero_entero
    if numero_entero % 2 == 0:
        print(f"El número {numero} es par")
    else:
        print("El número es impar.\n")

else:
    print("El número que ingresaste no es un número entero, este programa sólo sirve para números enteros.\n")
    
    
#%%

############# EJERCICIO 2: EDAD MINIMA #############
"""Alumno: Eduardo Hernández Hernández
   Tarea 01 de Fundamentos de Python 2025"""

# Programa que pregunta la edad a un usuario y determina si es mayor de edad o menor de edad

print("Este es un programa que determina si eres mayor o menor de edad. \n")
edad = input("Ingresa tu edad: ")
Edad = int(edad)

if Edad >= 18:
    print("Eres mayor de edad, vamos por unas cheves.")
elif Edad >= 0 and Edad < 18:
    print("Eres menor de edad.")
else:
    print("Usted nisiquiera es humano.")
        

#%%

############# EJERCICIO 3: SALUDO PERSONALIZADO #############
"""Alumno: Eduardo Hernández Hernández
   Tarea 01 de Fundamentos de Python 2025"""

#Pide el nombre del usuario, si comienza con A mayúscula, se muestra un saludo especial, de lo contrario da un saludo normal. 

nombre = input("Escribe tu nombre: ") # Pide el nombre al usuario


if nombre.startswith(" ") == True: # verifica que el usuario no haya comenzado a escribir su nombre usando la barra espaciadora
    nombre = nombre.strip(" ") # en caso de que haya oprimido la tecla de espacio, elimina ese espacio.

if nombre.isalpha() == True: # verifica si el nombre contiene unicamente letras
    if nombre.startswith("A"): # verifica si el nombre empieza con A
        print("HOLAA, ¿CÓMO ESTÁS', ¿QUE CUENTA LA FAMILIA?, ¡¡¡¿SE VA A HACER O NO SE VA A HACER...?!!!")
    else:
        print("Hola, que tal.")
else:
    print(f"{nombre} no es el nombre de una persona, al menos no una que viva en el planeta Tierra.\n")
    

#%%

############# EJERCICIO 4: TIPO DE NUMERO #############

"""Alumno: Eduardo Hernández Hernández
   Tarea 01 de Fundamentos de Python 2025"""

# pide un numero, y muestra si es positivo, negativo o cero. 

numero = input("Ingresa un numero ") # pide el numero
numero = eval(numero) # convierte el numero tipo str ingresado a uno tipo int o float según sea el caso interpretado por python. 

if numero > 0: # verifica si el numero es mayor que cero
    print(f"El número {numero} es positivo")
elif numero == 0:# sino es mayor que cero, entonces es menor o igual a cero; aqui verifica si el numero es igual a cero. 
    print(f"El número {numero} es cero.")
else: # sino se cumplió ninguna de las anteriores, significa que el numero es menor que cero, es decir, negativo.
    print(f"El número {numero} es negativo.")



#%%

############# EJERCICIO 5: ¿ES UN NÚMERO ENTERO VÁLIDO? #############

"""Alumno: Eduardo Hernández Hernández
   Tarea 01 de Fundamentos de Python 2025"""

# Pide un numero, si representa un número entero, lo convertimos a entero y mostramos el doble. De lo contrario, mostramos que no es válido. 

texto = input("Escribe un número: ") # pide un numero, escrito en el sistema decimal

if texto.isdigit() == True : # verifica que todos los caracteres del str texto sean numericos, (en el sistema decimal)
    numero = int(texto) # convierte el texto tipo str a un objeto tipo int y lo asigna a la variable numero
    print(f"El doble del número {numero} es {2*numero}")
elif texto.startswith("-") == True and type(eval(texto)) == int: # consideramos el caso de que el usuario ingrese un entero negativo, por ejemplo el número -3. Tambien verificamos que el numero sea un entero
    numero = eval(texto)
    print(f"El doble del número {numero} es {2*numero}")
elif texto.startswith("+") == True and type(eval(texto)) == int: # Consideramos el hecho de que el usuario ingrese el número comenzando con el signo positivo + y debe cumplirse que el numero tambien sea un entero
    numero = eval(texto)
    print(f"El doble del número {numero} es {2*numero}")
else:
    print("El número que ingresaste no es válido.")
    
    
"""Nótese que en este código se supuso que el número
ingresado por el usuario ya está escrito en el sistema decimal"""


#%%

############# EJERCICIO 6: CLASIFICACIÓN DE EDAD #############
"""Alumno: Eduardo Hernández Hernández
   Tarea 01 de Fundamentos de Python 2025"""
   

"""Menor de 13 años es la etapa de niñez, de 13 a 17 es adolescencia , de 18 a 59
es la adultez y mayor a 60 es adulto mayor."""


print("Este es un programa que determina si eres mayor o menor de edad. \n")
edad = input("Ingresa tu edad: ")
Edad = int(edad)

if Edad >= 60:
    print("Eres un adulto mayor.")
elif Edad >=18 and Edad <= 59:
    print("Eres un adulto.")
elif Edad >= 13 and Edad <= 17:
    print("Eres un adolescente.")
elif Edad >= 0 and Edad < 13:
    print("Eres un niño, bienvenido al mundo.")
else:
    print("Usted nisiquiera es humano o eres de la época de los dinosaurios.")
    

#%%

############# EJERCICIO 7: CONTRASEÑA SECRETA #############
"""Alumno: Eduardo Hernández Hernández
   Tarea 01 de Fundamentos de Python 2025"""

# Pide una contraseña, si es Python123 (respetando mayúsculas), muestra "Acceso concedido", de lo contrario se mostrará "Acceso denegado".

contraseña = input("Ingresa la contraseña: ") # pide la contraseña

if contraseña.isalnum() == True and contraseña == "Python123": # Verificamos si la contraseña ingresada no contiene caracteres que no sean alfanuméricos y que sea la contraseña permitida
    print("Acceso concedido.")
else:
    print("Acceso denegado.")


#%%

############# EJERCICIO 8: CALIFICACIÓN ESCOLAR #############
"""Alumno: Eduardo Hernández Hernández
   Tarea 01 de Fundamentos de Python 2025"""

# Pide una calificación de 0 a 10, si es 6 o mas, aprobado, de lo contrario será reprobado.


calificacion_texto = input("Escribe tu calificación: ")
calificacion_numerica = int(calificacion_texto)

if calificacion_numerica >= 0 and calificacion_numerica <= 10:
    if calificacion_numerica >= 6:
        print("Aprobado.")
    else:
        print("Reprobado.")
else:
    print("Tu calificación debe estar comprendida entre el 0 y 10.")
 
    
#%%

############# EJERCICIO 9: VERIFICADOR DE MAYÚSCULAS #############

"""Alumno: Eduardo Hernández Hernández
   Tarea 01 de Fundamentos de Python 2025"""


"""Pide una palabra, si toda está en mayúsculas, imprime GRITANDO, 
si está en minúsculas imprime Susurrando, si está mezclada imprime Normal """


palabra = input("Escribe una palabra: ") # pide una palabra
palabra = palabra.strip() # elimina los espacios (solo en caso de que el usuario haya escrito la palabra con espacios)

if palabra.isalpha() == True : # verifica que la palabra contenga exclusivamente caracteres alfabéticos
    if palabra.upper() == palabra : # ¿palabra esta en mayusculas?
        print("GRITANDO.")
    elif palabra.lower() == palabra : # ¿palabra esta en minusculas? 
        print("Susurrando.")
    elif palabra.swapcase() != palabra: # ¿palabra esta en mayusculas y minusculas?
        print("Normal")
else:
    print(f"{palabra} no es una palabra.") # si ninguna de las condiciones anteriores se cumple, significa que la palabra contiene elementos que no son alfabéticos. Por lo tanto no es válida
    

#%%

############# EJERCICIO 10: COMPARADOR DE DOS NUMEROS #############
"""Alumno: Eduardo Hernández Hernández
   Tarea 01 de Fundamentos de Python 2025"""   
    
# Pide dos numeros enteros, indica cuál es mayor o si son iguales. 

numero1 = input("Ingrese un número entero: ") # pide los numeros
numero2 = input("Ingrese otro número entero: ")

if numero1.isdigit() == True and numero2.isdigit() == True: # evalua si todos los caracteres son puramente numericosnumericos, esto excluye a aquellos escritos con punto decimal o negativos en forma de str
    numero1 = int(numero1) # conversion de los numeros tipo str a numeros tipo int
    numero2 = int(numero2)
    if numero1 < numero2 : # verifica que numero es mayor o si son iguales.
        print(f"El número {numero2} es mayor.")
    elif numero1 == numero2 :
        print("Ambos números son iguales.")
    else:
        print(f"El número {numero1} es mayor.")
elif numero1.startswith("-") == True or numero2.startswith("-") == True : # tal vez el usuario ingreso enteros negativos
    if type(eval(numero1)) == int and type(eval(numero2)) == int : # verificamos que sean enteros negativos 
        numero1 = int(numero1) # conversion de numeros str a numeros int
        numero2 = int(numero2)
        if numero1 < numero2 : # vemos que numero es mayor o si son iguales
            print(f"El número {numero2} es mayor.")
        elif numero1 == numero2 :
            print("Ambos números son iguales.")
        else:
            print(f"El número {numero1} es mayor.")
    else: 
        print("Se requiere que ambos números sean enteros.")
elif type(eval(numero1)) == float and type(eval(numero2)) == float: # tal vez los numeros que ingresó no son enteros.
    print("Se requiere que ambos números sean enteros.")
else:
    print("Lo que ingresaste no son números, al menos no en el sistema decimal.")
 


#%%
############# EJERCICIO 11: VERIFICADOR DE AÑO BISIESTO #############
"""Alumno: Eduardo Hernández Hernández
   Tarea 01 de Fundamentos de Python 2025"""

# pide un año, si es divisible entre 4 y (no entre 100 o si entre 400), es bisiesto. 

año = input("Escribe un año: ")
año = año.strip() # Se eliminan los espacios en caso de que el usuario haya oprimido la barra espaciadora.

"""Un año es bisiesto si es divisible entre 4 y (no entre 100 o sí entre 400), es bisiesto."""

if año.isdigit() == True:
    año = int(año)
    if (año // 4) * 4 == año and (año // 100) * 100 != año: # Divisible entre 4 pero no entre 100
        print(f"El año {año} es bisiesto.")
    elif (año // 4) * 4 == año and (año // 400) * 400 == año: # Divisible entre 4 y divisible entre 400
        print(f"El año {año} es bisiesto.")
    else:
        print(f"El año {año} no es bisiesto.")
    
    
"""Se sustituyo el operador % usando la division entera; pues si el cociente de la división entera (a // b) multiplicado
por b es exactamente igual al número a, entonces significa que el resultado de la división normal (a / b) es entero, es decir, 
a es divisible por b. Por otro lado, si el cociente de la división entera (a // b) multiplicado
por b NO es exactamente igual al número a, significa que el cociente de la división normal (a / b) tiene decimales, 
es decir, el número a NO es divisible por b"""

#%%

############# EJERCICIO 12: DETECTOR DE PALÍNDROMOS SIMPLES #############
"""Alumno: Eduardo Hernández Hernández
   Tarea 01 de Fundamentos de Python 2025"""



"Pide una frase. Verifica si es igual al revés"

### AQUI CREAMOS TABLA DE TRADUCCION PARA TRADUCIR LETRAS RARAS A LETRAS QUE ENTENDAMOS.

"áäàéëèíïìóöòúüù".upper() # convertimos a mayusculas las letras feas
"aaaeeeiiiooouuu".upper() # convertimos a mayusculas las letras chidas

tabla_de_traduccion = str.maketrans("áäàéëèíïìóöòúüùÁÄÀÉËÈÍÏÌÓÖÒÚÜÙ", "aaaeeeiiiooouuuAAAEEEIIIOOOUUU") # creamos la tabla que se usara para convertir letras feas en letras chidas

### AQUI TERMINAMOS DE CREAR TABLA DE TRADUCCION PARA TRADUCIR LETRAS RARAS A LETRAS QUE ENTENDAMOS.


### AQUI COMIENZA CÓDIGO PARA DETECTAR PALINDROMOS

frase_ingresada = input("Escribe una frase: ")

frase_entendible = frase_ingresada.translate(tabla_de_traduccion) # convierte la frase fea a una que entendamos

frase_minusculas = frase_entendible.casefold() # Convertimos la frase original a una entendible y con todo en minusculas

lista_frase_sin_espacios = frase_minusculas.split(" ") # obtenemos una lista, cuyos elementos son las palabras de la frase original pero entendible y todo en minusculas

frase_limpia = "".join(lista_frase_sin_espacios) # juntamos todos los elementos de la lista anterior

frase_limpia_reves = frase_limpia[:: -1] # invertimos la frase limpia

if frase_limpia == frase_limpia_reves :
    print("La frase que ingresaste es un palíndromo. ")
else:
    print("La frase que ingresaste no es un palíndromo. ")


#%%
############# EJERCICIO 13: CLASIFICADOR DE TEMPERATURA #############
"""Alumno: Eduardo Hernández Hernández
   Tarea 01 de Fundamentos de Python 2025"""


"""Clasifica la temperatura de la siguiente forma: 
    * Congelado si T < 0
    * Templado si 0 <= T <= 25
    * Caluroso si T > 25"""

temp_celsius = input("Por favor ingresa la temperatura en la escala celsius: ")

temp_celsius = float(temp_celsius) # convertimos el numero ingresado por el usuario a un número.
# Elegimos una conversión a float porque las temperaturas pueden tener decimales.

if temp_celsius >= -273.15 :
    if temp_celsius >= 0 and temp_celsius <= 25:
            print("El clima es templado.")
    elif temp_celsius > 25 :
            print("El clima es caluroso")
    else:
        print("El clima es congelado.")
else:
    print("Esa temperatura es fisicamente imposible.")
        
    

#%%
############# EJERCICIO 14: NOMBRE VÁLIDO Y LARGO #############
"""Alumno: Eduardo Hernández Hernández
   Tarea 01 de Fundamentos de Python 2025"""
   

"""Pide un nombre:
    
    * Si no contiene solo letras, muestra "Nombre inválido""
    * Si es válido, clasifica su longitud:
           ** < 5 Nombre corto.
           ** 5 a 8 Nombre promedio.
           ** > 8 Nombre largo.  """


nombre = input("Dime el nombre de una persona: ")

if nombre.isalpha() == True: # verifica que todos los caracteres sean alfabéticos
    tamaño_nombre = len(nombre) # cuenta cuantos carácteres tiene la variable nombre
    if tamaño_nombre > 8:
        print("Nombre largo.")
    elif tamaño_nombre >= 5 and tamaño_nombre <= 8 :
        print("Nombre promedio.")
    elif tamaño_nombre < 5 :
        print("Nombre corto.")
else:
    print(f"{nombre} no es el nombre de una persona, al menos no el de una en la Tierra.")
    


#%%
############# EJERCICIO 15: SIMULADOR DE LOGIN BÁSICO #############
"""Alumno: Eduardo Hernández Hernández
   Tarea 01 de Fundamentos de Python 2025"""
   
   

"""Pide usuario y contraseña. Si el usuario es "admin" y la contraseña "1234", imprime "Bienvenido administrador". 
Si el usuario es correcto pero la contraseña no, imprime "Contraseña incorrecta". En cualquier otro caso, imprime "Acceso denegado"."""


usuario = input("Usuario: ")
contraseña = input("Contraseña: ")

if usuario == "admin" and contraseña == "1234":
    print("Bienvenido administrador")
elif usuario == "admin" and contraseña != "1234":
    print("Contraseña incorrecta.")
else:
    print("Acceso denegado")

exit()
#%%

















































































 