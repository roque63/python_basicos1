# List of tuples
# Each tuple contains a test: the first element are the inputs, the second are the output, and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    (
        # Inputs
        ["60", "55", "4"],
        # Outputs
        ["Dame el peso inicial: ", "Dame el peso final: ", "Dame la cantidad de meses: ", "Lo que debes bajar por mes es: 1.25"],
        # Error message
        "Revisa los tipos de dato de tus variables. Revisa la prioridad de operadores."
    ),
    (
        # Inputs
        ["78", "73", "5"],
        # Outputs
        ["Dame el peso inicial: ", "Dame el peso final: ", "Dame la cantidad de meses: ", "Lo que debes bajar por mes es: 1.0"],
        # Error message
        "Revisa los tipos de dato de tus variables. Revisa la prioridad de operadores."
    )
]