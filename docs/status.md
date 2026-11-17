# Status

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
- Python 3.10 hat im Oktober 2026 sein Lebensende erreicht. Der Brief nennt es trotzdem als älteste unterstützte Version.
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
