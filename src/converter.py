# Absolute zero in Celsius
ABSOLUTE_ZERO_C = -273.15


def celsius_to_fahrenheit(c: float) -> float:
    """
    Converts from Celsius to Fahrenheit.
    """
    return (c * 9/5) + 32


def fahrenheit_to_celsius(f: float) -> float:
    """
    Converts from Fahrenheit to Celsius.
    """
    return (f - 32) * (5/9)


def celsius_to_kelvin(c: float) -> float:
    """
    Converts from Celsius to Kelvin.
    """
    if c < ABSOLUTE_ZERO_C:
        raise ValueError("below absolute zero")
    return c + 273.15


def kelvin_to_celsius(k: float) -> float:
    """
    Converts from Kelvin to Celsius.
    """
    if k < 0:
        raise ValueError("kelvin cannot be negative")
    return k - 273.15


def convert(value: float, from_unit: str, to_unit: str) -> float:
    """Convert a temperature between any supported units.

    Units: 'C' (Celsius), 'F' (Fahrenheit), 'K' (Kelvin)
    Raises: ValueError for unknown units or invalid temperatures.

    Examples:
        convert(100, 'C', 'F')  →  212.0
        convert(32,  'F', 'C')  →  0.0
        convert(0,   'C', 'K')  →  273.15
    """
    # Normalize to uppercase so 'c' and 'C' both work
    from_unit = from_unit.upper()
    to_unit = to_unit.upper()

    # Check input for correct letters
    if not (from_unit == 'C' or from_unit == 'F' or from_unit == 'K'): 
        raise ValueError("invalid unit")
    if not (to_unit == 'C' or to_unit == 'F' or to_unit == 'K'): 
        raise ValueError("invalid unit") 


    # If same unit, return as-is
    if from_unit == to_unit:
        return float(value)

    if from_unit == 'C':
        if to_unit == 'F':
            return celsius_to_fahrenheit(value)
        else:
            return celsius_to_kelvin(value)
    elif from_unit == 'F':
        if to_unit == 'K':
            return celsius_to_kelvin(fahrenheit_to_celsius(value))
        else:
            return fahrenheit_to_celsius(value)
    else:
        if to_unit == 'C':
            return kelvin_to_celsius(value)
        else:
            celsius_to_fahrenheit(kelvin_to_celsius(value))
