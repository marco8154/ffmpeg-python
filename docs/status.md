# Status

## 17.11.2026, Zyklus des Lead-Dienstes (Reviews und 0.3.1-Schnitt)

**Nachtrag 17.11.2026, PyPI-Name.** milahu hat in #807 vorgeschlagen, den Namen `ffmpeg-python` bei PyPI zu beantragen. Entscheidung des Visionärs (0003): 0.3.0 erscheint zuerst als `ffmpeg-python-ng`; den Antrag nach PEP 541 stellt der Visionär nach dem Release, frühestens am 17.12.2026, wenn der Maintainer bis dahin nicht geantwortet hat (Plan E15).

**Nachtrag 17.11.2026, Python-Versionen.** Entscheidung des Visionärs: Jede erschienene Python-Version ab 3.10 wird unterstützt, auch künftige. Python 3.15 (erschienen am 09.10.2026) ist in die CI aufgenommen. Neu in der CI: die jeweils neueste stabile Version (`3.x`) unter Linux, Windows und macOS, die nächste Version 3.16 als Vorabversion (blockiert nicht) und ein wöchentlicher Lauf. Das Projektziel auf swarvex.ai nennt noch „3.10 bis 3.14“; das kann nur der Visionär dort ändern.

Ruling: Nach jedem Python-Release die Version in die feste Liste der CI aufnehmen und die Vorabversion um eins erhöhen — sonst prüft niemand mehr die übernächste Version früh — Kosten bei Irrtum: eine Zeile in `ci.yml`.

**Lage.** Erste Einreichungen sind da. Angenommen: #430 (`CREDITS.md`) und #432 (`SECURITY.md`), beide auf Anhieb. Zwei Einreichungen stammen vom Lead-Konto selbst und gehen in die Peer-Review, mit Prüffragen: #543 (Aufgabe #427, `future` entfernt, 73 Tests grün) und #545 (Aufgabe #431, 46 offene PRs des Originals gesichtet). Kein Agent aktiv; Engpass laut `metrics`: Mitwirkende.

**Was passiert ist.**

- Aus der PR-Sichtung (#545) die neun `take-0.3.1`-Patches als Aufgaben #442 bis #450 geschnitten (`docs/plan.md`, Meilenstein 2). Die Diffs habe ich per `git fetch` der PR-Refs selbst gelesen; jede Aufgabe enthält den Patch, weil die Sandbox der Mitwirkenden kein Netzwerk hat.
- Funde #106 (future in `setup.py`; gehört zu E5), #107 und #108 entschieden.

**Urteile des Leads (dieser Zyklus).**

- Ruling: Kleine Fixes ohne Tests sind `take-0.3.1`, der Test entsteht beim Übernehmen — sonst wären auch die vier vorentschiedenen Patches `take-later` — Kosten bei Irrtum: einzelne Aufgaben nach hinten schieben.
- Ruling: `probe()` bekommt `input` und `capture_stderr` hinter `timeout`, anders als PR #588 — sonst bricht `probe(f, 'ffprobe', 5)` — Kosten bei Irrtum: keine, nur Abweichung vom Original.
- Ruling: #447 (PR #700) nutzt `os.fspath` direkt, ohne den Ausweichcode für Python < 3.6 — Kosten bei Irrtum: keine.
- Ruling: Alle Patch-Aufgaben warten auf #433, Dateien mit mehreren Patches als Kette — keine zwei offenen Aufgaben auf derselben Datei — Kosten bei Irrtum: späterer Start.
- Ruling: Für PR #609 fehlt im Commit eine E-Mail; `Co-authored-by` nutzt `ezequielramos@users.noreply.github.com` — Kosten bei Irrtum: Zeile im Commit korrigieren.

**Nächste Schritte.**

1. Peer-Reviews zu #543 und #545 abwarten; danach laufen #433, dann #440 und #442 bis #450 von selbst an.
2. Wenn #427 und #433 gemergt sind: E5 (Build über `pyproject.toml`) selbst erledigen.
3. Offen beim Visionär bleibt alles aus dem Abschnitt „Fundament“ unten (Actions, Issues, private Sicherheitsmeldungen — jetzt wichtig, weil `SECURITY.md` auf den Advisory-Link zeigt —, Ankündigung in #807).

## 17.11.2026, Zyklus des Lead-Dienstes

**Lage.** Noch keine Einreichung, keine Nachrichten, keine Funde; kein Agent aktiv (`metrics`: Engpass „contributors“). Die sechs Aufgaben #427 bis #432 sind weiter offen. Folgeaufgaben sind jetzt mit `depends_on` vorab angelegt und gehen von selbst raus, sobald ihre Vorgänger gemergt sind:

- #433 (E2, Python-2-Reste aus dem Paket, Stufe B): wartet auf #427 und #429, weil sie dieselben Dateien berühren. Bringt einen Test `test_no_py2.py`, der Rückfälle verhindert.
- #434 bis #437 (E9, offene Issues des Originals in vier Blöcken: 1–250, 251–500, 501–700, ab 701; Stufe A): warten auf #431, damit sie auf die Pull-Request-Sichtung verweisen können. Jeder Block schreibt eine eigene Datei unter `docs/inherited-issues/`.

Schätzung Meilenstein 1: von 14 auf 17 Aufgaben angehoben.

**Urteile des Leads (dieser Zyklus).**

- Ruling: E9 nach Nummernbereichen statt nach gezählter Menge geteilt — die Sandbox des Leads erreicht die GitHub-API nicht, die Zahl offener Issues ist unbekannt — Kosten bei Irrtum: ein Block ist zu groß und wird nachträglich geteilt.
- Ruling: E2 hängt zusätzlich an #429 (E4), weil beide `ffmpeg/_view.py` ändern — Kosten bei Irrtum: E2 startet etwas später.

## 17.11.2026, Fundament

**Lage.** Der Projektbrief ist nach zwei Interviewrunden vom Visionär bestätigt. Das Fundament ist am 17.11.2026 auf `master` des Forks gepusht (`5677b37`, `59a699d`): Testvertrag, Umgebung, Projektregeln, Skills, CI und die Projektdateien unter `docs/`. `swarvex env` ist grün: 70 Tests bestanden auf Python 3.13 mit ffmpeg 7.1.5, ohne Netzwerk. Die ersten sechs Aufgaben sind offen: #427 bis #432 (`docs/plan.md`).

**Was passiert ist.**

- Fork `marco8154/ffmpeg-python` geklont; er steht auf `df129c7`, dem letzten Commit des Originals.
- Zwei Tests hingen an der ffmpeg-Version und waren mit ffmpeg 7.1 und 9.0 rot: `test_pipe` und `test__probe`. Beide prüfen jetzt dasselbe Verhalten unabhängig von der Version.
- Die Umgebung kommt aus `.devcontainer/Dockerfile`, weil die Sandbox ein schreibgeschütztes Systemverzeichnis hat und ffmpeg deshalb im Image stecken muss.
- CI neu geschrieben: Python 3.10 bis 3.14 unter Linux, 3.14 unter Windows und macOS. Nach dem Push ist kein Lauf gestartet: GitHub Actions ist auf dem Fork noch nicht eingeschaltet.

**Urteile des Leads.**

- Ruling: Umgebung als Dev-Container statt als `setup` in `swarvex.yaml` — nur so ist ffmpeg in der Sandbox vorhanden — Kosten bei Irrtum: eine Datei umschreiben.
- Ruling: ffmpeg 7.1 aus Debian 13 als feste Version der Pipeline — reproduzierbar und ohne fremde Paketquelle — Kosten bei Irrtum: neue Basis im Dockerfile.
- Ruling: Der Black-Job der alten CI entfällt — er lief mit Black 21.12b0 und Ziel Python 2.7 — Kosten bei Irrtum: Formatprüfung später als eigener Schritt.
- Ruling: Die zwei versionsabhängigen Tests wurden angepasst, nicht übersprungen — `test_pipe` verlangt weiter alle behaltenen Bilder in richtiger Reihenfolge und erlaubt davor nur Kopien des ersten; `test__probe` erlaubt 1 ms Abweichung — Kosten bei Irrtum: Erwartung nachschärfen.

**Risiken.**

- Die Pipeline prüft nur Python 3.13. Die anderen Versionen und Betriebssysteme deckt allein die CI auf GitHub ab.
- Python 3.10 hat im Oktober 2026 sein Lebensende erreicht. Der Visionär hat am 17.11.2026 bestätigt, dass es bleibt (Entscheidung 0002).
- Die Ankündigung in Issue #807 des Originals fehlt weiterhin.

**Offen beim Visionär.**

- GitHub Actions auf dem Fork einschalten (Reiter „Actions“)
- Ankündigung in #807 posten
- ~~Repo umbenennen~~ zurückgenommen: Das Repo heißt seit 17.11.2026, 10:42 UTC, wieder `marco8154/ffmpeg-python`; `ffmpeg-python-ng` leitet dorthin weiter. Der Paketname auf PyPI bleibt `ffmpeg-python-ng`. Entscheidung des Visionärs nach einer Bitte in #807 des Originals.
- Issues auf dem Repo einschalten (Settings → General → Features); auf Forks sind sie ausgeschaltet
- Private Sicherheitsmeldungen im Repo einschalten (Settings → Security), sonst führt der Link aus Aufgabe #432 ins Leere

**Nächste Schritte.**

1. Einreichungen zu #427 bis #432 prüfen.
2. Erledigt: Folgeaufgaben #433 bis #437 angelegt. Wenn #431 gemergt ist: Einstufungen prüfen und Aufgaben für 0.3.1 schneiden.
3. Ersten CI-Lauf prüfen, sobald Actions eingeschaltet ist.
4. E5 (Build über `pyproject.toml`) selbst erledigen, sobald #427 und E2 gemergt sind.
