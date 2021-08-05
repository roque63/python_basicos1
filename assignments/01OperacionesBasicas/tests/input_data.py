# List of tuples
# Each tuple contains a test: the first element are the inputs, the second are the output, and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    (
        # Inputs
        ["10", "20"],
        # Outputs
        ["Dame un número: ", "Dame un número: ", "Suma: 30", "Resta: -10","Multiplicación: 200"],
        # Error message
        "Revisa los acentos. Revisa la prioridad de operadores."
    ),
    (
        # Inputs
        ["5", "4"],
        # Outputs
        ["Dame un número: ", "Dame un número: ", "Suma: 9", "Resta: 1","Multiplicación: 20"],
        # Error message
        "Revisa los acentos. Revisa la prioridad de operadores."
    ),
    (
        # Inputs
        ["8", "5"],
        # Outputs
        ["Dame un número: ", "Dame un número: ", "Suma: 13", "Resta: 3","Multiplicación: 40"],
        # Error message
        "Revisa los acentos. Revisa la prioridad de operadores."
    )
]