# clase coleccion
class Colecciones:
    # definimos del constructor
    def __init__(self, datos):
        #creacion de atributos de instancia
        self.coleccion = datos

    def obtenerElemento(self):
        ele = self.coleccion[2]


    def getElemento(self, pos):
        if pos < len(self.coleccion):
            return self.coleccion[pos]
        else:
            return -1
    def recorrido(self):
        cad = ''
        for ele in self.coleccion:
            print(ele)
        
        longitud = len(self.coleccion)
        for ind in range(0,longitud):
            print(ind)
        
        for ind,ele in enumerate(self.coleccion):
            print(ind,ele)
        
        for ind in range(0,longitud):
            if ind ==  longitud - 1:
                cad += self.coleccion[ind]
            else:
                cad += self.coleccion[ind]+","
            
        return cad
    
    def diccionario(self):
        dic2 = {}
        for clave, valor in self.coleccion.items():
            print(clave,valor)
            dic2[clave] = valor
        return dic2

    def invertir(self):
        lon = len(self.coleccion)-1 
        lista2 = []
        for  ind in range(lon,-1,-1):
          lista2.append(self.coleccion[ind])
        return lista2

    def listaTupla(self):
        usuarios = ''
        for  ind,usuario  in enumerate(self.coleccion):
            usuarios +='{} '.format(ind+1)
            for dato in usuario:
                usuarios += dato +' '
            usuarios = usuarios+'\n'       
        return usuarios

    def listaDiccionario(self):
        usuarios = 'Diccionario de Usuarios\n'
        for  usuario  in self.coleccion:
            for clave,valor in usuario.items():
                usuarios += '{}=>{} '.format(clave,valor)
            usuarios = usuarios+'\n'       
        return usuarios
    
    def listaComprehension(self):
        lista = [elem for elem in self.coleccion]
        return lista
    
    def diccionarioComprehension(self):
        dicc = { self.coleccion[p][:pos]: self.coleccion[p][pos+1:] for p,elem in enumerate(self.coleccion) for pos,car in enumerate(elem) if car == ':'}
        return dicc

