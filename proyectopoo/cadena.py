class Cadena:
    
    def __init__(self,cad=""):
        self.__cadena = cad

    @property
    def cadena(self):
        return self.__cadena
        
    @cadena.setter
    def cadena(self, cad=""):
        self.__cadena =cad

    @property
    def longitud(self):
        self.__longitud =0        
        for i in self.__cadena:
            self.__longitud +=1
        return self.__longitud
    
    def recorrer(self):
        nueva_cadena = ""
        for car in self.cadena:
            nueva_cadena += car + "\n"
        return nueva_cadena

    def invertir(self):
        lon = len(self.cadena)-1 
        nueva_cadena = ''
        for  ind in range(lon,-1,-1):
            nueva_cadena +=self.cadena[ind]
        return nueva_cadena

    def buscarCaracter(self,caracter):
        pos =-1
        for ind,car in enumerate(self.cadena):
            if  car == caracter:
                pos=ind
                break
        return pos

    def buscarCaracteres(self,caracter):
        posiciones =[]
        for ind,car in enumerate(self.cadena):
            if  car == caracter:
                posiciones.append(ind)
        return posiciones

    def cancatenar(self,cadena2):
        return self.cadena + cadena2
             
    def buscarVocales(self):
        nueva_cadena=""
        for car in self.cadena:
            if  car in "AEIOUaeiou":
                nueva_cadena += car
        return nueva_cadena     
        
    def reemplazarCaracter(self,caracter_viejo,caracter_nuevo):
        nueva_cadena = ''
        for  car in self.cadena:
            if car == caracter_viejo:
                nueva_cadena += caracter_nuevo
            else:
                nueva_cadena +=car
        return nueva_cadena
    def crearLista(self):
        pass
    def mostrarCadena(self):
        print(self.__cadena)
    
class SubCadena(Cadena):
    
    def __init__(self, cad):
        super().__init__(cad=cad)
    
    #Devuelve la primera posicion de la palabra encontrada
    def  buscarPalabra(self, subcadena):
        posicion = -1
        for i in range(self.longitud):
            if  self.cadena[i:i+len(subcadena)] == subcadena:
                posicion = i 
                break
        return posicion
    #Devuelve la primera varias posiciones de la palabra encontrada
    def buscarPalabras(self, subcadena):
        lista=[]
        for i in range(self.longitud):
            if  self.cadena[i:i+len(subcadena)] == subcadena:
                lista.append(i)
        return lista
    #Eliminar palabra un palabra de la frase
    def eliminarPalabra(self,subcadena):
        nueva_cadena=''
        cont=0
        while(cont < self.longitud):
            if self.cadena[cont:cont+len(subcadena)] ==  subcadena:
                cont += len(subcadena)-1
            else:
                nueva_cadena += self.cadena[cont]
            cont +=1
        return nueva_cadena
           
    #Extrae digitos de una  frase en un dicionario con clave los digitos y valor es cntidad de digitos 
    def extraerDigitos(self):
        digitos= ('0','1','2','3','4','5','6','7','8','9')
        clave = ''
        valor=0
        for caracter in self.cadena:
            if caracter in digitos:
                clave += caracter
                valor += 1
        return {clave:valor}

    #Inserta una palabra a la frase	
    def insertarPalabra(self,subcadena):
        nueva_cadena = ''
        bandera = True
        cont=0
        while(cont<self.longitud):
            if self.cadena[cont:cont+len(subcadena)] == subcadena and bandera == True:
                nueva_cadena += self.cadena[cont:cont+len(subcadena)]+' '+subcadena
                cont+=len(subcadena)-1
                bandera =False
            else:
                nueva_cadena +=self.cadena[cont] 
            cont +=1
        return  nueva_cadena
    #Extrae  caracteres Especiales
    def extraerEsp(self):
        carac_especiales=('€','¥','^','°','=','{','}','[',']','%','>''ç','.','|','^','º','ª','¬','´','`',"'",'"','€',',','@','#','$','_','&','-','+','(',')','/','*',':',';','!','?','¡','¿','‽','•','√','π','÷','×','¶','∆','£','¢','<')
        clave = ''
        valor = 0
        for caracter in self.cadena:
            if caracter in carac_especiales:
                clave += caracter
                valor +=1
        return {clave:valor}
cad =SubCadena('Iniciando.....')
print(cad.insertarPalabra('que'))