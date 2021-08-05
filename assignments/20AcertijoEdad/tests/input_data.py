# List of tuples
# Each tuple contains a test: the first element are the inputs, the second are the output, and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    (
        # Inputs
        ["2005"],
        # Outputs
        ["Dame el año actual: ", "Tu edad es: 52"],
        # Error message
        " -->a) Revisa los tipos de dato de tus variables. Revisa la prioridad de operadores. Recuerda que estamos trabajando con personas que nacieron antes del año 2000."
    ),
    (
        # Inputs
        ["2030"],
        # Outputs
        ["Dame el año actual: ", "Tu edad es: 65"],
        # Error message
        " -->b) Revisa los tipos de dato de tus variables. Revisa la prioridad de operadores. Recuerda que estamos trabajando con personas que nacieron antes del año 2000."
    ),
     (
        # Inputs
        ["2021"],
        # Outputs
        ["Dame el año actual: ", "Tu edad es: 60"],
        # Error message
        " -->c) Revisa los tipos de dato de tus variables. Revisa la prioridad de operadores. Recuerda que estamos trabajando con personas que nacieron antes del año 2000."
    )
]