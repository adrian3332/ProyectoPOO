# import flask
from flask import Flask
# para renderizar las paginas html
from flask import render_template
# para capturar lo datos del html
from flask import request  #"request" is not accessed
# importar clase de usuarios
from coleccion import Colecciones
from calculo import  Calculos
from cadena import Cadena,SubCadena

# instancia de flask con el nombre del  modulo

app = Flask(__name__)
#Instancias
# configuraciod de rutas o urls
# route (nombre url y el metodo(opcional))
@app.route('/')
def inicio():
    # return 'Mi p'
    return render_template("index.html")  

@app.route('/coleccion',  methods=['GET','POST'])
def coleccion():
    opcion,valor1,valor2,resp = '0','','',''
    if request.method == 'POST':
        opcion = request.form['select']
        valor1 = request.form['valor1']
        valor2 = request.form['valor2']
        if opcion == '1':
            lista = valor1.split()
            col =Colecciones(lista)
            if  col.getElemento(int(valor2)) != -1 :
                resp = col.getElemento(int(valor2))
            else:
                resp = 'No existe elemento en esa posicion'
        
        elif opcion == '2':
            tupla= tuple(valor1.split())
            col =Colecciones(tupla)
            resp = 'Tupla('+col.recorrido()+')'
        
        elif opcion == '3':
            lista=valor1.split()
            col =Colecciones(lista)
            resp = '['+col.recorrido()+']'

        elif opcion == '4':
            lista= valor1.split(',')
            dic ={}
            for item in lista:
                pos= item.find(":")
                clave = item[:pos]
                valor = item[pos+1:]
                dic[clave] = valor
            col = Colecciones(dic)
            resp = col.diccionario()

        elif opcion == '5':
            lista=valor1.split()
            col = Colecciones(lista)
            resp = col.invertir()

        elif opcion == '6':
            usuarios = [('Daniel','123'),('Yady','456'),('Erick','xyz')]
            col = Colecciones(usuarios)
            resp = col.listaTupla()
        elif opcion == '7':
            usuarios = [
                {'nombre':'Daniel','clave':'123'},
                {'nombre':'Yady','clave':'456'},
                {'nombre':'Erick','clave':'xyz'}
                ]
            col = Colecciones(usuarios)
            resp = col.listaDiccionario()
            
        elif opcion == '8':
            lista=valor1.split()
            col =Colecciones(lista)
            resp =  col.listaComprehension()

        elif opcion == '9':
            lista=valor1.split(',')
            col =Colecciones(lista)
            resp =  col.diccionarioComprehension()


    return render_template("colecciones.html",seleccion =opcion, n1=valor1,n2=valor2,respuesta=resp )  

@app.route('/calculo' , methods=['GET','POST'])
def calculo():
    opcion,valor1,valor2,resp = '0','','',''
    if request.method == 'POST':
        opcion = request.form['select']
        valor1 = request.form['valor1']
        valor2 = request.form['valor2']
        if opcion == '1':
            calculo  = Calculos(int(valor1))
            resp = calculo.divisores()

        if opcion == '2':
            calculo  = Calculos(int(valor1))
            resp = calculo.paresEimpares()

        if opcion == '3':
            calculo  = Calculos(int(valor1))
            resp = calculo.fibonacci()

        if opcion == '4':
            calculo  = Calculos(int(valor1))
            if calculo.esPrimo():
                resp = 'El numero {} Si es primo'.format(valor1)
            else:
                resp = 'El numero {} No es primo'.format(valor1)

        if opcion == '5':
            calculo  = Calculos(int(valor1))
            resp = calculo.primos()

        if opcion == '6':
            calculo  = Calculos(0)
            if calculo.primosGemelos(int(valor1),int(valor2)):
                resp = '({},{}) Son Primos Gemelos'.format(valor1,valor2)
            else:
                resp = '({},{}) No Son Primos Gemelos'.format(valor1,valor2)

        if opcion == '7':
            calculo  = Calculos(int(valor1))
            if calculo.esPerfecto():
                resp = 'El numero {} Si es perfecto'.format(valor1)
            else:
                resp = 'El numero {} No es perfecto'.format(valor1)

        if opcion == '8':
            calculo  = Calculos(0)
            if calculo.sonAmigos(int(valor1),int(valor2)):
                resp = '({},{}) Son Amigos'.format(valor1,valor2)
            else:
                resp = '({},{}) No Son Amigos'.format(valor1,valor2)
                
        if opcion == '9':
            calculo  = Calculos(int(valor1))
            resp = calculo.invertir()

        if opcion == '10':
            calculo  = Calculos(valor1)
            resp = calculo.binarioAdecimal()

        if opcion == '11':
            calculo  = Calculos(int(valor1))
            resp = calculo.decimalAbinario()


    return render_template("calculo.html",seleccion =opcion, n1=valor1,n2=valor2,respuesta=resp)  

@app.route('/cadena', methods=['GET','POST'])
def cadena():
    opcion,valor1,valor2,valor3,resp = '0','','','',''
    if request.method == 'POST':
        opcion = request.form['select']
        valor1 = request.form['valor1']
        valor2 = request.form['valor2']
        valor3 = request.form['valor3']
        if opcion == '1':
            cadena  = Cadena(valor1)
            resp = cadena.recorrer()

        if opcion == '2':
            cadena  = Cadena(valor1)
            resp = cadena.invertir()

        if opcion == '3':
            cadena  = Cadena(valor1)
            enc = cadena.buscarCaracter(valor2) 
            resp ='el caracter esta en la posicion {}'.format(enc) if enc != -1 else 'Caracter No encontrado'
        
        if opcion == '4':
            cadena  = Cadena(valor1)
            resp = cadena.buscarVocales()

        if opcion == '5':
            cadena  = Cadena(valor1)
            enc = cadena.buscarCaracteres(valor2) 
            resp ='el caracter esta en las posiciones {}'.format(enc) if enc  else 'Ninguna Ocurrencia encontrada'
        
        if opcion == '6':
            cadena  = Cadena(valor1)
            resp = cadena.cancatenar(valor2)

        if opcion == '7':
            cadena  = Cadena(valor1)
            resp = cadena.reemplazarCaracter(valor2,valor3)
        if opcion == '8':
            cadena = '1,2,3,4,5,677,90,6' if not valor1 else valor1 
            lista = [int(car)for car in cadena.split(',')]
            resp = 'Lista creada: {}'.format(lista)

        if opcion == '9':
            lista  = ["hola","tal",",Como estas"]
            cadena =''
            for elem in lista:
                cadena += elem+' '
            resp = 'Lista {}\ncadena creada: {}'.format(lista,cadena)

        if opcion == '10':
            subcadena  = SubCadena(valor1)
            enc = subcadena.buscarPalabras(valor2)
            print(enc)
            resp ='La Subcadena se encuentra en las posiciones {}'.format(enc) if enc  else 'No se encontro la Subcadena'

        if opcion == '11':
            subcadena  = SubCadena(valor1)
            resp = subcadena.insertarPalabra(valor2)

        if opcion == '12':
            subcadena  = SubCadena(valor1)
            resp = subcadena.eliminarPalabra(valor2)

        if opcion == '13':
            calculo  = Calculos(valor1)
            resp = calculo.binarioAdecimal()

        if opcion == '14':
            calculo  = Calculos(int(valor1))
            resp = calculo.decimalAbinario()

    return render_template("cadena.html",seleccion =opcion, n1=valor1,n2=valor2,n3=valor3,respuesta=resp)  

@app.route('/ayuda')
def ayuda():
    return render_template("ayuda.html")  


if __name__ == '__main__':
    app.run(port=3090,debug=True)