import pytest
from warnsystem import units


def test_geschwindigkeit():
    # 36 km/h sind genau 10 m/s
    ergebnis = units.convert(36.0, "km/h", "m/s")
    assert ergebnis == 10.0


def test_celsius_in_kelvin():
    # 0 Grad Celsius sind genau 273.15 Kelvin
    ergebnis = units.convert_temperature(0.0, "°C", "K")
    assert ergebnis == 273.15


def test_falsche_einheit():
    # Bei einer falschen Einheit soll ein Fehler kommen
    with pytest.raises(ValueError):
        units.convert_temperature(10.0, "quatsch", "°C")