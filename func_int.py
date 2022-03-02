#ejercicio 1

#Cambia el valor 10 en x a 15. Una vez que hayas terminado, x ahora debería ser [ [5,2,3], [15,8,9] ].
#Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'.
#En el directorio_deportes, cambia "Messi" por "Andrés".
#Cambia el valor 20 en z a 30.

x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0]= 15
print(x)

estudiantes[0]['last_name']='Bryant'
print(estudiantes)

directorio_deportes['fútbol'][0]='Andrés'
print(directorio_deportes)

z[0]['y']=30
print(z)







# #Ejercicio 2
# #Crea una función iterateDictionary(some_list)para que, dada una lista de diccionarios, la función recorra cada 
# diccionarios de la lista e imprima cada llave y el valor asociado. Por ejemplo, dada la siguiente lista:



estudiantes = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
        ]

def iterateDictionary(some_list):
    for x in range(0, len(some_list)):
        valor =""
        for key, val in some_list[x].items():
            valor += f"{key} - {val},"
        print(valor)    

iterateDictionary(estudiantes) 

# # debería devolver: (está bien si cada par clave-valor termina en 2 líneas separadas;

# un bonus para que aparezcan exactamente como se muestra a continuación)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel


# #ejercicio 3

#Crea una función iterateDictionary2(key_name, some_list)que, dada una lista de diccionarios y un nombre de clave, 
# la función imprima el valor almacenado en esa clave para cada diccionario. 
# Por ejemplo, iterateDictionary2('first_name', estudiantes) debería generar:
# Michael
# John
# Mark
# KB

def iterateDictionary2(key_name, some_list):
    for x in range(0, len(some_list)):
        for key, val in some_list[x].items():
            if key == key_name:
                print(val)

iterateDictionary2('last_name', estudiantes)
iterateDictionary2('first_name', estudiantes)


# #Y iterateDictionary2('last_name', estudiantes) debería generar:

# Jordan
# Rosales
# Guillen
# Tonel

# #ejercicio 4

# #Crea una función printInfo(some_dict)que, dado un diccionario cuyos valores son todos listas, imprima el nombre de cada clave junto con el tamaño de su lista, 
# # y luego imprima los valores asociados dentro de la lista de cada clave. Por ejemplo:

dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key, val in some_dict.items():
        print("------")
        print(f"{len(val)} {key.upper()}")
        for x in range (0, len(val)):
            print(val[x])


printInfo(dojo)


# # salida:
# 7 UBICACIONES
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORES
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon