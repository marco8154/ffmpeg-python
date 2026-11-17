# 0002: Paketname, Importname und unterstützte Python-Versionen

- Datum: 17.11.2026
- Entschieden von: Visionär (Empfehlung des Leads angenommen)
- Status: gilt; zum PyPI-Namen `ffmpeg-python` siehe Entscheidung 0003

## Zusammenhang

Das Original heißt auf PyPI `ffmpeg-python` und wird als `import ffmpeg` benutzt. Der Name auf PyPI gehört dem Maintainer des Originals. Das Original unterstützt laut `setup.py` Python 2.7 bis 3.10.

## Entscheidung

- Das Paket heißt auf PyPI `ffmpeg-python-ng`. Der Name war am 17.11.2026 frei.
- Das GitHub-Repo heißt `marco8154/ffmpeg-python`, wie das Original, nur mit anderem Besitzer. Ein kurzzeitiges Umbenennen in `ffmpeg-python-ng` am 17.11.2026 wurde am selben Tag zurückgenommen, nachdem ein Nutzer in #807 des Originals darum gebeten hatte; die Adresse mit Suffix leitet weiter.
- Der Importname bleibt `ffmpeg`. Nutzer tauschen nur das Paket, nicht ihren Code.
- Die erste Version ist 0.3.0. Sie setzt die Zählung des Originals (0.2.0) fort.
- Unterstützt wird jede erschienene Python-Version ab 3.10 (Visionär, 17.11.2026). Heute sind das 3.10 bis 3.15. Python 2 und alles unter 3.10 entfallen.
- Eine neue Python-Version wird unterstützt, sobald sie erscheint: Die CI testet die neueste stabile Version automatisch (`3.x`) und die nächste schon als Vorabversion. Nach jedem Release wird sie in die feste Liste der CI aufgenommen und die Vorabversion um eins erhöht.
- Die Paketangaben (ab `pyproject.toml`) setzen nur eine Untergrenze (`requires-python = ">=3.10"`), nie eine Obergrenze.

## Alternativen

- Neuer Importname (zum Beispiel `ffmpeg_ng`): beide Pakete wären nebeneinander installierbar, aber jeder Nutzer müsste seinen Code ändern. Das widerspricht der Säule Kompatibilität.
- Python 3.8 und 3.9 weiter unterstützen: beide bekommen keine Sicherheitsupdates mehr.
- Python 3.10 streichen (am 17.11.2026 erneut geprüft, abgelehnt): Die Bibliothek braucht nichts aus 3.11. Ubuntu 22.04 bringt 3.10 mit, und Nutzer dort könnten sonst nicht umsteigen und blieben beim Original mit `future`. Streichen später nur mit konkretem Grund, als eigene Entscheidung im Changelog.

## Folgen

- `ffmpeg-python` und `ffmpeg-python-ng` legen beide das Paket `ffmpeg` an und dürfen nicht zusammen installiert sein. Die README sagt das im Umstiegshinweis: erst `pip uninstall ffmpeg-python`, dann `pip install ffmpeg-python-ng`.
- Der Wegfall von Python 2 ist die einzige bewusste Inkompatibilität in 0.3.0 und steht im Changelog.
