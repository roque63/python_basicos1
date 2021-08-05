def main():
    #escribe tu código abajo de esta línea
    saldoAnterior = float(input("Dame el saldo del mes anterior: "))
    ingresos = float(input("Dame los ingresos: "))
    egresos = float(input("Dame los egresos: "))
    cheques = int(input("Dame el número de cheques: "))
    saldoFinal = (saldoAnterior+ingresos-egresos-cheques*13)*(1-7.5/100)
    print("El saldo final de la cuenta es:",saldoFinal)



if __name__ == '__main__':
    main()
