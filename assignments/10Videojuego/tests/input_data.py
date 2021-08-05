# List of tuples
# Each tuple contains a test: the first element are the inputs, the second are the output, and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    (
        # Inputs
        ["4", "1"],
        # Outputs
        ["Dame la cantidad de juegos nuevos: ", "Dame la cantidad de juegos usados: ", "El total de la compra es: 4350"],
        # Error message
        "Revisa los tipos de dato de tus variables. Revisa la prioridad de operadores."
    ),
    (
        # Inputs
        ["0", "0"],
        # Outputs
        ["Dame la cantidad de juegos nuevos: ", "Dame la cantidad de juegos usados: ", "El total de la compra es: 0"],
        # Error message
        "Revisa los tipos de dato de tus variables. Revisa la prioridad de operadores."
    )
]