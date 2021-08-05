# List of tuples
# Each tuple contains a test: the first element are the inputs, the second are the output, and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    (
        # Inputs
        ["10", "8", "10","8"],
        # Outputs
        ["Calificación de la materia: ", "Calificación de la materia: ", "Calificación de la materia: ", "Calificación de la materia: ", "El promedio es: 9.0"],
        # Error message
        "Revisa los tipos de dato de tus variables. Revisa la prioridad de operadores."
    ),
    (
        # Inputs
        ["7", "8", "9","10"],
        # Outputs
        ["Calificación de la materia: ", "Calificación de la materia: ", "Calificación de la materia: ", "Calificación de la materia: ", "El promedio es: 8.5"],
        # Error message
        "Revisa los tipos de dato de tus variables. Revisa la prioridad de operadores."
    ),
    (
        # Inputs
        ["0", "5", "0","5"],
        # Outputs
        ["Calificación de la materia: ", "Calificación de la materia: ", "Calificación de la materia: ", "Calificación de la materia: ", "El promedio es: 2.5"],
        # Error message
        "Revisa los tipos de dato de tus variables. Revisa la prioridad de operadores."
    )
]