# Conceptos básicos sobre programación en Python

![Fairlight CMI de 1979, primer sistema de workstation inteligente para audio desde el utilizo inteligente de samples. Antesesores de Python en sistemas binarios inteligentes.](../_resources/Fairlight_II_Page_R_vista-1.jpg)

* * *

#### ¿Qué es un condicional?

Un condicional es una sentencia utilizada en Python para ejecutar ciertos bloques de código basada en condiciones específicas. Estas sentencias ayudan a controlar el flujo de un programa, haciendo que se comporte diferentemente en distintas situaciones. Estas estructuras de control permiten tomar decisiones y ejecutan bloques de código dependiendo si la sentencia es verdadera (True) o falsa (False), lo que llamamos valor booleano.

La sentencia **if** es la forma más simple de condicional. Ejecuta un bloque de código si la condición dada es verdadera (true).Ej:

```
    age = 20
    if age >= 16:
        print('Can rent a car')
```

Por otro lado, si la condición no es verdadera (False), nos permite hacer uso de **Else**, desde donde podemos ejecutar otro bloque de código en el caso de que la primera sentencia no sea verdadera, y así cubrir la opción sobrante de una condición. Ej:

```
    age = 15
    if age >= 16:
        print('Can rent a car')
    else:
        print('Can´t rent a car')
```

En el caso de que queramos hacer uso de más de una condición, podemos recurrir al **Elif**, desde donde se tomarán en cuenta las condiciones que se mencionen y el 'Else', en el caso de que ninguna de las condiciones sea aplicable. Ej:

```
    age = 90
    if age >= 80: 
        print('You shouldn´t be driving')
    elif age >= 16:
        print('Can rent a car')
    else:
        print('Can´t rent a car')
```

Los condicionales son importantes y beneficiosos a la hora de llevar a cabo tareas que nos requieren encontrar elementos en listas, diccionarios, tuplas y variables. A su vez nos permiten verificar elementos a través de operadores. Los principales operadores son:

```
	== igualdad
	!= diferente
	> mayor que 
	< menor que 
	>= mayor o igual que
	< menor o igual que
```

En este ejemplo podemos ver si el nombre es verdadero o falso, en este caso como el nombre es != (diferente) a Camilo, nos devuelve 'Ese NO es tu nombre':

```
        nombre = 'Juncal'

        if nombre != 'Camilo':
          print('Ese NO es tu nombre')
        elif nombre == 'Camilo':
          print('Ese es tu nombre')
```

Por otro lado los condicionales se pueden utilizar en loops, por ejemplo dentro de un for in, desde donde podemos iterar una colección y verificar si un elemento se encuentra en una lista y conseguir que devuelva un valor específico:

```
        nombre = 'Enrique'
        lista_nombre = ['Jessica', 'Paul', 'George', 'Henry', 'Adán']
        
        presente = False
        
        for personaje in lista_nombre:
            if personaje == nombre:
                presente = True
        
        if presente:
            print('Presente en la lista')
        else:
            print('No presente en la lista')
```

En este ejemplo vemos como primero el for hace una iteración dentro de la lista buscando un nombre en este caso Enrique, tras la iteración y comprobar si se encuentra dicho nombre, el condicional encuentra que el nombre en efecto sí se encuentra, por lo tanto es True, y nos devuelve 'Presente en la lista'.

* * *

#### ¿Cuáles son los diferentes tipos de bucles en Python? ¿Por qué son útiles?

Un bucle en Python es un modo de repetir acciones de forma eficiente y automatizada. Se utiliza para iterar una lista de objetos y podemos hacerlo de dos formas: usando **For** Loops, contando a través de objetos y utilizando **While** Loops, iterando hasta encontrar una condición. Estas estructuras de control nos permiten repetir un bloque de código mientras se cumpla una condición o haya elementos por iterar.

Los For Loops pueden iterar secuencias como listas, tuplas, cadenas o rangos. Nos permiten ejecutar un bloque de código repetidamente por cada elemento en la secuencia. Ej:

```
    numbers = 11
    for number in range(0, numbers):
        print(number)
```

Como se puede apreciar en este ejemplo, el código imprime los números del 0 al 10, utilizando un For Loop que itera sobre el rango de números desde el 0 al numbers-1 (donde numbers es igual a 11).

Utilizamos For cuando sabemos cuantas veces queremos que se repita la iteración o cuando queremos recorrer una colección de datos.

Por otro lado, un While Loop, ejecuta un bloque de código hasta que la condición sea verdadera. Se usa para ejecutar un bloque de sentencias repetidamente hasta que se cumple una condición dada. Cuando la condición se vuelve falsa, se ejecuta la línea inmediatamente posterior al bucle en el programa.  
En el código a continuación, el bucle se ejecuta mientras la condición contador < 3 sea verdadera. Incrementa el contador en 1 en cada iteración e imprime "Mi contador" tres veces.

```
    contador = 0 
    while (contador < 3):
        contador = contador + 1
        print('Mi contador')
```

Un dato importante a tener en cuenta con los While loops son los bucles infinitos. Donde como este tipo de iteraciones se llevan a cabo hasta que una condición se cumpla, en el caso de no cumplirla, la iteración se lleva al infinito, por lo que debemos detenerla manualmente lo cual puede llevarnos a errores importantes. Ej:

```
        while True:
          print('Bucle infinito')
```

Dicho esto podemos decir que usamos While cuando no sabemos cuantas condiciones habrá y la repetición depende de una condición dinámica.

En el uso de iteraciones hay diferentes elementos que podemos utilizar para expresar con más detalles cómo queremos iterar una colección. Esto sería con el uso de **continue**, **break** y **else**.

**Continue** nos permite hacer una iteración y cuando sea cumpla la condición, simplemente sigue iterando. En este ejemplo la iteración continua aun después de encontrar la condición:

```
        for num in range(6):
            if num == 3:
                continue
            print(num)
```

**Break** facilita el detener una iteración en el momento que se encuentra la condición. Ej:

```
        for num in range(10):
            if num == 6:
                break
            print(num)
```

**Else** nos permite devolver un valor si la iteración acaba sin el utilizo de break:

```
        for num in range(100):
            print(num)
        else:
            print('Operation Succesfully Finished')
```

Las iteraciones o loops son útiles porque permiten recorrer colecciones de datos secuencialmente sin cargar todo el conjunto en memoria.

* * *

#### ¿Qué es una lista por comprensión en Python?

Una lista por comprensión es es una forma sencilla y eficaz de crear nuevas listas aplicando una expresión a cada elemento de un iterable existente (como una lista, una tupla o un rango). Ayuda a escribir código limpio, legible y eficiente en comparación con los bucles tradicionales. Ej:

```
    numbers = [3, 64, 12, 4]
    squared_numbers = [val ** 2 for val in numbers]
    print(squared_numbers)
```

Con este ejemplo conseguiríamos una nueva lista con los números de la lista dada primeramente al cuadrado.

Las **listas por comprensión** nos permiten hacer uso de otras operaciones como aplicar condiciones o transformar cadenas. Ej:

```
	numbers = [1,2,3,4,5,6]
	even = [num for num in numbers if num % 2 == 0]
	print(even)

	pets = ['josu', 'olga']
	uppers = [name.upper() for name in pets]
	print(uppers)
```

Con todo estos ejemplos podemos ver que las listas de comprensión nos permiten crear nuevas listas a partir de un iterable en una linea de código, en estos casos combinando un bucle for y/o aplicando una condicion if. 

* * *

#### ¿Qué es un argumento en Python?

Un argumento es un valor que se pasa a una función al llamarla. Puede ser una variable, un valor o un objeto que se pasa como entrada a una función o método.
El uso de argumentos nos permite hacer operaciones de manera más dinámica, donde la función no sabe que argumento va a recibir, pero gracias al uso de parámetros como varibales, es capaz de darnos la posibilidad de elegir el argumento que queramos obteniendo el mismo proceso de operación.
Ej:

```
        def sum(a,b):
          print(a+b)


        sum(1,2)
```

En este ejemplo vemos como sum(1,2) actúa como argumento del parámetro sum(a,b) definido en la función. Los argumentos son flexibles y cambiables, de manera que nos permite cambiar sus valores según lo que necesitemos y la vayamos adaptando.

Nos encontramos con dos tipos de argumentos principales, los **posicionales** y los de **palabra clave**.

Los argumentos posicionales deben incluirse en el orden adecuado, es decir, el primer argumento siempre se enumera primero cuando se llama a la función, el segundo argumento debe llamarse en segundo lugar y así sucesivamente. Ej:

```
        def cats(c1,c2):
          print(c1+c2)

        cats("Josu"," & Olga")
```

Los argumentos de palabra clave son argumentos pasados a una función o método, precedidos por una palabra clave y con el signo igual (=). El orden de un argumento de palabra clave con respecto a otro no importa, ya que los valores se asignan explícitamente. Ej:

```
        def cats(c1, c2)
          print(c1 + c2)

        cats(c1 = 'Josu', c2 = ' & Olga')
```

Mismamente podemos utilizar \*args y \*\*kwargs para permitir que las funciones acepten un número arbitrario de argumentos. Estas características proporcionan gran flexibilidad al diseñar funciones que necesitan gestionar un número variable de entradas.

El siguiente ejemplo muestra cómo \*args recopila múltiples argumentos posicionales en una tupla y cómo \*\*kwargs recopila argumentos de palabras clave en un diccionario.

```
        def nums(*args):
    	  return sum(args)


        print(nums(5, 10, 15))   


        def cats(**kwargs):
    	  for k, val in kwargs.items():
        print(k, val)


        cats(a=1, b=2, c=3)
```

* * *

#### ¿Qué es una función Lambda en Python?

Las funciones Lambda son pequeñas funciones anónimas, lo que significa que no tienen un nombre definido. Se utilizan para operaciones cortas y sencillas. Sólo pueden contener una expresión y devuelven el retorno implícito de esa expresión. Las lambdas son funciones pequeñas y de corta duración que se crean y utilizan de inmediato, principalmente para pasar lógica simple como argumento a otra función. Ej:

```
        a = josu
        upper = lambda x : x.upper()
        print(upper(a))
```

Se utilizan cuando se necesita una función rápida y temporal con el utilizo de sorted() o filter(). En este ejemplo la función lambda nos ordena las tuplas por el segundo valor de cada una de ellas, mientras que en el segundo filtra los números impares. Ej:

```
		numbers = [(4,5), (66,22)]
		sorted_numbers = sorted(numbers, key=lambda x: x[1])
		print(sorted_numbers)

		num_list = [1,2,3,4,5,6,7,8]
		odds = list(filter(lambda x: x % 2 == 1, num_list))
		print(odds)
```


Dichas funciones son una manera más limpia y corta de llevar a cabo funciones dentro de un bloque de código. 

En sus limitaciones podemos decir que no se pueden contener múltiples lineas, usar print como instrucción principal, tener varias expresiones o incluir bucles o condicionales complejos.  

* * *

#### ¿Qué es un paquete pip?

Un paquete pip es una distribución de código Python que incluye uno o más módulos o bibliotecas. Estos paquetes suelen publicarse en el Índice de Paquetes de Python (PyPI) y se pueden instalar fácilmente con pip. Los paquetes de Python pueden contener módulos, subpaquetes y recursos adicionales, como documentación y archivos de datos. 

Pip es el gestior oficial de paquetes de Python y nos permite descargar e instalar códigos creados por otras personas. 

Podemos instalar paquetes adicionales con el comando pip install de Python para el utilizo de dicha biblioteca. Ej:

```
        pip install numpy
```

Gracias a pip podemos añadir funcionalidades extra a Python. Esta librería de externa nos da la posibilidad de descargar paquetes y luego utilizarlos en un proyecto sin la necesidad de programarlas desde cero. En este ejemplo mostraré como utilizar un paquete descargado. Ej:

```
		pip install rquests

		import requests
```

