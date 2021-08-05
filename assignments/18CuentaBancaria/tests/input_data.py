# List of tuples
# Each tuple contains a test: the first element are the inputs, the second are the output, and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    (
        # Inputs
        ["100.1", "57.38", "5.23", "2"],
        # Outputs
        ["Dame el saldo del mes anterior: ", "Dame los ingresos: ", "Dame los egresos: ", "Dame el número de cheques: ", "El saldo final de la cuenta es: 116.78125"],
        # Error message
        " -->a) Revisa los tipos de dato de tus variables. Revisa la prioridad de operadores. Revisa el porcentaje."
    ),
    (
        # Inputs
        ["371.20", "138.45", "283.91", "7"],
        # Outputs
        ["Dame el saldo del mes anterior: ", "Dame los ingresos: ", "Dame los egresos: ", "Dame el número de cheques: ", "El saldo final de la cuenta es: 124.63449999999996"],
        # Error message
        " -->b) Revisa los tipos de dato de tus variables. Revisa la prioridad de operadores. Revisa el porcentaje."
    ),
    (
        # Inputs
        ["100", "0", "0", "0"],
        # Outputs
        ["Dame el saldo del mes anterior: ", "Dame los ingresos: ", "Dame los egresos: ", "Dame el número de cheques: ", "El saldo final de la cuenta es: 92.5"],
        # Error message
        " -->c) Revisa los tipos de dato de tus variables. Revisa la prioridad de operadores. Revisa el porcentaje."
    )
]