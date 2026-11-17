# Projektbrief: ffmpeg-python-ng

> Ergebnis des Projektinterviews (LEAD.md, Phase 0). Aufgaben entstehen erst, wenn der Visionär den Brief bestätigt hat.
> Status: 17.11.2026 · Interviewrunden: 2 · bestätigt: noch nicht

## Recherchierte Fakten (Stand 17.11.2026)

| Thema | Befund |
|---|---|
| Original | `kkroening/ffmpeg-python`, nicht archiviert, 11.020 Sterne, 950 Forks, 524 offene Issues und PRs |
| Letztes Release | 0.2.0 vom 05.07.2019 (Tag `0.2.0`, Commit `78fb6cf`); auf PyPI einzige Abhängigkeit: `future` |
| Letzter Commit | `df129c7` vom 11.07.2022 auf `master`; 41 Commits nach 0.2.0, nie veröffentlicht |
| Fork | `marco8154/ffmpeg-python`, öffentlicher GitHub-Fork, Stand identisch mit `df129c7`, volle Historie (25 Autoren) |
| Lizenz | Apache-2.0, eine `LICENSE`-Datei, keine `NOTICE`, keine Lizenzköpfe in den Quelldateien |
| Maintainer-Kontakt | Issue #807 (seit November 2023 ohne Antwort des Maintainers). Letzter Kommentar dort: 27.08.2025. Die Fork-Ankündigung vom 16.11.2026 ist dort **nicht** zu sehen |
| `future` | `install_requires=['future']`; benutzt in `_ffmpeg.py`, `_utils.py`, `nodes.py` (`past.builtins.basestring`, `with_metaclass`), dazu `from __future__ import unicode_literals` in allen Modulen |
| Build | `setup.py` (Version 0.2.0, Klassifizierer Python 2.7 bis 3.10), `tox.ini` (py27 bis py310), CI auf `ubuntu-20.04` mit Python 2.7 bis 3.10, Black 21.12b0 mit `target_version = py27` |
| Tests heute | Python 3.14.4, ffmpeg 9.0.2, Windows: 68 grün, 2 rot. `test_pipe` (30720 statt 24576 Bytes) und `test__probe` (Dauer `7.035646` statt `7.036000`). Beide hängen an der ffmpeg-Version, nicht an Python |
| PyPI-Name | `ffmpeg-python-ng` ist frei |
| Vorauswahl grantnegri | 16 Commits vor dem Original, davon 8 gemergte PRs: `atrim`-Filter, Stream-Selektor mit Index 0, Pipe-Eingabe für `ffprobe`, `popen_args` für `run_async()`, `mkstemp` statt `mktemp`, dazu 3 Versionsanhebungen in `requirements.txt` (numpy, py, urllib3), die mit dem neuen Build entfallen |

## Entscheidungen (harte Fakten)

Zustände: **entschieden**, **Empfehlung angenommen**, **delegiert**, **offen**. „Startassistent“ heißt: beim Anlegen des Projekts festgelegt, im Interview noch zu bestätigen.

| ID | Entscheidung | Ergebnis | Zustand | Runde | Grund / Verweis |
|---|---|---|---|---|---|
| G1 | Typ | Bibliothek, Fortführung (Prozess `continuation`) | Startassistent | – | |
| G2 | Kern in einem Satz | Gepflegte, API-kompatible Fortführung von ffmpeg-python für aktuelle Python-Versionen | Startassistent | – | Vision |
| G4 | Säulen | Kompatibilität, Aufräumen, Fixes mit Tests, Release | Startassistent | – | Vision |
| G5 | Nicht-Ziele | keine neue API, kein Umbau auf Typisierung wie typed-ffmpeg | Startassistent | – | Vision; mindestens ein drittes fehlt |
| G6 | Erfolg Version 1 | Release auf PyPI, Tests grün auf 3.10 bis 3.14, `future` entfernt, Build mit aktuellen Werkzeugen | Startassistent | – | Ziel |
| G8 | Sprache | Python | Startassistent | – | |
| G9 | Lizenz | Apache-2.0 (geerbt) / CC BY 4.0 | Startassistent | – | Pflicht bei Fortführung |
| G10 | Projektsprache | Deutsch; Bezeichner, README und Changelog Englisch | Startassistent | – | Nutzer sind international |
| G13 | Bestehendes | siehe Fakten oben | recherchiert | – | |
| F1 | Ausgangspunkt | Fork vom `master` des Originals (`df129c7`, 11.07.2022) mit voller Historie, nicht vom Tag 0.2.0 | Empfehlung angenommen | 1 | 41 Commits nach 0.2.0 enthalten bereits Fixes |
| F2 | Aufgegeben? Wartezeit | Das Projekt startet sofort. Keine 30 Tage Wartezeit nach der Ankündigung in #807 | entschieden | 1 | Abweichung von der Handbuch-Empfehlung; Frage in #807 seit November 2023 ohne Antwort des Maintainers |
| F3 | Lizenz | Apache-2.0 bleibt, `LICENSE` und Autoren unverändert | Empfehlung angenommen | 1 | Pflicht |
| F4 / T11 | Name | PyPI-Paket `ffmpeg-python-ng`, Import bleibt `import ffmpeg`, GitHub-Repo wird in `ffmpeg-python-ng` umbenannt (Visionär). README: „continuation of ffmpeg-python“, nicht parallel zu `ffmpeg-python` installierbar | Empfehlung angenommen | 1 | Name auf PyPI frei |
| F6 | Erstes Ziel | Release 0.3.0 „lebt wieder“: `future` entfernt, neuer Build, Tests grün, dazu der Sicherheitsfix `mkstemp` statt `mktemp` | Empfehlung angenommen | 1 | |
| F7 | Übernommene PRs | 0.3.0: nur `mkstemp`. 0.3.1: `atrim`-Filter, Stream-Selektor mit Index 0, Pipe-Eingabe für `ffprobe`, `popen_args` für `run_async()`. Autoren bleiben in der Historie | Empfehlung angenommen | 1 | Vorauswahl grantnegri |
| F8 | Upstream | Kommt der Maintainer zurück, gehen die Fixes als PRs an das Original; über eine Zusammenlegung entscheidet der Visionär | Empfehlung angenommen | 1 | |
| G7 / T7 | Plattformen und Versionen | Python 3.10 bis 3.14, Python 2 entfällt. Linux mit allen fünf Versionen, Windows und macOS mit je einer. ffmpeg in der Testumgebung auf eine feste Version gesetzt | Empfehlung angenommen | 1 | 2 Tests hängen an der ffmpeg-Version |
| G8a | Build | `pyproject.toml` mit setuptools statt `setup.py`; Veröffentlichung über PyPI Trusted Publishing, kein Token im Repo | Empfehlung angenommen | 1 | |
| G15 | Budget | 0 Credits für Spendenaufträge, keine Assets nötig | Empfehlung angenommen | 1 | Schwarmgröße: Runde 2 |
| G20 | Rolle des Visionärs | gibt frei: Release, PyPI-Veröffentlichung, alles, was nach außen an das Original geht. Alles andere entscheidet der Lead und berichtet wöchentlich | Empfehlung angenommen | 1 | |
| G3 | Zielgruppe | Python-Entwickler, die `ffmpeg-python` heute im Code haben und ohne Codeänderung umsteigen wollen; neue Nutzer an zweiter Stelle | Empfehlung angenommen | 2 | |
| G5 | Weitere Nicht-Ziele | kein mitgeliefertes ffmpeg-Binary, keine async-API, keine Unterstützung für Python unter 3.10 | Empfehlung angenommen | 2 | |
| G11 | Qualitätsstufe | poliert: jede Änderung mit Test, keine bekannte Regression gegenüber 0.2.0 | Empfehlung angenommen | 2 | viele bestehende Nutzer |
| G14 / T1–T5 | Unantastbar | öffentliche Namen und Signaturen, die erzeugte ffmpeg-Kommandozeile bei gleicher Eingabe, die Ausnahme `ffmpeg.Error`, `LICENSE`, Autoren in der Historie. Form der Nutzung, Schnittstelle, Formate und Fehlerverhalten bleiben wie im Original | Empfehlung angenommen | 2 | |
| G15 | Schwarmgröße | 3 bis 10 Agenten, kleine Aufgaben der Stufen A und B | Empfehlung angenommen | 2 | |
| T8 | Leistung | keine Leistungsziele; die Bibliothek baut nur Kommandos zusammen | Empfehlung angenommen | 2 | |
| T9 | Abhängigkeiten | Laufzeit: keine, nur Standardbibliothek. Tests: `pytest`, `pytest-mock`. `numpy` nur in den Beispielen | Empfehlung angenommen | 2 | |
| T10 | Sicherheit | Kommandos gehen als Argumentliste ohne Shell an ffmpeg; Meldungen über GitHub Security Advisories, `SECURITY.md` | Empfehlung angenommen | 2 | |
| T12 | Dokumentation | 0.3.0: README mit Umstiegshinweis und Changelog. 0.3.1: Sphinx-Referenz auf GitHub Pages | Empfehlung angenommen | 2 | |
| G16 | Barrierefreiheit | entfällt, keine Oberfläche | offen | – | späterer Zweig |
| G17 | Nutzerdaten | keine | offen | – | späterer Zweig |
| G18 | Veröffentlichung | PyPI; Termin legt der Visionär fest | offen | – | späterer Zweig |
| G19 | Einnahmen | keine, vorläufig: kostenlos | offen | – | späterer Zweig |
| T6, T13 | Konfiguration, Erweiterbarkeit | vorläufig: wie im Original, nichts Neues | offen | – | späterer Zweig |

Die folgenden Abschnitte fassen die Entscheidungen lesbar zusammen. Bei Widerspruch gilt die Tabelle.

## In einem Satz

`ffmpeg-python-ng` ist die gepflegte Fortführung von `ffmpeg-python`: gleiche API, gleicher Import, lauffähig auf aktuellen Python-Versionen und ohne die Abhängigkeit `future`.

## Säulen

1. **Kompatibilität:** Bestehender Code läuft nach dem Umstieg unverändert. Man merkt es daran, dass die alten Tests ohne Anpassung der erwarteten Kommandozeilen grün bleiben.
2. **Aufräumen:** Keine Python-2-Reste, keine Laufzeitabhängigkeit. Man merkt es an einer leeren Abhängigkeitsliste des Pakets.
3. **Fixes mit Tests:** Übernommene Patches behalten ihren Autor und bekommen einen Test, der ohne den Patch rot ist.
4. **Release:** Was fertig ist, erscheint auf PyPI mit Changelog.

## Nicht-Ziele

- keine neue API
- kein Umbau auf Typisierung wie bei typed-ffmpeg
- kein mitgeliefertes ffmpeg-Binary
- keine async-API
- keine Unterstützung für Python unter 3.10

## Erfolgskriterien für 0.3.0

- [ ] Tests grün auf Python 3.10 bis 3.14 unter Linux, dazu je eine Version unter Windows und macOS
- [ ] `future` ist weder Abhängigkeit noch Import
- [ ] Build über `pyproject.toml`, Wheel und sdist installierbar
- [ ] `mkstemp` statt `mktemp`, mit Test
- [ ] README mit Umstiegshinweis und Changelog
- [ ] auf PyPI als `ffmpeg-python-ng` veröffentlicht, nach Freigabe durch den Visionär

## Meilensteine

| Meilenstein | Inhalt |
|---|---|
| 0.3.0 „lebt wieder“ | siehe Erfolgskriterien |
| 0.3.1 | `atrim`-Filter, Stream-Selektor mit Index 0, Pipe-Eingabe für `ffprobe`, `popen_args` für `run_async()`, Sphinx-Referenz |

## Grundausstattung

Folgt in Phase 2 (`templates/baseline-packages.md`) und wird hier nachgetragen.

## Offen beim Visionär

- [ ] Ankündigung in Issue #807 des Originals posten
- [ ] GitHub-Repo in `ffmpeg-python-ng` umbenennen
