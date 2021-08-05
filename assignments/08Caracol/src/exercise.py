def main():
    #escribe tu código abajo de esta línea
    minutos = float(input("Dame los minutos: "))

    segundos = minutos * 60
    milimetros = segundos*5.7
    cm = milimetros/10

    print("Centímentros recorridos:",cm)


if __name__ == '__main__':
    main()
