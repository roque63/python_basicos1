def main():
    #escribe tu código abajo de esta línea
    num = int(input("Dame un número: "))

    #dígito 1
    d1 = num%10
    
    #dígito 2
    aux = int(num/10)
    # o aux = num//10
    d2 = aux%10

    #dígito 3
    aux = int(aux/10)
    # o aux = aux//10
    d3 = aux%10

    #dígito 4
    d4 = int(aux/10)
    # o aux = aux//10

    pares = 4-(d1%2+d2%2+d3%2+d4%2)
    
    print("El número de dígitos pares es:",pares)



if __name__ == '__main__':
    main()
