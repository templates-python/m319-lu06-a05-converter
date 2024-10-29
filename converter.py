def main():
    units = ['Meter', 'Zentimeter', 'Meilen', 'Seemeilen']
    factors = [1,100,0.000621371,0.000539957]

    print('Einheiten umrechnen')
    for unit in units:
        print(f'* {unit}')
    length = float(input('Länge > '))

    from_unit = -1
    while from_unit == -1:
        unit = input('Von > ')
        if unit in units:
            from_unit = units.index(unit)
        else:
            print('Ungültige Einheit')

    to_unit = -1
    while to_unit == -1:
        unit = input('Nach > ')
        if unit in units:
            to_unit = units.index(unit)
        else:
            print('Ungültige Einheit')

    result = length/factors[from_unit]*factors[to_unit]

    print(f'{length} {units[from_unit]} = {result} {units[to_unit]}')

    return units, factors


if __name__ == '__main__':
    main()
