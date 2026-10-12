# """Baustein 1 des Kursprojekts: Umrechnung von Maßeinheiten.

# Jede Einheit wird über eine lineare Funktion  basis = k * wert + d  in die
# Basiseinheit ihrer Größe umgerechnet (Temperatur: Kelvin, Geschwindigkeit: m/s, Länge: mm).
# Umrechnung von A nach B: A -> Basiseinheit -> B.
# """

# # Einheit -> (Größe, k, d), sodass gilt: basis = k * wert + d
# conversions = {
#     "K": ("temperature", 1.0, 0.0),
#     "°C": ("temperature", 1.0, 273.15),
#     # TODO: "°F" ergänzen
#     # Bonus: "m/s", "km/h", "kn"
#     "mm": ("length", 1.0, 0.0),
#     "inch": ("length", 25.4, 0.0),
#     "%": ("ratio", 1.0, 0.0),
# }


# def _lookup(unit):
#     """Liefert (Größe, k, d) einer Einheit. Unbekannte Einheiten führen zu einem ValueError."""
#     # TODO
#     raise NotImplementedError


# def quantity(unit):
#     """Liefert die Größe einer Einheit, z.B. "temperature"."""
#     # TODO
#     raise NotImplementedError


# def to_base(value, unit):
#     """Rechnet value von unit in die Basiseinheit der Größe um."""
#     # TODO
#     raise NotImplementedError


# def from_base(value, unit):
#     """Rechnet value von der Basiseinheit in unit um (Umkehrfunktion von to_base)."""
#     # TODO
#     raise NotImplementedError


# def convert(value, original_unit, target_unit):
#     """Rechnet value von original_unit in target_unit um (beliebige Größe)."""
#     # Bonus
#     raise NotImplementedError


# def convert_temperature(value, original_unit, target_unit):
#     """Rechnet eine Temperatur von original_unit in target_unit um.

#     >>> convert_temperature(14.0, "°F", "°C")
#     -10.0
#     """
#     # TODO
#     raise NotImplementedError

"""Baustein 1 des Kursprojekts: Umrechnung von Maßeinheiten.

Jede Einheit wird über eine lineare Funktion  basis = k * wert + d  in die
Basiseinheit ihrer Größe umgerechnet (Temperatur: Kelvin, Geschwindigkeit: m/s, Länge: mm).
Umrechnung von A nach B: A -> Basiseinheit -> B.
"""

# Einheit -> (Größe, k, d), sodass gilt: basis = k * wert + d
conversions = {
    "K": ("temperature", 1.0, 0.0),
    "°C": ("temperature", 1.0, 273.15),
    "°F": ("temperature", 5 / 9, 273.15 - 32 * (5 / 9)),
    "m/s": ("speed", 1.0, 0.0),
    "km/h": ("speed", 1 / 3.6, 0.0),
    "kn": ("speed", 0.5144, 0.0),
    "mm": ("length", 1.0, 0.0),
    "inch": ("length", 25.4, 0.0),
    "%": ("ratio", 1.0, 0.0),
}


def _lookup(unit):
    """Liefert (Größe, k, d) einer Einheit. Unbekannte Einheiten führen zu einem ValueError."""
    if unit not in conversions:
        raise ValueError(f"Unbekannte Einheit: '{unit}'")
    return conversions[unit]


def quantity(unit):
    """Liefert die Größe einer Einheit, z.B. "temperature"."""
    q, _, _ = _lookup(unit)
    return q


def to_base(value, unit):
    """Rechnet value von unit in die Basiseinheit der Größe um."""
    _, k, d = _lookup(unit)
    return k * value + d


def from_base(value, unit):
    """Rechnet value von der Basiseinheit in unit um (Umkehrfunktion von to_base)."""
    _, k, d = _lookup(unit)
    return (value - d) / k


def convert(value, original_unit, target_unit):
    """Rechnet value von original_unit in target_unit um (beliebige Größe)."""
    if quantity(original_unit) != quantity(target_unit):
        raise ValueError(
            f"Einheiten '{original_unit}' und '{target_unit}' gehören zu verschiedenen Größen."
        )
    base_val = to_base(value, original_unit)
    return float(from_base(base_val, target_unit))


def convert_temperature(value, original_unit, target_unit):
    """Rechnet eine Temperatur von original_unit in target_unit um.

    >>> convert_temperature(14.0, "°F", "°C")
    -10.0
    """
    if quantity(original_unit) != "temperature" or quantity(target_unit) != "temperature":
        raise ValueError("Eine oder beide Einheiten sind keine Temperatur.")
    return convert(value, original_unit, target_unit)