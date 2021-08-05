# List of tuples
# Each tuple contains a test: the first element are the inputs, the second are the output, and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    (
        # Inputs
        ["1500"],
        # Outputs
        ["Dame la harina en gramos: ", "Necesitas estos gramos de levadura: 75.0"],
        # Error message
        " -->a) Revisa los tipos de dato de tus variables. Revisa la prioridad de operadores. Recuerda trabajar en gramos."
    ),
    (
        # Inputs
        ["734"],
        # Outputs
        ["Dame la harina en gramos: ", "Necesitas estos gramos de levadura: 36.7"],
        # Error message
        " -->b) Revisa los tipos de dato de tus variables. Revisa la prioridad de operadores. Recuerda trabajar en gramos."
    ),
    (
        # Inputs
        ["234"],
        # Outputs
        ["Dame la harina en gramos: ", "Necesitas estos gramos de levadura: 11.7"],
        # Error message
        " -->c) Revisa los tipos de dato de tus variables. Revisa la prioridad de operadores. Recuerda trabajar en gramos."
    )
]