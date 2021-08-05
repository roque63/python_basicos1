# List of tuples
# Each tuple contains a test: the first element are the inputs, the second are the output, and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    (
        # Inputs
        ["105", "2021"],
        # Outputs
        ["Dame tu edad: ", "Dame el año actual: ", "Cumplirás 100 años en el año: 2016"],
        # Error message
        "Revisa los tipos de dato de tus variables. Revisa tus cálculos."
    ),
    (
        # Inputs
        ["0", "2000"],
        # Outputs
        ["Dame tu edad: ", "Dame el año actual: ", "Cumplirás 100 años en el año: 2100"],
        # Error message
        "Revisa los tipos de dato de tus variables. Revisa tus cálculos."
    )
]