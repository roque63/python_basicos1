# List of tuples
# Each tuple contains a test: the first element are the inputs, the second are the output, and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    (
        # Inputs
        ["1998", "2021"],
        # Outputs
        ["Dame el año de nacimiento: ", "Dame el año actual: ", "Los lustros que has vivido son: 4.6"],
        # Error message
        "Revisa los tipos de dato de tus variables. Revisa tus cálculos"
    ),
    (
        # Inputs
        ["2019", "2021"],
        # Outputs
        ["Dame el año de nacimiento: ", "Dame el año actual: ", "Los lustros que has vivido son: 0.4"],
        # Error message
        "Revisa los tipos de dato de tus variables. Revisa tus cálculos"
    ),
    (
        # Inputs
        ["1971", "2021"],
        # Outputs
        ["Dame el año de nacimiento: ", "Dame el año actual: ", "Los lustros que has vivido son: 10.0"],
        # Error message
        "Revisa los tipos de dato de tus variables. Revisa tus cálculos"
    )
]