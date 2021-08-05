# List of tuples
# Each tuple contains a test: the first element are the inputs, the second are the output, and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    (
        # Inputs
        ["1", "1", "1"],
        # Outputs
        ["Dame el número de mensajes: ", "Dame el número de megas: ", "Dame el número de minutos: ", "El costo mensual es: 2.4000000000000004"],
        # Error message
        "Revisa los tipos de dato de tus variables. Revisa la prioridad de operadores."
    ),
    (
        # Inputs
        ["2", "3.2", "5"],
        # Outputs
        ["Dame el número de mensajes: ", "Dame el número de megas: ", "Dame el número de minutos: ", "El costo mensual es: 8.16"],
        # Error message
        "Revisa los tipos de dato de tus variables. Revisa la prioridad de operadores."
    ),
        (
        # Inputs
        ["65", "32.1", "78"],
        # Outputs
        ["Dame el número de mensajes: ", "Dame el número de megas: ", "Dame el número de minutos: ", "El costo mensual es: 140.08"],
        # Error message
        "Revisa los tipos de dato de tus variables. Revisa la prioridad de operadores."
    )
]