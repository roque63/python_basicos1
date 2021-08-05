def main():
    #escribe tu código abajo de esta línea
    palabras = int(input("Dame el número de palabras: "))

    paginas = int(palabras/475)+1

    costo = paginas*60*.9
    
    print("El costo de la publicación es:",costo)



if __name__ == '__main__':
    main()
