![Tec de Monterrey](../../images/logotecmty.png)
# Saldo final de una cuenta bancaria
Básicos-CuentaBancaria

Modifica el programa que se encuentra en la carpeta `src` que se llama `exercise.py` y que contiene el siguiente código:

```python
def main():
    #escribe tu código abajo de esta línea
    pass

if __name__ == '__main__':
    main()
```

La línea `#escribe tu código abajo de esta línea` es un comentario, el programa la va a ignorar al ejecutarse.

Modifica el programa para que haga lo siguiente:

Un banco cobra el 7.5% de interés mensual sobre el saldo final de una cuenta. Además, cada cheque expedido tiene un costo de 13 pesos. Realiza un programa para obtener el saldo mensual de una cuenta en este banco tomando en cuenta el saldo del mes anterior, los ingresos, los egresos y el número de cheques expedidos.

Entradas: 
* Saldo del mes anterior (número decimal)
* Ingresos (número decimal)
* Egresos (número decimal)
* Número de cheques expedidos (número entero) 

Un dato en cada línea en ese orden.

Salida: Un número decimal que represente el saldo final de la cuenta en ese mes.

Ejemplo:
```
Dame el saldo del mes anterior: 100.1
Dame los ingresos: 57.38
Dame los egresos: 5.23
Dame el número de cheques: 2
El saldo final de la cuenta es: 116.78125
```

Una vez que termines tu actividad y la hayas probado con `pytest`, súbela a tu repositorio en GitHub, con el proceso de commit + push.

**Nota:** No te preocupes por esta parte del código `if __name__ == '__main__':` por el momento. No la vamos a necesitar para este programa, pero es una buena práctica incluirla y quedará más claro para qué sirve en los siguientes ejercicios.

[//]: # (Autor: Gil Huesca - ghjuarez at tec.mx)