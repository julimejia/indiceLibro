class pTerminos:
    def __init__(self, nombre):
        self.nombre = nombre
        self.izq = None
        self.der = None
        self.subT = None
        self.pags = None

    def insertarElemento(self, nombre):
        if self:
            if nombre < self.nombre:
                if self.izq is None:
                    self.izq = pTerminos(nombre)
                else:
                    self.izq.insertarElemento(nombre)
            elif nombre > self.nombre:
                if self.der is None:
                    self.der = pTerminos(nombre)
                else:
                    self.der.insertarElemento(nombre)
        else:
            self.nombre = nombre
    
    def buscar(self, nombre):
        if nombre < self.nombre:
            if self.izq is None:
                return self
            return self.izq.buscar(nombre)
        elif nombre > self.nombre:
            if self.der is None:
                return self
            return self.der.buscar(nombre)
        else:
            return str(self.nombre) + ' is found'

class sTerminos:
    def __init__(self, nombre):
        self.nombre = nombre
        self.izq = None
        self.der = None
        self.pags = None
    
    def insertarElemento(self, nombre):
        if self:
            if nombre < self.nombre:
                if self.izq is None:
                    self.izq = sTerminos(nombre)
                else:
                    self.izq.insertarElemento(nombre)
            elif nombre > self.nombre:
                if self.der is None:
                    self.der = sTerminos(nombre)
                else:
                    self.der.insertarElemento(nombre)
        else:
            self.nombre = nombre
    

class numPaginas:
    def __init__(self, numPag):
        self.numPag = numPag
        self.izquierda = None
        self.derecha = None
    
    def insertarElemento(self, numPag):
        if self:
            if numPag < self.numPag:
                if self.izq is None:
                    self.izq = numPaginas(numPag)
                else:
                    self.izq.insertarElemento(numPag)
            elif numPag > self.numPag:
                if self.der is None:
                    self.der = numPaginas(numPag)
                else:
                    self.der.insertarElemento(numPag)
        else:
            self.numPag = numPag

def crearTermino(nombre):
    nuevo = pTerminos(nombre)

def crearsubTermino(nombre):
    nuevo = sTerminos(nombre)

def crearPaginas(numPag):
    nuevo = pTerminos(numPag)




def printTree(node, level = 0):
    if node != None:
        printTree(node.der, level + 1)
        print('  ' * 4 * level + "(" + str(level) + ")" + '-> ' + str(node.nombre))
        printTree(node.izq, level + 1)

def main():
  # Leyendo el archivo
  datos=open("datos.txt", "r")
  texto = datos.readlines()

  root = pTerminos("")
  root1 = pTerminos("")
  #Recorriendo las lineas del archivo
  for numLinea in range(len(texto)):
    #La variable i es el número de la línea 

    cadena = texto[numLinea]

    #Verificamos dónde se halla el primer dígito de la cadena
    digito = 0
    for posInLinea in cadena:
    #La variable j es la posicion dentro de una linea
        if(cadena[digito].isdigit()):
            break
        else:
            digito += 1


    primeraLetra = cadena[0].lower()
    #Dependiendo del término con el que empiece creamos un árbol
    if(primeraLetra == 'm'):
        #Insertarmos el nombre del término principal en un nodo de pTerminos
        nom = cadena[2:digito]
        root.insertarElemento(nom)

        #Creamos el árbol de páginas para ese nodo principal
        prinPags=root.buscar(nom)
        cantPag = int(cadena[digito])
        pagesTree = numPaginas(cantPag)
        prinPags.pags = pagesTree
        
        #Insertamos en varios nodos las páginas de manera organizada
        for i in range(cantPag):
            print("Hola")

    



  printTree(root)
  #mostrarArbol(root)

  datos.close()
main()