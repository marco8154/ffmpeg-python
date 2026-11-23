# Plan

Stand: 23.11.2026. Schätzung für Meilenstein 1 auf swarvex: 17 Aufgaben (E9 in vier Blöcken).

## Globale Vorgaben (binden jede Aufgabe)

- Jede erschienene Python-Version ab 3.10 (heute 3.10 bis 3.15), keine Laufzeitabhängigkeit, keine neuen Testabhängigkeiten.
- Öffentliche API, Argumentlisten und `ffmpeg.Error` bleiben unverändert (`AGENTS.md`, Abschnitt Kompatibilität).
- Übernommene Patches behalten ihren Autor (`Co-authored-by`).
- Neue Tests in eigenen Dateien `ffmpeg/tests/test_<thema>.py`.

## Meilenstein 1: 0.3.0 „lebt wieder“

Liste nach `templates/continuation.md` (W-1 bis W-12).

| Punkt | Inhalt | Wer | Stufe | Hängt ab von | Stand |
|---|---|---|---|---|---|
| W-1 | Original gefragt | Visionär | – | – | offen: Ankündigung in #807 fehlt; Start ohne Wartezeit entschieden (Entscheidung 0001) |
| W-2 | Fork mit Historie | Lead | D | – | erledigt: Fork steht auf `df129c7` mit voller Historie; README-Hinweis erledigt |
| W-3 | Lizenz geerbt | Lead | D | – | erledigt: `LICENSE` unverändert, keine `NOTICE`, keine Lizenzköpfe im Original |
| W-4 | Name geklärt | Visionär | – | – | erledigt: Paket `ffmpeg-python-ng`, Repo `marco8154/ffmpeg-python` (Entscheidung 0002) |
| F0 | Fundament: Testvertrag, Umgebung, `AGENTS.md`, Skills, CI, zwei Tests unabhängig von der ffmpeg-Version | Lead | D | – | erledigt: `5677b37`, `59a699d` |
| E1 | `future` und `past` aus `ffmpeg/_utils.py`, `ffmpeg/_ffmpeg.py`, `ffmpeg/nodes.py` entfernen; Test: `import ffmpeg` gelingt ohne `future` | Schwarm | B | F0 | gemergt: Aufgabe #427 (`815aa2c`) |
| E2 | Python-2-Reste entfernen (`from __future__ import`, `from builtins import`, Zweige auf `sys.version_info`, Ausweich-Importe) in `ffmpeg/*.py` ohne Tests | Schwarm | B | E1, E4 | gemergt: Aufgabe #433 (`5c006b3`) |
| E3 | Python-2-Reste und zwei Warnungen in `ffmpeg/tests/test_ffmpeg.py` beheben (Rückgabewert in `test_fluent_complex_filter`, Regex-Warnung) | Schwarm | B | F0 | gemergt: Aufgabe #428 (`56ef339`) |
| E4 | W-8: `mkstemp` statt `mktemp` in `ffmpeg/_view.py`, mit Test; übernommener Patch von Sarthak Munshi (grantnegri `c1ef452`) | Schwarm | B | F0 | gemergt: Aufgabe #429 (`a2c0177`) |
| E5 | W-5: Build über `pyproject.toml` mit setuptools, Name `ffmpeg-python-ng`, Version 0.3.0, keine Abhängigkeiten, `requires-python = ">=3.10"` ohne Obergrenze, Klassifizierer 3.10 bis 3.15; `setup.py`, `setup.cfg`, `tox.ini`, `MANIFEST`, `requirements.txt` entfallen; `future` aus der Umgebung | Lead | D | E1, E2 | erledigt: Aufgabe #604 am 23.11.2026; Build ungeprüft, bis die CI läuft (Sandbox ohne setuptools) |
| E6 | W-10: `CREDITS.md` mit den Autoren aus der Git-Historie | Schwarm | A | F0 | angenommen: Aufgabe #430 |
| E7 | W-11, W-4: README erledigt vom Lead am 17.11.2026 (Hinweis auf das Original, Umstiegshinweis, Installation von GitHub, Badges und Links auf die Fortführung). Offen: `CHANGELOG.md` und in der README die PyPI-Installation als Hauptweg, sobald 0.3.0 veröffentlicht ist | Schwarm | B | E5 | README erledigt, Rest geplant |
| E8 | W-9: `docs/inherited-pull-requests.md`, offene Pull Requests des Originals gesichtet: übernehmen, verlinkt lassen, schließen | Schwarm | A | F0 | Nacharbeit: Aufgabe #431; die Peer-Review hatte kein Netzwerk und konnte die Fakten nicht prüfen |
| E9 | W-9: offene Issues des Originals gesichtet, vier Blöcke nach Nummern unter `docs/inherited-issues/` | Schwarm | A | E8 | angelegt: Aufgaben #434 bis #437, warten auf #431 |
| E10 | `SECURITY.md` (GitHub Security Advisories) | Schwarm | A | F0 | angenommen: Aufgabe #432 |
| E14 | Issue-Vorlage für Fehlerberichte (`.github/ISSUE_TEMPLATE/`) | Lead | D | F0 | erledigt: Aufgabe #556 am 19.11.2026; wirkt, sobald Issues auf dem Repo eingeschaltet sind |
| E11 | Release-Workflow mit PyPI Trusted Publishing | Lead | D | E5 | geplant; braucht den Visionär auf PyPI |
| E12 | W-11: Release 0.3.0 | Visionär gibt frei | – | alle | geplant |
| E13 | W-12: Nutzern Bescheid geben (#807, #877 im Original) | Visionär | – | E12 | geplant |
| E15 | Antrag nach PEP 541 auf den PyPI-Namen `ffmpeg-python` (Issue an `pypi/support`), frühestens 17.12.2026 und erst nach dem Release (Entscheidung 0003) | Visionär | – | E12 | geplant |

W-6 (alte Tests laufen) ist mit F0 erfüllt: 70 Tests grün in der Umgebung. W-7 (Abhängigkeiten geprüft) braucht keine eigene Aufgabe: Die einzige Laufzeitabhängigkeit ist `future`, und E1 mit E5 entfernt sie.

**Kritischer Pfad:** F0 → E1 → E2 → E5 → E7 → E12.

**Parallel ab F0:** E1, E3, E4, E6, E8, E10. Keine zwei davon schreiben in dieselbe Datei.

## Meilenstein 2: 0.3.1

Übernommene Patches: die neun `take-0.3.1`-Einträge aus `docs/inherited-pull-requests.md`, je eine Aufgabe mit Test, der ohne den Patch rot ist, und `Co-authored-by`. Alle warten auf #433 (E2), weil E2 dieselben Dateien berührt. Gleiche Dateien laufen als Kette.

| Aufgabe | Inhalt | Autor im Original (PR) | Dateien | Hängt ab von |
|---|---|---|---|---|
| #442 | Stream-Selektor mit Index 0 | Artem Eltyshev (#490) | `ffmpeg/_run.py` | #433 |
| #443 | `explicit_maps` für `get_args()`/`compile()` | Artem Eltyshev (#403) | `ffmpeg/_run.py` | #442 |
| #444 | `popen_args` für `run_async()` | Michael Litvin (#675) | `ffmpeg/_run.py` | #443 |
| #445 | Pipe-Eingabe für `probe()`; `input` nach `timeout` | Rocky Cai (#588) | `ffmpeg/_probe.py` | #433 |
| #446 | `capture_stderr` für `probe()` | Ezequiel Ramos (#609) | `ffmpeg/_probe.py` | #445 |
| #447 | Pfadobjekte als Dateinamen (`os.fspath`) | Brian Hou (#700) | `ffmpeg/_ffmpeg.py` | #433 |
| #448 | `get_hash` mit `usedforsecurity=False` (FIPS) | Zachary Berry (#766) | `ffmpeg/_utils.py` | #433 |
| #449 | relativer Import in `_view.py` | Shimpei Yamaguchi (#772) | `ffmpeg/_view.py` | #433 |
| #450 | Filter `atrim` | Jason Cordial (#449) | `ffmpeg/_filters.py` | #433 |

Dazu die Sphinx-Referenz auf GitHub Pages und was die Sichtung (E8, E9) als „übernehmen“ einstuft.

Große Graphen (Messung vom 17.11.2026, Python 3.14): `get_args()` wächst quadratisch (800 überlagerte Eingänge: 1,7 s) und bricht ab etwa 990 Knoten in einer Kette mit `RecursionError` ab. Ursache ist `topo_sort` in `ffmpeg/dag.py`.

| Aufgabe | Inhalt | Hängt ab von |
|---|---|---|
| #440 | `topo_sort` mit Mengen statt Listen; Argumentliste unverändert | #433 |
| #441 | `topo_sort` ohne Rekursion; Kette mit 2000 Filtern läuft | #440 |

## Grundausstattung

Steht im Projektbrief, Abschnitt Grundausstattung; vom Visionär am 17.11.2026 bestätigt.
