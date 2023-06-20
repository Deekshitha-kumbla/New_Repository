def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius/4*9 + 32
    return fahrenheit

def celsius_to_kelvin(celsius):
    K = celsius + 273.15
    return K

def kelvin_to_celsius(kelvin):
    return C = kelvin - 273.15

def kelvin_to_fahrenheir(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)
