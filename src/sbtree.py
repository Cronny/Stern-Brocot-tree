def escritura(cadena):
    """Abrimos el archivo de salida y escribimos en el la cadena deseada."""
    salida = open('../archivos/salidaR2.txt', 'w')
    salida.write(cadena)
    salida.close()
    
def mcd(a, b):
    """Máximo Común Divisor de dos números."""
    if b == 0:
        return a
    else:
        return mcd(b, a%b)

def suma(a, b):
    """Suma dos 2-tuplas entrada por entrada."""
    return (a[0] + b[0], a[1] + b[1])

def decimal(a):
    """Dada una 2-tupla 'a', regresamos su valor decimal."""
    return a[0]/a[1]

def steBro(a, b):
    """
    Dada una fracción (a/b) damos su representación en el sistema Stern-Brocot.

    Primero revisamos los casos triviales (números no coprimos o que a=1=b).
    Después, construimos una lista de 2-tuplas, la cuál será la representación de
    nuestro árbol (la tupla de enmedio es la raíz, a la izquierda están sus hijos
    izquierdos y a la derecha los derechos). Ahora, lo que hay que hacer es 
    pararnos en la raíz y verificar si nuestro objetivo (el nodo a/b) es mayor
    o menor que la raíz, dependiendo de esto nos movemos a la izquierda o derecha
    y creamos el elemento que necesitaremos (p.e, si es menor creamos el hijo
    izquierdo de la raíz) y nos paramos en este. Volvemos a hacer la misma 
    verificación que con la raíz hasta que el nodo en el que estemos parados sea
    igual que nuestro objetivo.
    """
    if mcd(a, b) != 1:
        #Si pasa esto, no podemos hacer nada.        
        return "NÚMEROS NO COPRIMOS."
    
    if a == b:
        #El único caso posible es que a y b sean 1. 
        return ""
    
    #El caso interesante:    
    arbol = [(0, 1), (1, 1), (1, 0)] #El árbol.
    cadena = "" #La cadena que regresaremos con L's y R's.
    obj = (a, b) #La dupla que buscamos.
    actual = (1, 1) #La dupla actual.
    i = 1 #Indice auxiliar, lo usaremos para marcar la posición del actual.
    
    #Notemos que el árbol Stern-Brocot es un árbol ordenado, por lo que lo
    #único que haremos será ir recorriendo el árbol, y dependiendo de nuestro
    #nodo actual, si es mayor o menor, sabremos para donde movernos:
    """ Algoritmo"""    
    while decimal(obj) != decimal(actual):
        #Si el número es menor, sumamos nuestro nodo actual con el nodo
        #que tengamos a la izquierda en la representación del árbol,
        #y lo insertamos en la posición en la que estaba el nodo actual.
        if decimal(obj) < decimal(actual):
            cadena += "L"
            actual = suma(actual, arbol[i-1])
            arbol.insert(i, actual)
        else:
            #Si era mayor, lo sumamos con el nodo a la derecha y lo ponemos
            #en esta posición.
             cadena += "R" 
             i = i+1
             actual = suma(actual, arbol[i])
             arbol.insert(i, actual)
    return cadena               

def sbtree():
    """Abrimos, usamos el algoritmo en la entrada y escribimos la salida.."""
    archivo = open('../archivos/entradaR2.txt', 'r')
    salida = ''
    for linea in archivo:
        entradas = linea.split()
        salida += steBro(int(entradas[0]), int(entradas[1])) + "\n"
    archivo.close()
    escritura(salida)

#Ya no más corremos la wea.
sbtree()
