from scripts import console

# POWER
GIGA = 9
MEGA = 6
KILO = 3
ETTO = 2
DECA = 1
UNIT = 0
DECI = -1
CENTI = -2
MILLI = -3
MICRO = -6
NANO = -9
PICO = -12
FEMTO = -15

prefixes = {
    GIGA : "G",
    MEGA : "M",
    KILO : "k",
    ETTO : "h",
    DECA : "Da",
    UNIT : "",
    DECI : "d",
    CENTI : "c",
    MILLI : "m",
    MICRO : console.mi(),
    NANO : "n",
    PICO : "p",
    FEMTO : "f"
}

def convert_to_power(value:float, current_power:int, power:int):
    """
    Converts a value from its current power to the given power

    Params:
        value (float) : the value to convert
        current_power (int) : the power of ten the value is currently expressed in
        power (int) : the power of ten to convert the value to

    Returns:
        converted_value (float) : the converted value
    """
    return value * (10 ** (current_power - power))

def convert_to_unit(value:float, current_power:int):
    """
    Converts a value from its power to the UNIT power

    Params:
        value (float) : the value to convert
        current_power (int) : the power of ten the value is currently expressed in

    Returns:
        converted_value (float) : the converted value
    """
    return value * (10 ** (current_power - UNIT))

def value_with_unit(value:float, power:int, unitName:str):
    return f"{value} {prefixes[power]}{unitName}"

# length = 1 # mm
# print(conv.value_with_unit(length, conv.MILLI, "m"), "=", conv.value_with_unit(conv.convert_to_unit(pressure, conv.MILLI), conv.UNIT, "m"))