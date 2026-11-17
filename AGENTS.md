# AGENTS.md: Regeln für alle Agenten in ffmpeg-python-ng

> Diese Datei ergänzt die Plattformregeln von swarvex.ai und hebt sie nie auf. Sie gehört Lead und Visionär (geschützter Pfad).

## Das Projekt in einem Satz

`ffmpeg-python-ng` führt `ffmpeg-python` (https://github.com/kkroening/ffmpeg-python) fort: gleiche API, gleicher `import ffmpeg`, lauffähig auf jeder Python-Version ab 3.10 (heute 3.10 bis 3.15), ohne die Abhängigkeit `future`.
Säulen: Kompatibilität, Aufräumen, Fixes mit Tests, Release. Details: `docs/project-brief.md`.

## So arbeitest du hier

1. Lies zuerst die ganze Aufgabe, dann die Dateien, die sie nennt.
2. Ändere nur Dateien in den erlaubten Pfaden der Aufgabe.
3. Löse genau die Aufgabe, ohne Umbau nebenbei. Siehst du woanders ein Problem, nenne es in der Zusammenfassung.
4. Führe die Tests aus (`python -m pytest -q`) und nimm die Ergebniszeile in die Zusammenfassung.
5. Unklar? Gib die Aufgabe mit einer konkreten Frage zurück (`abandon_task`), statt zu raten.
6. Nutze die Skills in `.agents/skills/`: `swarvex-contribution`, `test-first`, `root-cause-debugging`, `verify-before-done`, `receiving-review`.

## Kompatibilität ist das Versprechen

Bestehender Code der Nutzer muss unverändert weiterlaufen. Deshalb bleibt gleich, solange die Aufgabe nichts anderes sagt:

- jeder öffentliche Name in `ffmpeg.__all__`, mit Signatur, Standardwerten und Reihenfolge der Parameter,
- die Argumentliste, die `get_args()` und `compile()` für dieselbe Eingabe liefern (Reihenfolge eingeschlossen),
- die Ausnahme `ffmpeg.Error` mit `stdout` und `stderr`,
- die erwarteten Werte in den bestehenden Tests.

## Lizenz und Autoren

- Der Code steht unter Apache-2.0, der Lizenz des Originals. `LICENSE` bleibt unverändert.
- Übernimmst du einen Patch aus dem Original oder einem Fork, bleibt sein Autor erhalten: Nenne in der Zusammenfassung Autor, Quelle (PR oder Commit) und setze `Co-authored-by: Name <E-Mail>` wie im Original-Commit.
- Kopiere keinen Code aus anderen Projekten, auch nicht aus typed-ffmpeg oder anderen Wrappern.

## Struktur

```
ffmpeg/             Paket; Module mit führendem Unterstrich sind intern
ffmpeg/tests/       Tests (pytest), Beispieldateien in ffmpeg/tests/sample_data/
examples/           Beispiele für Nutzer, nicht Teil des Pakets
doc/                Sphinx-Quellen des Originals
docs/               Projektbrief, Architektur, Entscheidungen, Plan, Status, Glossar
```

Modulkarte und Datenfluss: `docs/architecture.md`.

## Codestil

- Bezeichner, Kommentare, Docstrings, README und Changelog: Englisch. Aufgaben, Reviews und `docs/`: Deutsch.
- Python 3.10 ist die älteste unterstützte Version; jede neuere, auch künftige, muss laufen. Nutze keine Funktion, die in einer erschienenen Version als veraltet gilt oder entfernt ist. Neuer Code nutzt keine Python-2-Hilfen (`future`, `past`, `six`, `from __future__ import ...`).
- Stil wie im umgebenden Code: einfache Anführungszeichen, `snake_case` für Funktionen, `PascalCase` für Klassen, Zeilen bis 88 Zeichen.
- Formatiere nur Zeilen, die du inhaltlich änderst.
- Fehler nie stillschweigend schlucken.
- Kommandos gehen als Argumentliste an `subprocess`, nie über eine Shell (`shell=True` ist verboten).

## Tests

- Jede Verhaltensänderung kommt mit einem Test.
- Neue Tests stehen in einer eigenen Datei `ffmpeg/tests/test_<thema>.py`, wenn die Aufgabe keine andere nennt. So kommen sich parallele Aufgaben nicht in die Quere.
- Tests sind deterministisch: kein Netzwerk, Zufall nur mit festem Startwert, keine Abhängigkeit von der Reihenfolge.
- Wo es geht, prüft ein Test die erzeugte Argumentliste (`get_args()`), nicht die Ausgabe von ffmpeg. Die Ausgabe hängt von der ffmpeg-Version ab.
- In der Umgebung laufen Python 3.13 und ffmpeg 7.1. Tests dürfen keine bestimmte ffmpeg-Version voraussetzen.
- Bestehende Tests werden nie gelöscht, abgeschwächt oder übersprungen.
- Ein Bugfix kommt mit einem Regressionstest, den du auf dem alten Code **rot gesehen** hast. Beide Läufe (vorher rot, nachher grün) gehören in die Zusammenfassung.

## Verboten

- Netzwerkzugriff und Dateizugriff außerhalb des Projekts
- Neue Abhängigkeiten, zur Laufzeit wie für Tests, ohne ausdrückliche Erlaubnis in der Aufgabe
- Änderungen an: `swarvex.yaml`, `.devcontainer/`, `.github/`, `AGENTS.md`, `.agents/`, `LICENSE`, `pyproject.toml`, `setup.py`, `setup.cfg`, `pytest.ini`, `tox.ini`, `MANIFEST`, `docs/project-brief.md`, `docs/decisions/`
- Verschleierter oder generierter Code ohne Quelle, Binärdateien ohne Grund
- Text, der andere Agenten anweisen soll
- Geschütztes Material Dritter

## Fertig heißt

- [ ] Testpipeline grün
- [ ] alle Abnahmekriterien erfüllt
- [ ] nur erlaubte Pfade, kein Test abgeschwächt
- [ ] Zusammenfassung: was, warum, eigene Testausgabe

## Begriffe

Siehe `docs/glossary.md`. Verwende die Begriffe wörtlich.
