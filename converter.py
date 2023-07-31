def main():
    units = ['Meter', 'Zentimeter', 'Meilen', 'Seemeilen']
    factors = [1, 100, 0.000621371, 0.000539957]

    print('Einheiten umrechnen')
    for unit in units:
        print(f'* {unit}')

    value = float(input('Länge > '))
    unit_from = -1
    while unit_from == -1:
        unit = input('Einheit von >')
        try:
            unit_from = units.index(unit)
        except ValueError:
            print('Ungültige Einheit')

    unit_to = -1
    while unit_to == -1:
        unit = input('Einheit nach >')
        try:
            unit_to = units.index(unit)
        except ValueError:
            print('Ungültige Einheit')

    result = value * factors[unit_to] / factors[unit_from]
    print(f'{value} {units[unit_from]} = {result} {units[unit_to]}')
    return units, factors


def read_float(prompt):
    """
    reads a floating point number
    :param prompt: the prompt to be shown to the user
    :return: the number entered by the user
    """
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print('Bitte geben Sie eine Zahl ein')


def read_unit(prompt, units_dict):
    """
    reads a valid unit from the user
    :param prompt: the prompt to be shown to the user
    :param units_dict: a dictionary with the valid units as keys
    :return: the unit entered by the user
    """
    show_units(units_dict)
    while True:
        input_unit = input(prompt)
        if input_unit in units_dict:
            return input_unit
        else:
            print('Bitte wählen Sie eine bekannte Einheit aus')


def show_units(units_dict):
    """
    shows the available units
    :param units_dict: a dictionary with the valid units as keys
    :return: None
    """
    print('Verfügbare Einheiten: ', end='')
    for unit in units_dict.keys():
        print(unit, end=', ')
    print()
