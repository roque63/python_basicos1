# List of tuples
# Each tuple contains a test: the first element are the inputs, the second are the output, and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    (
        # Inputs
        ["1", "2", "3","4"],
        # Outputs
        ["Dame x1: ", "Dame y1: ", "Dame x2: ", "Dame y2: ","Pendiente: 1.0"],
        # Error message
        "Revisa los tipos de dato de tus variables. Revisa el orden en el que se capturan los datos."
    ),
    (
        # Inputs
        ["10.5", "7.2", "-1.5","4"],
        # Outputs
        ["Dame x1: ", "Dame y1: ", "Dame x2: ", "Dame y2: ","Pendiente: 0.26666666666666666"],
        # Error message
        "Revisa los tipos de dato de tus variables. Revisa el orden en el que se capturan los datos."
    ),
    (
        # Inputs
        ["3.4", "-1.3", "8.4","2.5"],
        # Outputs
        ["Dame x1: ", "Dame y1: ", "Dame x2: ", "Dame y2: ","Pendiente: 0.76"],
        # Error message
        "Revisa los tipos de dato de tus variables. Revisa el orden en el que se capturan los datos."
    )
]