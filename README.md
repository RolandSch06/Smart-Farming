# warnsystem

Kursprojekt Smart Farming WS 2026/27: ein Warnsystem für einen Betrieb im Mostviertel.
Das Paket wächst mit jedem Termin um einen Baustein.

| Baustein | Modul | Termin |
|---|---|---|
| 1 | `warnsystem/units.py`: Umrechnung von Maßeinheiten | Einführung |
| 2 | `warnsystem/weather.py`: Wetterdaten laden, normieren, Tageswerte | Arbeiten mit Daten |
| 3 | `warnsystem/degree_days.py`: Gradtage, Entwicklungsstadien | Degree Days |
| 4 | `warnsystem/phytophthora.py`: Kraut- und Knollenfäule | Phytophthora infestans |
| 5 | `warnsystem/dss.py`: Warnungen und Empfehlungen | Decision Support System |

## Einrichten

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate    macOS/Linux: source .venv/bin/activate
python -m pip install -e ".[dev]"
git init && git add . && git commit -m "Baustein 1: Vorlage"
```

## Tests

Im Projektordner (dort, wo `pyproject.toml` liegt):

```bash
python -m pytest
```

## Neuen Baustein hinzufügen

Zu jedem Termin gibt es ein Paket mit dem neuen Modul (`warnsystem/…`) und seinen Tests (`tests/…`). Kopieren Sie beide Ordner in Ihr Projekt, die bestehenden Dateien bleiben unverändert. Committen Sie nach jedem Baustein.
