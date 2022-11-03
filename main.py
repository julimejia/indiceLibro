class pTerminos:
    def __init__(self, nombre):
        self.nombre = nombre
        self.izq = None
        self.der = None
        self.subT = sTerminos("")
        self.pags = numPaginas("")

    def insertarPaginas(self,nodo, listapagina): #metodo para insertar las paginas una vez creado el nodo
        for i in listapagina:
            nodo.pags.insertarPag(i)

    def insertarElemento(self, nombre,valores):
        if self:
            if self.nombre == "":
               self.nombre = nombre
               self.insertarPaginas(self, valores) 
            elif nombre < self.nombre:
                if self.izq is None:
                    self.izq = pTerminos(nombre)
                    self.insertarPaginas(self.izq, valores)
                else:
                    self.izq.insertarElemento(nombre)
            elif nombre > self.nombre:
                if self.der is None:
                    self.der = pTerminos(nombre)
                    self.insertarPaginas(self.der, valores)
                else:
                    self.der.insertarElemento(nombre)
        else:
            self.nombre = nombre
            self.insertarPaginas(self.der, valores)
            
            
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
        self.nombre = numPag
        self.izq = None
        self.der = None
    
    def insertarPag(self, numPag):
        if self:
            if numPag < self.nombre:
                if self.izq is None:
                    self.izq = numPaginas(numPag)
                else:
                    self.izq.insertarPag(numPag)
            elif numPag > self.nombre:
                if self.der is None:
                    self.der = numPaginas(numPag)
                else:
                    self.der.insertarPag(numPag)
        else:
            self.nombre = numPag


def separarDigitos(lineaPaginas,digitos):
        act = int(digitos)
        next1 = act + 2
        digitos= []
        for digitosPag in range(act,len(lineaPaginas),2):
            digitos.append(lineaPaginas[act:next1])
            act += 2
            next1 += 2
        
        return digitos

def walk(x):
    print(x.nombre)
    if x!=None:
        walk(x.izq)
        print(x.nombre)
        walk(x.der)
#def printTree(node):
  
def digito(cadena):
    digito = 0
    for i in cadena:
        if(cadena[digito].isdigit()):
            break
        else: 
            digito += 1
    return digito

def main():
    
    root = pTerminos("")
    while True:
        a = input()
        if a[0] == "m":
            digit = digito(a)
            lista_pag = separarDigitos(a,digit)
            root.insertarElemento(a[2:digit],lista_pag)
        else:
                break
  

    print(walk(root.pags)) 
main()  