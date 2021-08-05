import math
def main():
    #escribe tu código abajo de esta línea


    mts=float(input("Area a pintar en metros: "))
    rendimiento=float(input("Rendimiento (m2/l): "))
    litros=math.ceil(mts / rendimiento)
    print(litros)


if __name__ == '__main__':
    main()
