def main():
    #escribe tu código abajo de esta línea
   #Autor: David Cantú
    #Campus: Monterrey
    #Fecha: Agosto 8 de 2019
    #Actividad Prioridad de Operaciones Básicas 

    from math import sqrt
    
    oper1 = 2*(3/4) + 4*(2/3) - 3*(1/5) + 5*(1/2)
    print(round(oper1,4))
    oper2 = 2* sqrt(35**2) + 4*sqrt(36**3) - 6*sqrt(49**2)
    print(round(oper2,4))
    a = 4
    b = 5
    oper3 =(a**3 + 2*b**2) / (4*a) 
    print(round(oper3,4))
    oper4 = (2*(a+b)**2 + 4*(a-b)**2) / (a*b**2)
    print(round(oper4,4))
    oper5 = sqrt((a+b)**2 + 2**(a+b)) / (2*a +2*b)**2
    print(round(oper5,4))




if __name__ == '__main__':
    main()
