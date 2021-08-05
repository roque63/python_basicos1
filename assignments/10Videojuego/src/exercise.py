def main():
    #escribe tu código abajo de esta línea
    #Leer los datos
    n = int(input("Dame la cantidad de juegos nuevos: "))
    v = int(input("Dame la cantidad de juegos usados: "))
    #Hacer el cálculo
    resultado = (350 * v) + (1000 * n)
    #Imprimir
    print("El total de la compra es:",resultado)




if __name__ == '__main__':
    main()
