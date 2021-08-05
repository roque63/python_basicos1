def main():
    #escribe tu código abajo de esta línea
    inicial = float(input("Dame el peso inicial: "))
    final = float(input("Dame el peso final: "))
    meses = int(input("Dame la cantidad de meses: "))
    kilos = (inicial-final)/meses
    print("Lo que debes bajar por mes es:",kilos)



if __name__ == '__main__':
    main()
