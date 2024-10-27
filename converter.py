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

    unit_to = input('Einheit zu: ')
    while not unit_to in units:
        print('Ungültige Einheit')
        unit_to = input('Einheit zu: ')

    result = value * factors[units.index(unit_to)] / factors[units.index(unit_from)]
    print(f'{value} {units[units.index(unit_from)]} = {result} {units[units.index(unit_to)]}')
    return units, factors

if __name__ == '__main__':
    main()
