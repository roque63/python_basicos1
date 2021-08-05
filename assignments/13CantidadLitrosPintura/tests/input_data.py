# List of tuples
# Each tuple contains a test: the first element are the inputs, the second are the output, and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    (
        # Inputs
        ["857.5","10"],
        # Outputs
        ["Area a pintar en metros: ", "Rendimiento (m2/l): ", "Litros a comprar: 86"],
        # Error message
        "Revisa los tipos de dato de tus variables. Revisa el operador adecuado. El resultado debe ser un entero porque compras litros completos"
    ),
    (
        # Inputs
        ["10", "10"],
        # Outputs
        ["Area a pintar en metros: ", "Rendimiento (m2/l): ", "Litros a comprar: 1"],
        # Error message
        "Cuida los mensajes al usuario que se te solicitaron. Revisa los tipos de dato de tus variables. Revisa el operador adecuado. El resultado debe ser un entero porque compras litros completos"
    )]