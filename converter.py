def main():
    units = ['Meter', 'Zentimeter', 'Meilen', 'Seemeilen']
    factors = [1, 100, 0.000621371, 0.000539957]

    print('Einheiten umrechnen')
    for unit in units:
        print(f'* {unit}')

    value = float(input('Länge > '))
    unit_from = input('Einheit von: ')
    while not unit_from in units:
        print('Ungültige Einheit')
        unit_from = input('Einheit von: ')

    unit_to = input('Einheit von: ')
    while not unit_to in units:
        print('Ungültige Einheit')
        unit_to = input('Einheit von: ')

    result = value * factors[unit_to] / factors[unit_from]
    print(f'{value} {units[unit_from]} = {result} {units[unit_to]}')
    return units, factors
