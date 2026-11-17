# Status

## 17.11.2026

**Lage.** Der Projektbrief ist nach zwei Interviewrunden vom Visionär bestätigt. Das Fundament ist am 17.11.2026 auf `master` des Forks gepusht (`5677b37`, `59a699d`): Testvertrag, Umgebung, Projektregeln, Skills, CI und die Projektdateien unter `docs/`. `swarvex env` ist grün: 70 Tests bestanden auf Python 3.13 mit ffmpeg 7.1.5, ohne Netzwerk. Aufgaben sind noch keine angelegt.

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
- Repo in `ffmpeg-python-ng` umbenennen
- Grundausstattung bestätigen (Vorschlag steht im Projektbrief)

**Nächste Schritte.**

1. Grundausstattung bestätigen lassen.
2. Ersten CI-Lauf prüfen, sobald Actions eingeschaltet ist.
3. Aufgaben E1, E3, E4, E6, E8, E10 anlegen (`docs/plan.md`).
