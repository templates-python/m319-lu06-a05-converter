from converter import main
import pytest

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
    """Testet die Einheiten-Umwandlungsfunktion und ignoriert Fließkommazahlen-Ungenauigkeit."""
    inputs = iter([43.5, 'Meter', 'Seemeilen'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()
    captured = capsys.readouterr()

    expected_prefix = 'Einheiten umrechnen\n* Meter\n* Zentimeter\n* Meilen\n* Seemeilen\n43.5 Meter = '
    expected_suffix = ' Seemeilen\n'

    # Extrahieren Sie den Fließkommawert aus dem erfassten Output
    float_str = captured.out[len(expected_prefix):-len(expected_suffix)].strip()
    captured_float = float(float_str)

    expected_float = 0.0234881295


    # Überprüfen Sie den Fließkommawert mit pytest.approx
    assert captured_float == pytest.approx(expected_float, rel=1e-9)

    # Überprüfen Sie den Rest des Strings
    assert captured.out.startswith(expected_prefix)
    assert captured.out.endswith(expected_suffix)


def test_convert2(capsys, monkeypatch):
    """Testet die Einheiten-Umwandlungsfunktion und ignoriert Fließkommazahlen-Ungenauigkeit."""
    inputs = iter([0.375, 'Meilen', 'Zentimeter'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()
    captured = capsys.readouterr()

    expected_prefix = 'Einheiten umrechnen\n* Meter\n* Zentimeter\n* Meilen\n* Seemeilen\n0.375 Meilen = '
    expected_suffix = ' Zentimeter\n'

    # Extrahieren Sie den Fließkommawert aus dem erfassten Output
    float_str = captured.out[len(expected_prefix):-len(expected_suffix)].strip()
    captured_float = float(float_str)

    expected_float = 60350.41867097112

    # Überprüfen Sie den Fließkommawert mit pytest.approx
    assert captured_float == pytest.approx(expected_float, rel=1e-9)

    # Überprüfen Sie den Rest des Strings
    assert captured.out.startswith(expected_prefix)
    assert captured.out.endswith(expected_suffix)