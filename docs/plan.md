# Plan

Stand: 17.11.2026. Schätzung für Meilenstein 1 auf swarvex: 17 Aufgaben (E9 in vier Blöcken).

## Globale Vorgaben (binden jede Aufgabe)

- Python 3.10 bis 3.14, keine Laufzeitabhängigkeit, keine neuen Testabhängigkeiten.
- Öffentliche API, Argumentlisten und `ffmpeg.Error` bleiben unverändert (`AGENTS.md`, Abschnitt Kompatibilität).
- Übernommene Patches behalten ihren Autor (`Co-authored-by`).
- Neue Tests in eigenen Dateien `ffmpeg/tests/test_<thema>.py`.

## Meilenstein 1: 0.3.0 „lebt wieder“

Liste nach `templates/continuation.md` (W-1 bis W-12).

| Punkt | Inhalt | Wer | Stufe | Hängt ab von | Stand |
|---|---|---|---|---|---|
| W-1 | Original gefragt | Visionär | – | – | offen: Ankündigung in #807 fehlt; Start ohne Wartezeit entschieden (Entscheidung 0001) |
| W-2 | Fork mit Historie | Lead | D | – | erledigt: Fork steht auf `df129c7` mit voller Historie; README-Hinweis offen (E7) |
| W-3 | Lizenz geerbt | Lead | D | – | erledigt: `LICENSE` unverändert, keine `NOTICE`, keine Lizenzköpfe im Original |
| W-4 | Name geklärt | Visionär | – | – | erledigt: Paket `ffmpeg-python-ng`, Repo `marco8154/ffmpeg-python` (Entscheidung 0002) |
| F0 | Fundament: Testvertrag, Umgebung, `AGENTS.md`, Skills, CI, zwei Tests unabhängig von der ffmpeg-Version | Lead | D | – | erledigt: `5677b37`, `59a699d` |
| E1 | `future` und `past` aus `ffmpeg/_utils.py`, `ffmpeg/_ffmpeg.py`, `ffmpeg/nodes.py` entfernen; Test: `import ffmpeg` gelingt ohne `future` | Schwarm | B | F0 | offen: Aufgabe #427 |
| E2 | Python-2-Reste entfernen (`from __future__ import`, `from builtins import`, Zweige auf `sys.version_info`, Ausweich-Importe) in `ffmpeg/*.py` ohne Tests | Schwarm | B | E1, E4 | angelegt: Aufgabe #433, wartet auf #427 und #429 |
| E3 | Python-2-Reste und zwei Warnungen in `ffmpeg/tests/test_ffmpeg.py` beheben (Rückgabewert in `test_fluent_complex_filter`, Regex-Warnung) | Schwarm | B | F0 | offen: Aufgabe #428 |
| E4 | W-8: `mkstemp` statt `mktemp` in `ffmpeg/_view.py`, mit Test; übernommener Patch von Sarthak Munshi (grantnegri `c1ef452`) | Schwarm | B | F0 | offen: Aufgabe #429 |
| E5 | W-5: Build über `pyproject.toml` mit setuptools, Name `ffmpeg-python-ng`, Version 0.3.0, keine Abhängigkeiten; `setup.py`, `setup.cfg`, `tox.ini`, `MANIFEST`, `requirements.txt` entfallen; `future` aus der Umgebung | Lead | D | E1, E2 | geplant |
| E6 | W-10: `CREDITS.md` mit den Autoren aus der Git-Historie | Schwarm | A | F0 | offen: Aufgabe #430 |
| E7 | W-11, W-4: README (erste Zeile „Continuation of ffmpeg-python“, Umstiegshinweis, Badges und Links auf die Fortführung) und `CHANGELOG.md` | Schwarm | B | E5 | geplant |
| E8 | W-9: `docs/inherited-pull-requests.md`, offene Pull Requests des Originals gesichtet: übernehmen, verlinkt lassen, schließen | Schwarm | A | F0 | offen: Aufgabe #431 |
| E9 | W-9: offene Issues des Originals gesichtet, vier Blöcke nach Nummern unter `docs/inherited-issues/` | Schwarm | A | E8 | angelegt: Aufgaben #434 bis #437, warten auf #431 |
| E10 | `SECURITY.md` (GitHub Security Advisories) | Schwarm | A | F0 | offen: Aufgabe #432 |
| E14 | Issue-Vorlage für Fehlerberichte (`.github/ISSUE_TEMPLATE/`) | Lead | D | F0 | geplant; `.github/` ist geschützt |
| E11 | Release-Workflow mit PyPI Trusted Publishing | Lead | D | E5 | geplant; braucht den Visionär auf PyPI |
| E12 | W-11: Release 0.3.0 | Visionär gibt frei | – | alle | geplant |
| E13 | W-12: Nutzern Bescheid geben (#807, #877 im Original) | Visionär | – | E12 | geplant |

W-6 (alte Tests laufen) ist mit F0 erfüllt: 70 Tests grün in der Umgebung. W-7 (Abhängigkeiten geprüft) braucht keine eigene Aufgabe: Die einzige Laufzeitabhängigkeit ist `future`, und E1 mit E5 entfernt sie.

**Kritischer Pfad:** F0 → E1 → E2 → E5 → E7 → E12.

**Parallel ab F0:** E1, E3, E4, E6, E8, E10. Keine zwei davon schreiben in dieselbe Datei.

## Meilenstein 2: 0.3.1

Übernommene Patches aus der Vorauswahl, je eine Aufgabe mit Test, der ohne den Patch rot ist:

| Inhalt | Autor im Original | Dateien |
|---|---|---|
| Filter `atrim` | Jason Cordial | `ffmpeg/_filters.py` |
| Stream-Selektor mit Index 0 | Artem Eltyshev | `ffmpeg/nodes.py` |
| Pipe-Eingabe für `ffprobe` | Rocky Cai | `ffmpeg/_probe.py` |
| `popen_args` für `run_async()` | Michael Litvin | `ffmpeg/_run.py` |

Dazu die Sphinx-Referenz auf GitHub Pages und was die Sichtung (E8, E9) als „übernehmen“ einstuft.

Große Graphen (Messung vom 17.11.2026, Python 3.14): `get_args()` wächst quadratisch (800 überlagerte Eingänge: 1,7 s) und bricht ab etwa 990 Knoten in einer Kette mit `RecursionError` ab. Ursache ist `topo_sort` in `ffmpeg/dag.py`.

| Aufgabe | Inhalt | Hängt ab von |
|---|---|---|
| #440 | `topo_sort` mit Mengen statt Listen; Argumentliste unverändert | #433 |
| #441 | `topo_sort` ohne Rekursion; Kette mit 2000 Filtern läuft | #440 |

## Grundausstattung

Steht im Projektbrief, Abschnitt Grundausstattung; vom Visionär am 17.11.2026 bestätigt.
