from converter import main


def test_lists(capsys, monkeypatch):
    inputs = iter([0, 'Meter', 'Seemeilen'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    units, factors = main()
    assert units == list(('Meter', 'Zentimeter', 'Meilen', 'Seemeilen'))
    assert factors == list((1, 100, 0.000621371, 0.000539957))


def test_inout(capsys, monkeypatch):
    inputs = iter([0, 'Meter', 'Seemeilen'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    units, factors = main()
    captured = capsys.readouterr()
    assert captured.out == 'Einheiten umrechnen\n* Meter\n* Zentimeter\n* Meilen\n* Seemeilen\n0.0 Meter = 0.0 Seemeilen\n'

def test_invalid_units(capsys, monkeypatch):
    inputs = iter([0, 'Zehen', 'Meilen', 'a', 'blubb', 'Seemeilen'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    units, factors = main()
    captured = capsys.readouterr()
    assert captured.out == 'Einheiten umrechnen\n* Meter\n* Zentimeter\n* Meilen\n* Seemeilen\nUngültige Einheit\nUngültige Einheit\nUngültige Einheit\n0.0 Meilen = 0.0 Seemeilen\n'



def test_convert1(capsys, monkeypatch):
    inputs = iter([43.5, 'Meter', 'Seemeilen'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    units, factors = main()
    captured = capsys.readouterr()
    assert captured.out == 'Einheiten umrechnen\n* Meter\n* Zentimeter\n* Meilen\n* Seemeilen\n43.5 Meter = 0.0234881295 Seemeilen\n'



def test_convert2(capsys, monkeypatch):
    inputs = iter([0.375, 'Meilen', 'Zentimeter'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    units, factors = main()
    captured = capsys.readouterr()
    assert captured.out == 'Einheiten umrechnen\n* Meter\n* Zentimeter\n* Meilen\n* Seemeilen\n0.375 Meilen = 60350.41867097112 Zentimeter\n'

