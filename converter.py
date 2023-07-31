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
