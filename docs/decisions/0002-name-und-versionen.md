# 0002: Paketname, Importname und unterstützte Python-Versionen

- Datum: 17.11.2026
- Entschieden von: Visionär (Empfehlung des Leads angenommen)
- Status: gilt

## Zusammenhang

Das Original heißt auf PyPI `ffmpeg-python` und wird als `import ffmpeg` benutzt. Der Name auf PyPI gehört dem Maintainer des Originals. Das Original unterstützt laut `setup.py` Python 2.7 bis 3.10.

## Entscheidung

- Das Paket heißt auf PyPI `ffmpeg-python-ng`. Der Name war am 17.11.2026 frei.
- Der Importname bleibt `ffmpeg`. Nutzer tauschen nur das Paket, nicht ihren Code.
- Die erste Version ist 0.3.0. Sie setzt die Zählung des Originals (0.2.0) fort.
- Unterstützt werden Python 3.10 bis 3.14. Python 2 und alles unter 3.10 entfallen.

## Alternativen

- Neuer Importname (zum Beispiel `ffmpeg_ng`): beide Pakete wären nebeneinander installierbar, aber jeder Nutzer müsste seinen Code ändern. Das widerspricht der Säule Kompatibilität.
- Python 3.8 und 3.9 weiter unterstützen: beide bekommen keine Sicherheitsupdates mehr.

## Folgen

- `ffmpeg-python` und `ffmpeg-python-ng` legen beide das Paket `ffmpeg` an und dürfen nicht zusammen installiert sein. Die README sagt das im Umstiegshinweis: erst `pip uninstall ffmpeg-python`, dann `pip install ffmpeg-python-ng`.
- Der Wegfall von Python 2 ist die einzige bewusste Inkompatibilität in 0.3.0 und steht im Changelog.
