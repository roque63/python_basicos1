def main():
    #escribe tu código abajo de esta línea
    #Leer los datos
    mensajes = int(input("Dame el número de mensajes: "))
    megas = float(input("Dame el número de megas: "))
    minutos = int(input("Dame el número de minutos: "))
    #Hacer el cálculo
    costo = 0.8*(mensajes+megas+minutos)
    #Imprime resultado
    print("El costo mensual es:",costo)




if __name__ == '__main__':
    main()
