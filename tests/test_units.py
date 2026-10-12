"""Tests für Baustein 1. Ausführen mit:  python -m pytest"""
import pytest

from warnsystem import units


@pytest.mark.parametrize(
    "value, original, target, expected",
    [
        (14.0, "°F", "°C", -10.0),
        (-40.0, "°F", "°C", -40.0),
        (100.0, "°C", "°F", 212.0),
        (0.0, "°C", "K", 273.15),
        (0.0, "K", "°C", -273.15),
        (300.0, "K", "°F", 80.33),
    ],
)
def test_convert_temperature(value, original, target, expected):
    assert units.convert_temperature(value, original, target) == pytest.approx(expected, abs=0.01)


@pytest.mark.parametrize("unit", ["K", "°C", "°F"])
def test_same_unit_returns_value(unit):
    assert units.convert_temperature(21.5, unit, unit) == pytest.approx(21.5)


@pytest.mark.parametrize("unit", ["K", "°C", "°F"])
def test_round_trip(unit):
    base = units.to_base(17.3, unit)
    assert units.from_base(base, unit) == pytest.approx(17.3)


def test_other_quantity_is_not_a_temperature():
    with pytest.raises(ValueError):
        units.convert_temperature(1.0, "mm", "°C")


def test_returns_float():
    assert isinstance(units.convert_temperature(20, "°C", "°F"), float)


@pytest.mark.parametrize("original, target", [("°R", "°C"), ("°C", "celsius"), ("", "K")])
def test_unknown_unit_raises(original, target):
    with pytest.raises(ValueError):
        units.convert_temperature(1.0, original, target)


# ---------------------------------------------------------------- Bonus
def _convert_available():
    try:
        units.convert(1.0, "K", "K")
        return True
    except (NotImplementedError, AttributeError):
        return False


bonus = pytest.mark.skipif(not _convert_available(), reason="Bonus: convert() noch nicht implementiert")


@bonus
@pytest.mark.parametrize(
    "value, original, target, expected",
    [
        (10.0, "m/s", "km/h", 36.0),
        (36.0, "km/h", "m/s", 10.0),
        (1.0, "kn", "m/s", 0.5144),
        (20.0, "°C", "°F", 68.0),
    ],
)
def test_convert_bonus(value, original, target, expected):
    assert units.convert(value, original, target) == pytest.approx(expected, abs=0.001)


@bonus
def test_convert_incompatible_quantities_raises():
    with pytest.raises(ValueError):
        units.convert(1.0, "m/s", "°C")
