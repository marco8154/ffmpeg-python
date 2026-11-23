# Status

## 23.11.2026, Zyklus des Lead-Dienstes (Docstring `atrim`)

**Lage.** Keine Einreichungen, keine Funde. Ein Agent ist aktiv (an #443), drei Aufgaben sind frei, sechs blockiert. `bottleneck` ist leer, die Antwortzeit liegt bei 0,1 h. Der Zyklus lief wegen Nachricht #90. Sie ist meine eigene an den Visionär und weiter offen; zu beantworten gab es nichts.

**Erledigt.** Im Docstring von `atrim` beschreibt `end` jetzt „first audio sample“ statt „first frame“ (Nachtrag zu #450). 101 Tests grün.

**Nächste Schritte.**

1. Einreichungen zu #441, #443, #444 und #446 prüfen.
2. #431 nach der Wiedereinreichung mit offline prüfbaren Prüffragen versehen.
3. Offen beim Visionär: Nachricht #90 (CI-Job `build`, Actions, Issues, private Sicherheitsmeldungen, #807); E11 braucht ihn auf PyPI.

## 23.11.2026, Zyklus des Lead-Dienstes (Reviews #779 bis #783)

**Lage.** Die Aufgaben für 0.3.1 laufen weiter. Ein Agent ist aktiv (an #446), drei Aufgaben sind frei, fünf blockiert. Die Antwortzeit liegt bei 0,1 h, `bottleneck` ist leer. Keine Funde, kein Feedback.

**Erledigt.**

- Angenommen: #779 (Aufgabe #447, Pfadobjekte), #780 (#448, FIPS), #781 (#449, relativer Import), #782 (#450, `atrim`) und #783 (#605, `CHANGELOG.md`). Alle vier Code-Patches habe ich zusammen auf `7009cf9` nachgeprüft: Die neuen Tests sind ohne die Fixes rot (7 failed), mit den Fixes sind 101 Tests grün. `str`-, `bytes`- und `pipe:`-Dateinamen ergeben die gleiche Argumentliste wie vorher.
- Fund: Der Merge-Bot schreibt keine `Co-authored-by`-Zeilen in die Commits (`a2c0177`, `549b513`, `7009cf9`). Deshalb gibt es jetzt Aufgabe #606 (Stufe A): Sie trägt alle zehn übernommenen Patches in die Tabelle in `CREDITS.md` ein, ergänzt die 0.3.1-Einträge unter `[Unreleased]` und repariert den Link `[Unreleased]` (`compare/...` führt ins Leere; das ging auf meine Formulierung in #605 zurück). Sie startet von selbst, wenn #605 und alle 0.3.1-Patches gemergt sind. Den Visionär habe ich informiert (Nachricht #91, Empfehlung: Wunsch an die Plattform).

Ruling: Autoren der übernommenen Patches in `CREDITS.md` statt die Historie neu zu schreiben — `master` ist öffentlich, ein Force-Push bräche jeden Klon — Kosten bei Irrtum: GitHub zeigt die Autoren nicht als Co-Autoren an.

**Nächste Schritte.**

1. Wenn #450 gemergt ist: Im Docstring von `atrim` bei `end` „first audio sample“ statt „first frame“ schreiben (eigene kleine Änderung des Leads).
2. Einreichungen zu #441, #443, #444 und #446 prüfen.
3. #431 nach der Wiedereinreichung mit offline prüfbaren Prüffragen versehen.
4. Offen beim Visionär: Nachricht #90 (CI-Job `build`, Actions, Issues, private Sicherheitsmeldungen, #807); E11 braucht ihn auf PyPI.

## 23.11.2026, Zyklus des Lead-Dienstes (Reviews #776 bis #778)

**Lage.** Die Aufgaben für 0.3.1 laufen: Ein Agent ist aktiv, zwei Personen haben in diesem Zyklus eingereicht. Die einzige offene Nachricht ist meine eigene an den Visionär (#90, CI-Job `build`).

**Erledigt.**

- #776 (Aufgabe #442, Stream-Selektor 0), #777 (#440, `topo_sort` mit Mengen) und #778 (#445, `probe(input=...)`) angenommen. Alle drei habe ich auf `9b759be` nachgeprüft: Die neuen Tests sind ohne Fix rot, und mit allen drei Patches zusammen sind 92 Tests grün. Nach dem Merge starten #443, #441 und #446 von selbst.
- E7 geschnitten: Aufgabe #605 (`CHANGELOG.md` für 0.3.0, Stufe A, `text.en`). Die acht Fakten stehen in der Aufgabe. 0.2.0 ist auf den 06.07.2019 datiert (UTC, Commit „Release 0.2.0“).

**Warten auf die Prüfung.** #779 (#447, Pfadobjekte) und #780 (#448, FIPS, Stufe A, geht nach zwei Peer-Freigaben automatisch durch). Bei #779 im Review prüfen: `output(filename=None)` und Dateinamen, die keine Pfade sind, wie `pipe:`.

**Nächste Schritte.**

1. #779 und #780 prüfen, sobald sie `checked_ok` sind.
2. #431 nach der Wiedereinreichung mit offline prüfbaren Prüffragen versehen (siehe Eintrag unten).
3. E11 (Release-Workflow) braucht den Visionär auf PyPI. Offen beim Visionär ist weiter Nachricht #90 (CI-Job `build`, Actions, Issues, private Sicherheitsmeldungen, #807).

## 23.11.2026, Zyklus des Lead-Dienstes (Review #775, E5)

**Lage.** #774 (Aufgabe #429) ist gemergt (`a2c0177`). Kein Agent aktiv, keine Nachrichten, keine Funde. Engpass laut `metrics`: Mitwirkende.

**Erledigt.**

- #775 (Aufgabe #433, E2, Python-2-Reste aus dem Paket) angenommen. Nachgeprüft auf `a2c0177`: `test_no_py2.py` vorher rot (8 failed, 1 passed), nachher grün; 84 Tests grün; `__all__` bleibt bei 27. Gemergt als `5c006b3`; damit sind #440, #442, #445, #447, #448, #449 und #450 frei. Auf `5c006b3` mit gesperrtem `future`: 84 Tests grün.
- E5 selbst erledigt (Aufgabe #604): `pyproject.toml` (setuptools ≥ 77, `ffmpeg-python-ng` 0.3.0, keine Abhängigkeiten, `requires-python = ">=3.10"`, Lizenz als SPDX-Ausdruck), `setup.py`, `setup.cfg`, `tox.ini`, `MANIFEST`, `requirements.txt` entfernt, `future` aus dem Dockerfile. Den CI-Job `build` (sdist, Wheel, `twine check --strict`, Wheel ohne `future` installieren) darf der Lead-Dienst nicht pushen (keine Rechte auf `.github/workflows/`); er ging als Text an den Visionär. Tests laufen mit gesperrtem `future` grün (75 auf `a2c0177`).

Ruling: E5 vor dem Merge von #433 umgesetzt — E5 berührt kein `ffmpeg/`, und die verbliebenen Importe (`builtins`, `__future__`) sind Standardbibliothek, laufen also ohne `future` — Kosten bei Irrtum: Pipeline rot bis zum Merge von #433.

**Risiko.** Den Build kann ich in der Sandbox nicht prüfen (kein setuptools, kein Netzwerk für pip). Ob `pyproject.toml` baut, zeigt erst der CI-Job `build`. Er läuft, wenn der Visionär ihn einträgt und Actions auf dem Fork einschaltet; bis dahin prüft der bestehende Job `pip install -e .` den Build zumindest teilweise.

**#431 (PR-Sichtung) in Nacharbeit.** Der Peer-Reviewer (nevs84) hatte kein Netzwerk und konnte die 46 Zeilen nicht gegen GitHub prüfen; strukturell fand er alles in Ordnung, nur bei #625 soll der Grund eine der drei Regeln nennen. Die Aufgabe liegt 24 h beim Runner des Visionärs. Wenn sie wieder eingereicht ist: Prüffragen setzen, die offline prüfbar sind (Struktur, Summen, Regel je `decline`), und im Hinweis sagen, dass ich die `take-0.3.1`-Diffs am 17.11. selbst per `git fetch` gelesen habe.

**Nächste Schritte.**

1. Die freigegebenen Aufgaben (#440, #442 …) beobachten, Einreichungen prüfen.
2. Wiedereinreichung von #431 mit Prüffragen versehen (siehe oben).
3. E7 (`CHANGELOG.md`) und E11 (Release-Workflow) als Nächstes schneiden bzw. selbst machen; E11 braucht den Visionär auf PyPI.
4. Offen beim Visionär: CI-Job `build` in `.github/workflows/ci.yml` eintragen (Nachricht vom 23.11.); unverändert Actions, Issues und private Sicherheitsmeldungen einschalten, Ankündigung in #807.

## 23.11.2026, Zyklus des Lead-Dienstes (Review #774)

**Lage.** Der Engpass bei der Peer-Review hat sich gelöst: #543 (Aufgabe #427, `future` entfernt) und #549 (#428, Testdatei) sind nach Peer-Review (nevs84) gemergt (`815aa2c`, `56ef339`). Drei Personen und vier Agenten haben inzwischen beigetragen. Keine Nachrichten, keine Funde.

**Erledigt.** #774 (Aufgabe #429, `mkstemp` statt `mktemp` in `view()`, übernommener Patch von Sarthak Munshi) angenommen. Ich habe den Patch auf `56ef339` nachgeprüft: 75 Tests grün, der neue Test ist ohne den Fix rot. Die Einreichung wartet auf den Merge. Danach startet #433 (E2) von selbst, weil es nur an #427 und #429 hängt.

**Hinweis Scorecard.** `area_lead_recommendation` nennt core, upstream und quality. Grund sind Antwortzeiten über 24 h, die aus dem Peer-Review-Stau vom 17. bis 22.11. kommen. Jetzt wartet nichts mehr. Die Lead-Position „core“ (#3) bleibt offen.

**Nächste Schritte.**

1. Einreichung zu #433 prüfen, sobald sie da ist.
2. Wenn #433 gemergt ist: E5 (Build über `pyproject.toml`) selbst erledigen. `setup.py` und `requirements.txt` nennen noch `future` (Fund #106).
3. Was beim Visionär offen ist, steht unverändert im Abschnitt „Fundament“ unten.

## 21.11.2026, Zyklus des Lead-Dienstes (Plattformhinweis)

**Lage.** Plattformnachricht #85: Einreichungen warten länger als einen Tag, mehr Lead-Kraft würde helfen. Unverändert warten #543, #545 und #549 auf eine Peer-Review (älteste 96,7 h), 16 Aufgaben blockiert, kein Agent aktiv.

**Erledigt.** Lead-Position „core“ (`ffmpeg/**`, Position #3) geöffnet; ein Bereichslead als andere Person darf die wartenden Einreichungen prüfen. Dem Visionär den Link zum Teilen geschickt (Nachricht #87), #85 beantwortet.

Ruling: Keine zweite Lead-Instanz unter dem Konto des Visionärs — sie dürfte dessen eigene Einreichungen ebenfalls nicht annehmen — Kosten bei Irrtum: keine.

**Nächste Schritte.** Bewerbung abwarten (entscheidet der Visionär); sonst unverändert die Liste vom 17.11. (unten).

## 18. bis 20.11.2026, Routinezyklen des Lead-Dienstes (2 bis 9)

**Lage.** Unverändert: keine Nachrichten, keine Funde, kein Feedback, kein Agent aktiv. #543, #545 und #549 warten auf eine Peer-Review (älteste laut `metrics` am 20.11.: 76,6 h). `matching_tasks` hält auch #429 für Runner des Visionärs zurück, solange dessen eigene Arbeit auf Reviews wartet, die niemand übernehmen kann. Damit ist ohne eine zweite Person mit Vertrauensstufe 1 (andere Modellfamilie, in den letzten 24 Stunden aktiv) keine Aufgabe bearbeitbar. Nachricht #63 an den Visionär ist weiter unbeantwortet; ich schicke keine zweite. Routinezyklen ohne neue Lage ändern künftig nur diesen Eintrag.

**Erledigt (Zyklus 6).** E14 selbst gemacht, weil es an nichts hängt: Formular für Fehlerberichte und `config.yml` mit Link auf private Sicherheitsmeldungen unter `.github/ISSUE_TEMPLATE/` (Aufgabe #556). Wirkt erst, wenn der Visionär Issues auf dem Repo einschaltet.

**Nächste Schritte.** Unverändert die Liste vom 17.11. (unten).

## 18.11.2026, Routinezyklus des Lead-Dienstes

**Lage.** Unverändert seit gestern Abend: keine Nachrichten, keine Funde, kein Feedback, kein Agent aktiv. #543, #545 und #549 warten seit 21 Stunden auf eine Peer-Review. Alle drei kommen vom Konto des Visionärs, also kann nur eine andere Person mit Vertrauensstufe 1 sie freigeben. Frei ist nur #429, 16 Aufgaben sind blockiert. Dem Visionär habe ich den Engpass gemeldet (Nachricht #63) und vorgeschlagen, in #807 des Originals um Reviewer zu werben.

**Nächste Schritte.** Unverändert die Liste vom 17.11. (unten).

## 17.11.2026, Routinezyklus des Lead-Dienstes

**Lage.** Keine Nachrichten, keine Funde, kein Feedback, kein Agent aktiv. Neu eingereicht: #549 (Aufgabe #428, Testdatei ohne Python-2-Reste, 70 Tests grün, beide Warnungen weg). Sie stammt wie #543 und #545 vom Konto des Visionärs; ich habe den Patch gegen alle sechs Vorgaben geprüft, keinen Fehler gefunden und fünf Prüffragen für die Peer-Review gesetzt. Engpass laut `metrics`: Peer-Review (drei Einreichungen warten, die älteste seit 7,6 Stunden); verfügbar ist nur eine Aufgabe (#429), 16 sind blockiert, bis #427 und #431 gemergt sind.

**Risiko.** Solange keine zweite Person mit Vertrauensstufe 1 reviewt, steht der kritische Pfad (E1 → E2 → E5). Mehr Mitwirkende sind der Hebel, nicht neue Aufgaben: Weitere Aufgaben auf `ffmpeg/*.py` würden mit den wartenden kollidieren.

**Nächste Schritte.** Unverändert die Liste aus dem vorigen Zyklus (unten).

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
