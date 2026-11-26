# Plan

Stand: 24.11.2026. Schätzung für Meilenstein 1 auf swarvex: 17 Aufgaben (E9 in sechs Blöcken).

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
| E7 | W-11, W-4: README erledigt vom Lead am 17.11.2026 (Hinweis auf das Original, Umstiegshinweis, Installation von GitHub, Badges und Links auf die Fortführung). Offen: `CHANGELOG.md` und in der README die PyPI-Installation als Hauptweg, sobald 0.3.0 veröffentlicht ist | Schwarm | A | E5 | README erledigt; `CHANGELOG.md` angenommen (Aufgabe #605, #783); PyPI-Installation in der README nach dem Release |
| E8 | W-9: `docs/inherited-pull-requests.md`, offene Pull Requests des Originals gesichtet: übernehmen, verlinkt lassen, schließen | Schwarm | A | F0 | offen: Aufgabe #652 (offline aus `docs/inherited-issues/raw-pulls.json`, ersetzt #431) |
| E9 | W-9: offene Issues des Originals gesichtet, sechs Blöcke nach Nummern unter `docs/inherited-issues/` | Schwarm | A | F0 | offen: Aufgaben #653 bis #658 (offline aus `raw-issues.json`, Export des Visionärs `cdb986c`; ersetzen #612 bis #615) |
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
| #442 | Stream-Selektor mit Index 0 (angenommen, #776) | Artem Eltyshev (#490) | `ffmpeg/_run.py` | #433 |
| #443 | `explicit_maps` für `get_args()`/`compile()` (angenommen, #785) | Artem Eltyshev (#403) | `ffmpeg/_run.py` | #442 |
| #444 | `popen_args` für `run_async()` | Michael Litvin (#675) | `ffmpeg/_run.py` | #443 |
| #445 | Pipe-Eingabe für `probe()`; `input` nach `timeout` (angenommen, #778) | Rocky Cai (#588) | `ffmpeg/_probe.py` | #433 |
| #607 | `capture_stderr` für `probe()` (ersetzt #446: `test_probe_input.py` fehlte in den Pfaden) | Ezequiel Ramos (#609) | `ffmpeg/_probe.py`, `ffmpeg/tests/test_probe_input.py` | #445 |
| #447 | Pfadobjekte als Dateinamen (`os.fspath`) (angenommen, #779) | Brian Hou (#700) | `ffmpeg/_ffmpeg.py` | #433 |
| #448 | `get_hash` mit `usedforsecurity=False` (FIPS) (angenommen, #780) | Zachary Berry (#766) | `ffmpeg/_utils.py` | #433 |
| #449 | relativer Import in `_view.py` (angenommen, #781) | Shimpei Yamaguchi (#772) | `ffmpeg/_view.py` | #433 |
| #450 | Filter `atrim` (angenommen, #782; Docstring `end` vom Lead auf „audio sample“ korrigiert) | Jason Cordial (#449) | `ffmpeg/_filters.py` | #433 |

Danach #608 (Stufe A, ersetzt #606, angenommen #800): `CHANGELOG.md` unter `[Unreleased]` und die Autorentabelle in `CREDITS.md` für alle zehn übernommenen Patches; hängt an #605 und allen offenen 0.3.1-Aufgaben. Grund: Der Merge-Bot schreibt keine `Co-authored-by`-Zeilen in die Commits.

Dazu die Sphinx-Referenz: #611 (Stufe B, ersetzt #610, angenommen 23.11.) stellt `doc/src/` auf ffmpeg-python-ng um und ergänzt die Docstrings von `Error` und `view`; die Veröffentlichung auf GitHub Pages braucht einen Workflow, also den Visionär. Außerdem, was die Sichtung (E8, E9) als „übernehmen“ einstuft.

Große Graphen (Messung vom 17.11.2026, Python 3.14): `get_args()` wächst quadratisch (800 überlagerte Eingänge: 1,7 s) und bricht ab etwa 990 Knoten in einer Kette mit `RecursionError` ab. Ursache ist `topo_sort` in `ffmpeg/dag.py`. Behoben: #440 (Mengen, angenommen #777) und #441 (ohne Rekursion, angenommen #787). Danach #609: `DagNode.__repr__` ohne Parameter `other` (Fund #157).

| Aufgabe | Inhalt | Hängt ab von |
|---|---|---|
| #440 | `topo_sort` mit Mengen statt Listen; Argumentliste unverändert (angenommen, #777) | #433 |
| #441 | `topo_sort` ohne Rekursion; Kette mit 2000 Filtern läuft | #440 |

## Meilenstein 3: 0.3.2

Quelle: die Sichtung des Originals (#652 bis #658; angenommen 25.11.: #897, #898, #900, #902, #904). Je Fix eine Aufgabe mit Regressionstest, der auf dem alten Code rot ist. Vor dem Schnitt gegen den aktuellen Code geprüft: #654 und #611 (Issues) sind schon behoben, #656 (crop) ist im heutigen Code kein Fehler (Signatur und Docstring stimmen überein).

| Aufgabe | Inhalt | Quelle | Dateien | Hängt ab von |
|---|---|---|---|---|
| #681 (angenommen, #948) | `quiet=True` behält angeforderte Pipes | PR #538 (ArchieMeng) | `ffmpeg/_run.py`, `CHANGELOG.md` | – |
| #682 (gemergt, #967) | `get_args()` ohne Ausgang: klare `TypeError`-Meldung (Klasse bleibt) | Fund #176 | `ffmpeg/_run.py` | #681 |
| #683 | RTSP-Beispiel ohne Platzhalter | Issue #310 | `examples/README.md` | – |
| #685 (gemergt, #969) | Filter `hstack`/`vstack` | Wunsch PR #220 (russiaman, nur Idee) | `ffmpeg/_filters.py`, `CHANGELOG.md`, Test | – |
| #686 | README-FAQ: Flags ohne Wert mit `None` | Issue #703 | `README.md` | – |

Offen zur Entscheidung (ändern die Argumentliste für heute fehlerhafte Eingaben, also nur mit Ruling oder Visionär): #406 (Dateiname mit `-`), #416 (Apostroph-Escaping), #461/PR #844 (leere Flag-Argumente); #108/#116/PR #783 (stdin). Kandidaten ohne Bedenken: PR #220 (`vstack`/`hstack`, ergänzt nur Filter wie `atrim`).

Aus Block 5 am Code geprüft (26.11.): #745 (Positionsargumente von Filtern werden in `nodes.py` zweimal auf Ebene 1 maskiert) und #756 (gleiche `input()` werden ein Knoten) ändern beide `get_args()` für heute gültige Eingaben. Sie gehören deshalb zu den offenen Entscheidungen oben. Approval #110 an den Visionär: 0.3.2 bleibt streng kompatibel, diese Punkte kommen in 0.4.0 mit „Breaking changes“. #703 → #686. Wünsche: #707 (`global_args`/`overwrite_output` auf Filterströmen), #740 (Helfer für Standbild plus Ton).

## Grundausstattung

Steht im Projektbrief, Abschnitt Grundausstattung; vom Visionär am 17.11.2026 bestätigt.
