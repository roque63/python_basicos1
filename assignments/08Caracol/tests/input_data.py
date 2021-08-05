# List of tuples
# Each tuple contains a test: the first element are the inputs, the second are the output, and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    (
        # Inputs
        ["3"],
        # Outputs
        ["Dame los minutos: ", "Centímentros recorridos: 102.6"],
        # Error message
        "Revisa los tipos de dato de tus variables. Revisa los cálculos, recuerda que hay que convertir a centímetros por minuto."
    ),
    (
        # Inputs
        ["1.5"],
        # Outputs
        ["Dame los minutos: ", "Centímentros recorridos: 51.3"],
        # Error message
        "Revisa los tipos de dato de tus variables. Revisa los cálculos, recuerda que hay que convertir a centímetros por minuto."
    ),
    (
        # Inputs
        ["33"],
        # Outputs
        ["Dame los minutos: ", "Centímentros recorridos: 1128.6"],
        # Error message
        "Revisa los tipos de dato de tus variables. Revisa los cálculos, recuerda que hay que convertir a centímetros por minuto."
    )
]