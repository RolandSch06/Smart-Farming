# Übungsaufgabe 1: Maßeinheit Konvertierung

**Baustein 1 des Kursprojekts** „Warnsystem für einen Betrieb im Mostviertel“.
Dieser Ordner ist das Grundgerüst Ihres Projekts. Er wächst mit jedem Termin um einen Baustein, Einrichtung siehe `README.md`. Das Modul `warnsystem/units.py` verwendet ab Baustein 2 die Wetterdaten, um Einheiten aus der API zu prüfen und umzurechnen.

## Aufgabe

Verallgemeinern Sie die Temperaturumrechnung aus der Vorlesung in `warnsystem/units.py`:

```python
def convert_temperature(value, original_unit, target_unit): ...
```

- `value` ist vom Typ `float`, `original_unit` und `target_unit` vom Typ `str` (`"K"`, `"°C"`, `"°F"`).
- Rückgabewert: `value` umgerechnet von `original_unit` in `target_unit`, als `float`.
- Die Umrechnung erfolgt über das Wörterbuch `conversions`: Jede Einheit wird zuerst in die Basiseinheit (Kelvin) umgerechnet und von dort in die Zieleinheit. Implementieren Sie dafür `to_base` und `from_base`, und ergänzen Sie `"°F"` im Wörterbuch.
- Fehlerbehandlung: Unbekannte Einheiten führen zu einem `ValueError` mit verständlicher Meldung (`_lookup`). Dasselbe gilt für Einheiten, die keine Temperatur sind, z.B. `"mm"` (`quantity`).
- Beispiel: `convert_temperature(14.0, "°F", "°C")` → `-10.0`

## Tests

`tests/test_units.py` ist vorgegeben und darf nicht verändert werden. Ergänzen Sie eigene Tests in `tests/test_eigene_units.py`.

```bash
python -m pytest
```

Zu Beginn schlagen die Tests fehl. Ziel ist, dass alle Tests grün sind.

## Bonus

Schreiben Sie eine allgemeine Funktion `convert(value, original_unit, target_unit)` für alle Größen im Wörterbuch. Ergänzen Sie dafür Windgeschwindigkeiten (`"m/s"`, `"km/h"`, `"kn"`). Gehören die beiden Einheiten zu verschiedenen Größen, wird ein `ValueError` geworfen. Die Bonus-Tests laufen automatisch, sobald `convert` implementiert ist.

## Abgabe

Das Projekt als ZIP oder Git-Repository (ohne `.venv`).
