# Stern-Brocot-tree
Éste ejercicio fué la práctica 7 de mi curso de Modelado y Programación. Es el reto de programación UVa 10077
Los detalles del problema pueden verse [aquí](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1018).
Todo el siguiente bloque de texto es parte del readme que entregué junto a ésta práctica en el que explico como fué que llegue a la solución y una rápida explicación de ésta.

## Introducción
Al resolver ésta práctica mi mayor problema era que no sabía ni siquiera por donde empezar. Trate de encontrar algún complejo patrón entre los números, que cada 'x' fracciones se les sumara 'y' número, o que entre nivel y nivel el número máximo estaba dado por alguna rara ecuación... Pasé por alto lo más obvio entre los patrones: el órden natural. Primero noté que los hijos izquierdos tenían la propiedad de que numerador era siempre más pequeño que el denominador, y en el lado derecho lo contrario. Ya de ahí fué fácil notar que el árbol de Stern-Brocot éra un árbol ordenado, osea, que lo que tenía que hacer era saber si el nodo en el que estaba parado era menor o mayor al nodo al que quería llegar, dependiendo esto tenía que irme a la izquierda o a la derecha. Ahora faltaba implementarlo, el único problema que tuve fue saber como representar el árbol de una forma que me facilitara el construirlo (insertar la fracción entre las dos que tenía que sumar), asi que cuando a mi mente llegó usar una lista de tuplas, sabía que esa era la respuesta, pues podía sumar dependiendo los índices.

## Algoritmo
Empiezo checando los casos triviales: cuando los números no son coprimos
y cuando los números son iguales. Para esto, defino una función que me
da el MCD de dos números, si está función aplicada a los dos números a y
b da un número diferente de 1, no hacemos nada pues esto indica que los
números no son primos relativos. Luego, si a y b son iguales, como primero
checamos que ya eran primos relativos, el único caso posible es que ambos
sean el 1 y este caso es cuando tenemos que parar la ejecución del programa,
asi que regreso una cadena vacía. Ahora, si no entramos a ninguno de estos
dos casos quiere decir que tenemos una fracción a/b en la cual son primos
relativos y diferentes. Construimos una lista de tuplas, en la que cada tupla
representa una fraccion; empezamos con la raíz y los dos números exteriores
que nos ayudan a construir el árbol, definimos también algunas cosas que nos
facilitaran el algoritmo, entre ellas una variable actual que nos dirá el nodo en
el que estamos "parados" en esa iteración, obj la fracción objetivo y i el índice
del nodo actual. Ahora, mientras el nodo obj y actual sean diferentes vamos
a checar cual de los dos es más pequeño, si el obj es menor, tenemos que
irnos hacia la izquierda, asi que añadimos eso a la cadena que regresaremos
al final, redefinimos al actual como la suma del actual y del nodo que este
a la izquierda en la lista. Si actual es menor, entonces escribimos la R en
la cadena que regresaremos al final, aumentamos en 1 nuestro índice i y en
este nuevo índice insertamos el nuevo nodo actual que lo definiremos como
el actual anterior y la obj -ésima posición del nodo (el que está a la derecha).
Al salir de este ciclo, simplemente regresamos la cadena.

## ¿Cómo ejecutar?
Necesitamos el archivo entradaR2.txt pero este ya está en la carpeta archivos
del proyecto. Asi que lo único que hay que hacer es movernos a la carpeta
src/ y ejecutar con python3 el archivo sbtree.py. Después, en la carpeta
archivos se nos debe haber creado un archivo llamado salidaR2.txt en el cual está el resultado
