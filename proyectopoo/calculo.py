class Calculos:
    def __init__(self, numero):
        self.numero = numero
 
    def divisores(self):
        lista = [num for num in range(1,self.numero,1) if self.numero % num ==0 ]
        return  lista

    def paresEimpares(self):
        dicc ={'pares':[],'impares':[]}
        for num in range(self.numero):
            if num % 2 == 0:
                dicc['pares'].append(num)
            else:
                dicc['impares'].append(num)
        return dicc

    def fibonacci(self):
        lista = []
        fib, suc = 0,1
        for i in range(self.numero):
            lista.append(fib)
            fib, suc = suc, fib + suc
        return lista
    
    def esPrimo(self):
        cont=0
        for n in range(1,self.numero+1):
            if self.numero % n == 0:
                cont +=1
        return cont == 2 
    
    def primos(self):
        lista = []
        for num in range(self.numero):
            c = Calculos(num)
            if c.esPrimo():
                lista.append(num)
        return lista
    def binarioAdecimal(self):
        decimal = 0
        for pos,num in enumerate(self.numero[::-1]):
            num= int(num)
            decimal += (2**pos)*num
        return decimal

    def decimalAbinario(self):
        cad=''
        num = self.numero
        while (num != 0):
            cad+= str(num%2)
            num = num//2
        return cad[::-1]

    def primosGemelos(self,num1,num2):
        cal1 = Calculos(num1)
        cal2 = Calculos(num2)
        if cal1.esPrimo() and cal2.esPrimo() and  num1 %2 != 0 and num2 % 2 != 0:
            return (num1-2 == num2 and num2 + 2 ==num1) or (num1+2 == num2 and num2 - 2 ==num1)
        return False
    
    def invertir(self):
        num=self.numero
        x=0
        lon=len(str(num))
        for i in range(lon):
            mod=num%10
            num=num//10
            x=x*10+mod
        return x

    def esPerfecto(self):
        suma = 0
        for i in range(1,self.numero):
            if (self.numero % i == 0):
                suma += i
        return self.numero == suma
        
    def sonAmigos(self,num1,num2):
        cal1 =  Calculos(num1)
        cal2 =  Calculos(num2)
        suma_cal1= sum(cal1.divisores())
        suma_cal2= sum(cal2.divisores())
        return suma_cal1 == num2 and suma_cal2 == num1

        



















