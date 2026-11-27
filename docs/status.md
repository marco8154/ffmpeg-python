# Status

## 27.11.2026, Zyklus des Lead-Dienstes (warten auf #110 und #122)

**Lage.** Ausgelöst durch die zwei eigenen offenen Approvals (#110, #122) und 0 freie Aufgaben bei 0 aktiven Agenten. #697 ist gemergt (4a24c18); keine Einreichungen offen. Beide Approvals sind unbeantwortet, nichts Neues zu tun.

**Ruling:** Weiter keine Aufgaben auf Vorrat (0 aktive Agenten; alle Kandidaten hängen an #110 oder #122). Wenn falsch: ein Zyklus Verzug.

**Nächste Schritte:** unverändert wie im Eintrag darunter.

*Nachtrag:* Ein weiterer Zyklus mit demselben Anlass (#110 und #122 offen, 0 Agenten, 0 Einreichungen): keine Änderung.

*Nachtrag 2:* Wieder derselbe Anlass (#110 und #122 offen, 0 Agenten, 0 Einreichungen, 0 Funde): keine Änderung.

*Nachtrag 3–8:* Derselbe Anlass (#110 und #122 offen, 0 Agenten, 0 Einreichungen, 0 Funde, 0 Feedback): keine Änderung (zuletzt mehrfach geprüft).

## 27.11.2026, Zyklus des Lead-Dienstes (#697 angenommen, Release-Approval #122)

**Lage.** Ausgelöst durch die geprüfte Einreichung 1036 und die eigene offene Approval #110. 1036 (#697, README `filter_script:v`) ist angenommen: Pipeline grün (140 passed), alle Kriterien erfüllt; wartet auf den Merge-Zug. Damit sind alle Aufgaben der Meilensteine 0.3.0 bis 0.3.2 angenommen. Auf PyPI ist noch nichts veröffentlicht. Der CHANGELOG deckt alle Code-Änderungen von 0.3.2 schon ab.

**Erledigt.** Approval #122 an den Visionär: erstes Release heißt 0.3.0 und enthält alles von master; Entwurf `.github/workflows/release.yml` (Trusted Publishing, Tag `v*`, Environment `pypi`) zum Eintragen durch ihn; danach Tag `v0.3.0` durch ihn.

**Ruling:** Keine Aufgaben auf Vorrat (0 aktive Agenten; Rest hängt an #110 und #122). Wenn falsch: ein Zyklus Verzug.

**Nächste Schritte.**
1. Nach „ja“ zu #122: CHANGELOG `[Unreleased]` und `[0.3.0]` zu `[0.3.0] - <Datum>` zusammenführen, Links unten anpassen, pushen; Visionär taggt. Danach Aufgabe E7 (README: PyPI-Installation als Hauptweg) schneiden.
2. Nach „ja“ zu #110: Meilenstein 0.4.0 anlegen und schneiden (#745, #756/#880, #406, #416, #461/PR #844, #108/#116/PR #783).
3. Schätzung 0.3.2 bleibt 11 (die elfte ist die Release-Vorbereitung des Leads).

## 27.11.2026, Zyklus des Lead-Dienstes (#697 eingereicht, Prüfung läuft)

**Lage.** Ausgelöst durch die eigene offene Approval #110 und 0 freie Aufgaben bei 0 aktiven Agenten. #694 und #696 sind gemergt (2be7b84, 00d5e7b). Einreichung 1036 (#697, README `filter_script:v`) ist inhaltlich geprüft: Satz und Codeblock wörtlich an der richtigen Stelle, Prüfbefehl selbst nachgeführt (`['-i', 'in.mp4', '-filter_script:v', 'filters.txt', 'out.mp4']`), nur README.md. Annehmen ging noch nicht, weil die Plattform-Prüfung läuft.

**Ruling:** Weiter keine Aufgaben auf Vorrat (0 aktive Agenten; übrige Kandidaten hängen an #110). Wenn falsch: ein Zyklus Verzug.

**Nächste Schritte.**
1. 1036 annehmen, sobald die Prüfung grün ist.
2. Nach dem Merge von #697: Release-Vorbereitung 0.3.2 (CHANGELOG, Version, Freigabe durch den Visionär).
3. Nach Antwort auf #110: bei „ja“ Meilenstein 0.4.0 anlegen und schneiden.

## 27.11.2026, Zyklus des Lead-Dienstes (nichts zu tun, Merge-Zug und Visionär)

**Lage.** Ausgelöst durch die eigene offene Approval #110 und 0 freie Aufgaben bei 0 aktiven Agenten. Keine Einreichungen. 1029 (#694) und 1030 (#696) stehen noch im Merge-Zug (main unverändert bei b65700a); #697 bleibt bis zum Merge von #694 blockiert.

**Ruling:** Weiter keine Aufgaben auf Vorrat (0 aktive Agenten; übrige Kandidaten hängen an #110). Wenn falsch: ein Zyklus Verzug.

**Nächste Schritte.** Unverändert wie im Eintrag darunter.

## 27.11.2026, Zyklus des Lead-Dienstes (1029 und 1030 angenommen)

**Lage.** Ausgelöst durch zwei geprüfte Einreichungen, die eigene offene Approval #110 und 0 freie Aufgaben bei 0 aktiven Agenten. 1029 (#694, README-FAQ zu `popen_args` unter Windows) und 1030 (#696, Beispiel Standbild plus Tonspur) sind angenommen: Pipeline grün (140 passed), alle Kriterien erfüllt. Beide warten jetzt auf den Merge-Zug. #697 wird frei, sobald #694 gemergt ist.

**Ruling:** Weiter keine Aufgaben auf Vorrat (0 aktive Agenten; die übrigen Kandidaten ändern `get_args()` und hängen an #110). Wenn falsch: ein Zyklus Verzug beim nächsten Agenten.

**Nächste Schritte.**
1. #697 prüfen, sobald es eingereicht ist.
2. Danach Release-Vorbereitung 0.3.2 (CHANGELOG, Version, Freigabe durch den Visionär).
3. Nach Antwort auf #110: bei „ja“ Meilenstein 0.4.0 anlegen und schneiden.

## 27.11.2026, Zyklus des Lead-Dienstes (#694/#696 eingereicht, warten auf die Prüfung)

**Lage.** Ausgelöst durch die eigene, offene Approval #110 und 0 freie Aufgaben bei 0 aktiven Agenten. Einreichungen 1029 (#694) und 1030 (#696) sind da und am Text gegen die Aufgaben geprüft: beide erfüllen alle Kriterien (Stelle, wörtliche Texte, Prüfausgabe in der Zusammenfassung, nur erlaubte Pfade). Annehmen ging noch nicht, weil die Testpipeline der Plattform sie erst prüft. #697 hängt an #694.

**Ruling:** Weiter keine Aufgaben auf Vorrat (Begründung wie im Eintrag darunter).

**Nächste Schritte.**
1. Nach grüner Prüfung 1029 und 1030 annehmen (inhaltlich schon geprüft, siehe oben).
2. Danach #697 prüfen; dann Release-Vorbereitung 0.3.2.
3. Nach Antwort auf #110: bei „ja“ Meilenstein 0.4.0 anlegen und schneiden.

## 27.11.2026, Zyklus des Lead-Dienstes (nichts zu tun, Merge-Zug und Visionär)

**Lage.** Ausgelöst durch die eigene, offene Approval #110 und 0 freie Aufgaben bei 0 aktiven Agenten. Keine Einreichungen, keine Funde. Die drei offenen Aufgaben (#694, #696, #697) warten nur auf den Merge-Zug (5 angenommene Patches, darunter #683 und #693). Alles weitere für 0.3.2 ist geschnitten; die übrigen Punkte warten auf die Antwort zu #110.

**Ruling:** Keine neuen Aufgaben auf Vorrat. Ohne aktive Agenten bringt Nachschub nichts, und die restlichen Kandidaten ändern `get_args()` (0.4.0, hängt an #110). Wenn falsch: ein Zyklus Verzug beim nächsten Agenten.

**Nächste Schritte:** unverändert wie im Eintrag darunter.

## 27.11.2026, Zyklus des Lead-Dienstes (Nachschub: #695 bis #697 geschnitten)

**Lage.** Ausgelöst durch 0 freie Aufgaben bei 1 aktivem Agenten (arbeitet an #693) und die eigene, offene Approval #110 (wartet weiter auf den Visionär). Keine Einreichungen. #683 und #686 warten auf den Merge-Zug.

**Erledigt.** Wünsche aus Block 5/6 am Code geprüft. #740 (Standbild plus Ton) und #833 (`filter_script:v`) gehen schon heute → #695 (B, Test, sofort frei), #696 (A, Beispiel, hängt an #683), #697 (A, README, hängt an #694). Erwartete Argumentlisten selbst nachgeprüft. Schätzung 0.3.2: 8 → 11.

**Ruling:** #707, #764 und #775 kommen nicht in 0.3.2, weil sie neues Verhalten im Graphen brauchen oder `get_args()` ändern. Wenn das falsch ist, kostet es nur Zeit: geparkt im Plan, nichts verworfen.

**Nächste Schritte.**
1. Einreichungen zu #693, #695, danach #694/#696/#697 prüfen.
2. Nach Antwort auf #110: bei „ja“ Meilenstein 0.4.0 anlegen und schneiden (#745, #756/#880, #406, #416, #461/PR #844, #108/#116/PR #783).
3. Nach 0.3.2: Release-Vorbereitung (CHANGELOG, Approval zum Release an den Visionär).
4. Weiter offen beim Visionär: Rest von #90 und PyPI für E11/E12.

## 27.11.2026, Zyklus des Lead-Dienstes (#658, #683, #686 angenommen; #693/#694 geschnitten)

**Lage.** Ausgelöst durch drei geprüfte Einreichungen. Kein Agent aktiv. Approval #110 (0.3.2 streng kompatibel, Breaking Fixes in 0.4.0) ist weiter offen beim Visionär.

**Erledigt.** Angenommen: #997 (#658, Sichtung Block 6, 78 Issues; Hinweis: #880 hätte `decline` als Duplikat von #756 sein sollen, im Plan zusammengeführt), #999 (#683, RTSP-Beispiel), #1007 (#686, FAQ Flags ohne Wert; Beispiel selbst nachgeprüft). Die Issue-Sichtung ist damit vollständig. Neu geschnitten: #693 (B, `run()` mit `popen_args`, Docstrings von `run()`/`run_async()` ohne falsches `**kwargs`) und #694 (A, README-FAQ, hängt an #693).

**Nächste Schritte.**
1. Einreichungen zu #693 und danach #694 prüfen.
2. Nach Antwort auf #110: bei „ja“ Meilenstein 0.4.0 anlegen und schneiden (#745, #756/#880, #406, #416, #461/PR #844, #108/#116/PR #783).
3. Wünsche aus Block 5/6 (#707, #740, #764, #775, #833) am Code prüfen; nur rein ergänzende kommen in 0.3.2 oder später.
4. Weiter offen beim Visionär: Rest von #90 und PyPI für E11/E12.

## 26.11.2026, Zyklus des Lead-Dienstes (#682 und #685 gemergt)

**Lage.** Ausgelöst durch die eigene, offene Approval #110. Kein Agent aktiv, keine Einreichungen, 3 Aufgaben frei (#658, #683, #686); Engpass laut Metrik: `contributors`. Der Merge-Stau ist aufgelöst.

**Erledigt.** #967 (#682) und #969 (#685) sind gemergt. CHANGELOG-Zeile zu #682 unter `### Changed` ergänzt (Ruling aus dem letzten Eintrag damit erfüllt), Plan aktualisiert. Volle Suite: 133 passed.

**Nächste Schritte.**
1. Einreichungen zu #658, #683, #686 prüfen.
2. Nach Antwort auf #110: bei „ja“ Meilenstein 0.4.0 anlegen und schneiden.
3. Nach #658: restliche Kandidaten aus Block 6 prüfen und schneiden; Schätzung von 0.3.2 (8) anpassen.
4. Weiter offen beim Visionär: Rest von #90 und PyPI für E11/E12.

## 26.11.2026, Zyklus des Lead-Dienstes (#682 und #685 angenommen)

**Lage.** Ausgelöst durch die eigene, offene Approval #110. Kein Agent aktiv, 3 Aufgaben frei (#658, #683, #686). #967 (Aufgabe #682) und #969 (Aufgabe #685) sind im Peer-Review angenommen und warten auf den Merge-Zug (Engpass laut Metrik: `merge`, ältester 1 h). Folgezyklen (ausgelöst durch #110): unverändert, beide warten weiter auf den Merge-Zug (ältester zuletzt 4,4 h), keine Einreichungen. Hält der Merge-Stau über 24 h an, melde ich ihn dem Visionär.

**Ruling:** Die CHANGELOG-Zeile zu #682 schreibe ich erst, wenn #969 gemergt ist — warum: #969 ändert ebenfalls `CHANGELOG.md`, ein Commit von mir davor könnte den Merge-Zug zum Scheitern bringen — Kosten, wenn falsch: ein Zyklus Verzögerung bei einer Doku-Zeile.

**Nächste Schritte.**
1. Nach Merge von #967 und #969: CHANGELOG-Zeile unter `### Changed` ergänzen (TypeError `has no output`, vorher `reduce()`-Fehler bzw. `KeyError`); Plan auf erledigt setzen.
2. Einreichungen zu #658, #683, #686 prüfen.
3. Nach Antwort auf #110: bei „ja“ Meilenstein 0.4.0 anlegen und schneiden.
4. Weiter offen beim Visionär: Rest von #90 und PyPI für E11/E12.

## 26.11.2026, Zyklus des Lead-Dienstes (eigene Einreichungen #967 und #969)

**Lage.** Kein Agent aktiv, 3 Aufgaben frei (#658, #683, #686). Approval #110 (0.4.0 für Fixes, die Argumentlisten ändern) weiter offen.

**Erledigt.**
- #967 (Aufgabe #682, `get_args()` ohne Ausgang) und #969 (Aufgabe #685, `hstack`/`vstack`) sind Einreichungen meiner eigenen Person: geprüft, kein Mangel gefunden, Prüfpunkte gesetzt, sie gehen ins Peer-Review. Pipeline grün (128 bzw. 129 passed), Zeilen ≤ 88.
- Mein Aufgabentext zu #682 war falsch: `ffmpeg.input(...).get_args()` gibt es nicht (`@output_operator`), dort kommt `AttributeError`. Die Tests nutzen richtig `ffmpeg.get_args(...)`/`ffmpeg.compile(...)`. Fund #191 (Methode auf Eingangsströmen) verworfen: neue API, nicht 0.3.2.
- Zur CHANGELOG-Zeile von #682 (sammle ich): für einen Graphen nur mit Filter kam bisher `KeyError`, jetzt `TypeError` mit klarer Meldung; ohne Filter war es schon `TypeError`.

**Nächste Schritte.**
1. Nach Annahme von #967: CHANGELOG-Zeile unter `### Changed` ergänzen (TypeError `has no output`, vorher `reduce()`-Fehler bzw. `KeyError`).
2. Einreichungen zu #658, #683, #686 prüfen.
3. Nach Antwort auf #110: bei „ja“ Meilenstein 0.4.0 anlegen und schneiden.
4. Weiter offen beim Visionär: Rest von #90 und PyPI für E11/E12.

## 26.11.2026, Zyklus des Lead-Dienstes (keine Änderung)

**Lage.** Ausgelöst durch die eigene, offene Approval #110 (0.3.2 streng kompatibel, 0.4.0 für Fixes, die Argumentlisten ändern). Keine Einreichungen, kein Agent aktiv, 5 Aufgaben frei (#658, #682, #683, #685, #686). Die nächsten Schritte des Eintrags „0.3.2 weiter geschnitten“ gelten unverändert.

## 26.11.2026, Zyklus des Lead-Dienstes (0.3.2 weiter geschnitten)

**Lage.** Kein Agent aktiv, keine Einreichungen, keine Nachrichten. Frei sind #658, #682 (seit dem Merge von #681), #683 und neu #685 und #686.

**Erledigt.**
- Kandidaten aus Block 5 am Code geprüft. #745 (doppelte Maskierung von Positionsargumenten in `nodes.py`, Zeilen 284 und 291) und #756 (gleiche `input()` werden ein Knoten) sind echte Fehler. Beide Korrekturen ändern aber die Argumentliste für heute gültige Eingaben.
- Neue Aufgaben: #685 (`hstack`/`vstack`, Level B, Rolle core, Idee aus PR #220) und #686 (README-FAQ zu Flags mit `None`, Level A, Rolle docs, Issue #703). Die erwarteten Argumentlisten habe ich selbst nachgeprüft. Die Pfade überschneiden sich nicht mit #682 und #683.
- Approval #110 an den Visionär: 0.3.2 bleibt streng kompatibel. Fixes, die Argumentlisten ändern (#745, #756, #406, #416, #461/PR #844, stdin), kommen in Meilenstein 0.4.0 mit „Breaking changes“.

**Nächste Schritte.**
1. Einreichungen zu #658, #682, #683, #685 und #686 prüfen.
2. Nach Antwort auf #110: bei „ja“ Meilenstein 0.4.0 anlegen und dort je Punkt eine Aufgabe schneiden. Bei „nein“ bleiben die Punkte geparkt.
3. Nach #658: die restlichen Kandidaten aus Block 6 prüfen und schneiden; die Schätzung von 0.3.2 (8) danach anpassen.
4. Weiter offen beim Visionär: Rest von #90 und PyPI für E11/E12.

## 25.11.2026, Zyklus des Lead-Dienstes (Review #948)

**Lage.** Kein Agent aktiv, 2 Aufgaben frei (#658, #683), #682 wird nach dem Merge von #681 frei. Keine offenen Nachrichten.

**Erledigt.** #948 (Aufgabe #681, `quiet=True` behält Pipes, PR #538) angenommen: selbst nachgeprüft, der neue Test ist auf dem alten Code in genau den Fällen 2–4 rot, mit dem Patch grün; volle Suite 124 passed.

**Nächste Schritte.** Einreichungen zu #658, #682, #683 prüfen; danach die restlichen 0.3.2-Aufgaben aus den Kandidaten in `docs/plan.md`, Meilenstein 3, schneiden (vorher gegen den Code prüfen). Offene Punkte beim Visionär unverändert (Rest von #90, PyPI für E11/E12).

## 25.11.2026, Zyklus des Lead-Dienstes (Review #947)

**Lage.** Ein Agent aktiv, 2 Aufgaben frei, 1 blockiert (#682). Keine offenen Nachrichten. Nur #658 (Issues ab 763) der Sichtung steht noch aus.

**Erledigt.** #947 (Aufgabe #657, Issues 661–762) angenommen: selbst gegen `raw-issues.json` geprüft, 78/78 Zeilen, Datum und Kommentarzahl stimmen in jeder Zeile, Stichproben der Einstufungen stimmen. Kandidaten aus Block 5 (#745, #756, #703, Wünsche #707, #740) in `docs/plan.md`, Meilenstein 3.

**Nächste Schritte.** Wie im Eintrag „Sichtung angenommen, 0.3.2 begonnen“: Einreichungen zu #658 und #681 bis #683 prüfen, danach die restlichen 0.3.2-Aufgaben schneiden.

## 25.11.2026, Zyklus des Lead-Dienstes (Sichtung angenommen, 0.3.2 begonnen)

**Lage.** Ein Agent aktiv, #657/#658 (Issues ab 661) laufen noch. Keine offenen Nachrichten.

**Erledigt.**
- Angenommen: #897 (PRs, #652), #898 (#653), #900 (#654), #902 (#655), #904 (#656). Selbst geprüft gegen die JSON-Exporte: vollständig, sortiert; Datum, Kommentare, Autor und Draft stimmen in allen Zeilen, Summen stimmen. #902 trotz `request_changes` im Peer-Review angenommen: die Beschreibung erlaubt `decline` für „nicht nachvollziehbar“ (#408, #475); der Widerspruch lag in meinem Abnahmekriterium. Künftige Sichtungsaufgaben: Kriterium und Beschreibung gleich formulieren.
- Meilenstein 0.3.2 angelegt (Schätzung 8): #681 (quiet und Pipes, PR #538), #682 (Fund #176, hängt an #681), #683 (RTSP-Beispiel, Issue #310). #684 versehentlich als Duplikat von #682 angelegt und sofort geschlossen.

**Nächste Schritte.**
1. Einreichungen zu #657, #658, #681 bis #683 prüfen.
2. Nach #657/#658: aus allen `bug`/`take-next` die restlichen 0.3.2-Aufgaben schneiden; Kandidaten und offene Entscheidungen in `docs/plan.md`, Meilenstein 3. Die Klassen der Sichtung sind Vorschläge: vor jedem Schnitt gegen den Code prüfen (#656 war kein Fehler).
3. Nach dem Merge von #611: README-Link `## [API reference]` umstellen, sobald die Referenz auf GitHub Pages liegt.
4. Offen beim Visionär: Rest von #90 (Actions, Issues, private Sicherheitsmeldungen, #807), PyPI für E11/E12.

## 24.11.2026, Zyklus des Lead-Dienstes (Sichtung neu geschnitten)

**Lage.** Der Visionär hat #90 und #96/#99 umgesetzt (`cdb986c`): Job `build` in `ci.yml` und der Export der offenen Issues (478) und Pull Requests (46) des Originals unter `docs/inherited-issues/`. Keine Einreichungen, kein Agent aktiv.

**Erledigt.** E8 und E9 offline lösbar neu geschnitten, Quelle die JSON-Dateien, Stichtag 24.11.2026, jede Aufgabe mit einem Prüfbefehl für die Vollständigkeit (fehlende, zusätzliche, doppelte Nummern):
- #652: Pull Requests (46), Einstufung `taken`/`take-next`/`take-later`/`keep-linked`/`decline`; die neun PRs aus `CREDITS.md` sind `taken`.
- #653 bis #658: Issues in sechs Blöcken zu je etwa 80 (1–273, 274–400, 401–530, 531–660, 661–762, ab 763).

**Nächste Schritte.**

1. Einreichungen zu #652 bis #658 prüfen: Prüfbefehl selbst ausführen, Stichproben der Einstufungen gegen die JSON-Datei, keine Platzhalter.
2. Aus `take-next` und `bug` die Aufgaben für 0.3.2 schneiden (je Patch eine Aufgabe mit rotem Test und `Co-authored-by`).
3. Nach dem Merge von #611: README-Link `## [API reference]` umstellen, sobald die Referenz auf GitHub Pages des Forks liegt (Pages-Workflow beim Visionär).
4. Offen beim Visionär: Rest von #90 (Actions, Issues, private Sicherheitsmeldungen, Ankündigung in #807), PyPI für E11/E12.

## 24.11.2026, Zyklus des Lead-Dienstes (keine Änderung, mehrere Zyklen zusammengefasst)

**Lage.** Keine Einreichungen, keine Funde, kein Agent aktiv, keine Aufgabe offen. #90 und #96/#99 (eigene Fragen an den Visionär) weiter unbeantwortet, kein Export unter `docs/inherited-issues/`, kein Job `build` in `ci.yml`. Die nächsten Schritte des Eintrags „#431 geparkt“ gelten unverändert.

## 24.11.2026, Zyklus des Lead-Dienstes (keine Änderung)

**Lage.** Keine Einreichungen, keine Funde, kein Agent aktiv, keine Aufgabe offen. #90 und #96/#99 (eigene Fragen an den Visionär) weiter unbeantwortet, kein Export unter `docs/inherited-issues/`. Restarbeit von 0.3.0 (E8, E9, E11 bis E13) braucht Export, PyPI oder Freigabe des Visionärs; offline schneidbar ist nichts. Die nächsten Schritte des Eintrags „#431 geparkt“ gelten unverändert.

## 24.11.2026, Zyklus des Lead-Dienstes (keine Änderung, #431 geparkt)

**Lage.** Keine Einreichungen, keine Funde, kein Agent aktiv, keine Aufgabe offen. Alles Weitere wartet auf den Visionär: #90 (CI-Job `build`), #96/#99 (Export von Issues und Pull Requests), Pages-Workflow für die Referenz aus #611. Ohne aktive Agenten ist der Vorrat von 0 Aufgaben kein Engpass; offline lösbare Arbeit ohne den Export gibt es nicht. Die nächsten Schritte des Eintrags „#431 geparkt“ gelten unverändert.

## 24.11.2026, Zyklus des Lead-Dienstes (#431 geparkt)

**Lage.** Keine Einreichungen, kein Agent aktiv, keine Aufgabe mehr offen. #90 und #96 beim Visionär weiter unbeantwortet.

**Erledigt.** Ruling: #431 geschlossen (geparkt) — seit 24.11. dreimal ohne Ergebnis zurückgegeben (03:53, 03:54, 06:37), Peer-Review konnte offline nichts prüfen; gleicher Grund wie #612 bis #615 — Kosten bei Irrtum: ein Agent mit Webzugriff findet die Aufgabe nicht; Neuschnitt dauert Minuten. Info #99 an den Visionär: Export bitte auch für Pull Requests (`gh pr list … --json … > docs/inherited-issues/raw-pulls.json`).

**Nächste Schritte.**

1. Liegen `docs/inherited-issues/raw-issues.json` und/oder `raw-pulls.json` vor: #431 und #612 bis #615 offline lösbar neu schneiden (Quelle die JSON-Datei, Stichtag = Exportdatum, Prüffragen über Summen und Einstufungen). Der Text der Einreichung zu #431 (46 Zeilen, Einstufungen) ist als Vergleich nutzbar.
2. Nach dem Merge von #611: README-Link `## [API reference]` umstellen, sobald die Referenz auf GitHub Pages des Forks liegt.
3. Offen beim Visionär: #90 (CI-Job `build`, Actions, Issues, private Sicherheitsmeldungen, #807) und #96/#99 (Export).

## 24.11.2026, Zyklen des Lead-Dienstes (keine Änderung, zuletzt 24.11.)

**Lage.** Keine Einreichungen, keine Funde, kein Agent aktiv, nur #431 offen; die Nacharbeits-Reservierung seines Beitragenden ist am 24.11. 03:54 abgelaufen, die Aufgabe ist jetzt für alle frei. Kein Export unter `docs/inherited-issues/`, kein Job `build` in `ci.yml`: #90 und #96 (meine eigenen Fragen an den Visionär) weiter unbeantwortet. Die nächsten Schritte des Eintrags „Review #820, Issue-Sichtung geparkt“ gelten unverändert.

## 23.11.2026, Zyklus des Lead-Dienstes (keine Änderung)

**Lage.** Keine Einreichungen, keine Funde, kein Agent aktiv, nur #431 offen (Nacharbeit, reserviert bis 24.11. 03:51). Der Zyklus lief wieder wegen #90 und #96, meinen eigenen offenen Fragen an den Visionär. Die nächsten Schritte des Eintrags „Review #820, Issue-Sichtung geparkt“ gelten unverändert.

## 23.11.2026, Zyklus des Lead-Dienstes (keine Änderung)

**Lage.** Keine Einreichungen, kein Agent aktiv, nur #431 offen (Nacharbeit, reserviert bis 24.11. 03:51). Der Zyklus lief wegen #90 und #96, beide meine eigenen Fragen an den Visionär, weiter unbeantwortet. Die nächsten Schritte des Eintrags „Review #820, Issue-Sichtung geparkt“ gelten unverändert.

## 23.11.2026, Zyklus des Lead-Dienstes (Review #820, Issue-Sichtung geparkt)

**Lage.** Kein Agent aktiv. Offen ist nur noch #431 (Nacharbeit, bis 24.11. 03:51 für seinen Beitragenden reserviert). #90 und #96 beim Visionär weiter unbeantwortet.

**Erledigt.**

- #820 (Aufgabe #613) abgelehnt: nur eine Platzhalterdatei „kein Netzwerk“, keine Daten. Die Aufgabe verlangt in diesem Fall die Rückgabe, nicht eine Einreichung.
- Ruling: #612 bis #615 geschlossen (geparkt) — ohne Netzwerk unlösbar, 12 Reservierungen ohne Ergebnis und jetzt Platzhalter-Einreichungen — Kosten bei Irrtum: ein Agent mit Webzugriff findet die Aufgaben nicht; Neuschnitt dauert Minuten. Info an den Visionär gesendet.

**Nächste Schritte.**

1. Liegt der Export aus #96 (`docs/inherited-issues/raw-issues.json`) vor: vier Sichtungsaufgaben offline lösbar neu schneiden (Quelle die JSON-Datei, Stichtag = Exportdatum, Prüffragen über Summen und Einstufungen).
2. Einreichung zur Nacharbeit von #431 prüfen, mit `set_review_points`.
3. Nach dem Merge von #611: README-Link `## [API reference]` umstellen, sobald die Referenz auf GitHub Pages des Forks liegt.
4. Offen beim Visionär: #90 (CI-Job `build`, Actions, Issues, private Sicherheitsmeldungen, #807) und #96 (Issue-Export).

## 23.11.2026, Zyklus des Lead-Dienstes (keine Änderung)

**Lage.** Keine Einreichungen, kein Agent aktiv, 5 Aufgaben frei (#431, #612 bis #615). Der Zyklus lief wegen der Nachrichten #90 und #96; beide sind meine eigenen an den Visionär und weiter unbeantwortet. Nichts zu tun; die nächsten Schritte des vorigen Eintrags gelten unverändert.

## 23.11.2026, Zyklus des Lead-Dienstes (Rückgaben #615, Export angefragt)

**Lage.** Keine Einreichungen, keine Funde, kein Agent aktiv; 5 Aufgaben frei (#431, #612 bis #615). Der Zyklus lief wegen Nachricht #90 (meine eigene an den Visionär, weiter offen).

**Beobachtet.** Auch #615 wurde zweimal ohne Ergebnis zurückgegeben (21:56, 22:04). Rolle `upstream`: 11 Reservierungen ohne Ergebnis. Das Muster ist eindeutig; Warten bis 26.11. bringt nichts.

**Erledigt.** Nächsten Schritt vorgezogen: Nachricht #96 an den Visionär, Export der offenen Issues mit `gh issue list … --json` nach `docs/inherited-issues/raw-issues.json`.

**Nächste Schritte.**

1. Bei „ja“ und vorliegendem Export: #612 bis #615 schließen und offline lösbar neu schneiden (Quelle die JSON-Datei, Stichtag = Exportdatum, Prüffragen über Summen und Einstufungen).
2. Einreichungen zu #612 bis #615 und zur Nacharbeit von #431 prüfen, mit `set_review_points`.
3. Nach dem Merge von #611: README-Link `## [API reference]` umstellen, sobald die Referenz auf GitHub Pages des Forks liegt.
4. Offen beim Visionär: #90 (CI-Job `build`, Actions, Issues, private Sicherheitsmeldungen, #807) und #96 (Issue-Export).

## 23.11.2026, Zyklus des Lead-Dienstes (Rückgaben #613)

**Lage.** Keine Einreichungen, keine Funde, kein Agent aktiv; 5 Aufgaben frei (#431, #612 bis #615), `bottleneck`: Mitwirkende. Der Zyklus lief wegen Nachricht #90; sie ist meine eigene an den Visionär und weiter offen.

**Beobachtet.** #613 wurde zweimal ohne Ergebnis zurückgegeben (21:17 und 21:26, „finished without changing the allowed paths“). Wahrscheinlich liefen beide Agenten in einer Sandbox ohne Netzwerk; die Aufgabe verlangt genau dann die Rückgabe. Selbst einspringen kann ich nicht: Weder die Sandbox des Lead-Dienstes noch WebFetch erreichen github.com (keine Namensauflösung), und Issues liegen nicht in Git-Refs. Ruling: #612 bis #615 bleiben unverändert — sie brauchen Mitwirkende mit Webzugriff (direkt verbundene Agenten, `daten`/`text.en`) — Kosten bei Irrtum: weitere Leerläufe von Runner-Agenten, sichtbar an den Rückgaben.

**Nächste Schritte.**

1. Gibt es bis zum 26.11. weiter nur Rückgaben ohne Ergebnis: beim Visionär einen Export der vier Issue-Listen als Rohdaten anfragen (Nummer, Titel, zuletzt geändert, Kommentare, Text); die Einstufung wird dann eine offline lösbare Aufgabe.
2. Einreichungen zu #612 bis #615 und zur Nacharbeit von #431 prüfen, mit `set_review_points` (Struktur, Summen, Einstufungen).
3. Nach dem Merge von #611: README-Link `## [API reference]` umstellen, sobald die Referenz auf GitHub Pages des Forks liegt.
4. Offen beim Visionär: Nachricht #90 (CI-Job `build`, Actions, Issues, private Sicherheitsmeldungen, #807); danach Workflow für Sphinx und GitHub Pages vorschlagen. E11 braucht ihn auf PyPI.

## 23.11.2026, Zyklus des Lead-Dienstes (Issue-Sichtung entkoppelt)

**Lage.** Keine Einreichungen, keine Funde, kein Agent aktiv. Der Zyklus lief wegen Nachricht #90; sie ist meine eigene an den Visionär und weiter offen. 0.3.1 ist zu 100 % fertig. Die vier „unberührten“ `upstream`-Aufgaben waren nicht unklar, sondern nur blockiert: Sie warteten auf #431, das bis 24.11. 03:51 für die Nacharbeit seines Beitragenden reserviert ist.

**Erledigt.**

- Ruling: Issue-Sichtung hängt nicht mehr an #431 — sie braucht die PR-Liste nicht, „fixed“ verweist jetzt auf `CHANGELOG.md`/`CREDITS.md`, die seit 0.3.1 alle übernommenen Patches führen — Kosten bei Irrtum: ein Issue verweist auf die Changelog-Zeile statt auf die PR-Nummer, nachträglich ergänzbar.
- #434 bis #437 geschlossen, ersetzt durch #612 bis #615 (gleiche Pfade, ohne `depends_on`, dazu „Abfrage über der Tabelle angeben“, damit Prüfer ohne Rätsel nachprüfen können). Damit sind vier Aufgaben sofort frei.

**Nächste Schritte.**

1. Einreichungen zu #612 bis #615 und zur Nacharbeit von #431 prüfen. Peer-Reviewer haben oft kein Netzwerk: beim Eingang mit `set_review_points` offline prüfbare Fragen setzen (Struktur, Summen, Einstufungen) und die Fakten stichprobenartig selbst bestätigen, soweit ich github.com erreiche.
2. Nach dem Merge von #611: README-Link `## [API reference]` umstellen, sobald die Referenz auf GitHub Pages des Forks liegt.
3. Workflow für Sphinx-Build und GitHub Pages dem Visionär vorschlagen, sobald #90 beantwortet ist (Lead-Token darf `.github/workflows/` nicht pushen).
4. Offen beim Visionär: Nachricht #90 (CI-Job `build`, Actions, Issues, private Sicherheitsmeldungen, #807); E11 braucht ihn auf PyPI.

## 23.11.2026, Zyklus des Lead-Dienstes (Review #802, 0.3.1 fertig)

**Lage.** Kein Agent aktiv, `bottleneck`: Mitwirkende. Alle 14 Aufgaben von 0.3.1 sind angenommen; Schätzung auf 14 gesetzt (100 %). Offen bleiben die fünf Aufgaben der Rolle `upstream` in 0.3.0 (vier seit über drei Tagen unberührt). Nachricht #90 an den Visionär ist weiter offen.

**Erledigt.** #802 (Aufgabe #611, Sphinx-Referenz, Docstrings `Error`/`view`) angenommen. Rot-Lauf selbst nachgeholt: `test_every_public_name_has_docstring` auf `6acc06d` rot, fehlend genau `Error` und `view`; mit Patch 119 Tests grün (Pipeline).

**Nächste Schritte.**

1. Nach dem Merge von #611: Im README zeigt `## [API reference]` noch auf `kkroening.github.io/ffmpeg-python`; umstellen, sobald die Referenz auf GitHub Pages des Forks liegt.
2. Workflow für Sphinx-Build und GitHub Pages dem Visionär vorschlagen, sobald #90 beantwortet ist (Lead-Token darf `.github/workflows/` nicht pushen).
3. Die unberührten `upstream`-Aufgaben in 0.3.0 prüfen: zu groß oder unklar? Gegebenenfalls kleiner schneiden.
4. #431 nach der Wiedereinreichung mit offline prüfbaren Prüffragen versehen.
5. Offen beim Visionär: Nachricht #90 (CI-Job `build`, Actions, Issues, private Sicherheitsmeldungen, #807); E11 braucht ihn auf PyPI.

## 23.11.2026, Zyklus des Lead-Dienstes (Sphinx-Referenz geschnitten)

**Lage.** Keine Einreichungen, keine Funde, kein Agent aktiv; `bottleneck`: Mitwirkende. #608 ist gemergt (`caf7541`), 116 Tests grün. Der Zyklus lief wegen Nachricht #90; sie ist meine eigene an den Visionär und weiter offen.

**Erledigt.**

- `CHANGELOG.md`: unter `[Unreleased]` → `### Fixed` die Zeile für #609 (`repr()` of a node no longer raises `TypeError`).
- Sphinx-Referenz als #611 geschnitten (Stufe B, Rolle docs): `doc/src/conf.py` und `index.rst` auf ffmpeg-python-ng, Docstrings für `Error` und `view`, Test `test_doc_reference.py`. #610 geschlossen, weil ich dort `tomllib` vorgeschrieben hatte (erst ab Python 3.11).
- Korrektur zum letzten Status: Sphinx ist in der Sandbox nicht installiert, ein Build ist hier nicht prüfbar. Deshalb prüft #611 nur `conf.py`, `index.rst` und Docstrings über pytest.

Lehre: In Testvorgaben nur die Standardbibliothek von Python 3.10 verwenden.

**Nächste Schritte.**

1. Einreichung zu #611 prüfen; danach ist 0.3.1 bis auf die Veröffentlichung der Referenz fertig. Die Schätzung (15) dann auf die tatsächliche Zahl setzen.
2. Für Sphinx-Build und GitHub Pages braucht es einen Workflow: nach Antwort auf #90 dem Visionär vorschlagen.
3. #431 nach der Wiedereinreichung mit offline prüfbaren Prüffragen versehen.
4. Offen beim Visionär: Nachricht #90 (CI-Job `build`, Actions, Issues, private Sicherheitsmeldungen, #807); E11 braucht ihn auf PyPI.

## 23.11.2026, Zyklus des Lead-Dienstes (Review #800)

**Lage.** Kein Agent aktiv, `bottleneck`: Mitwirkende. Alle 13 geplanten Aufgaben von 0.3.1 sind angenommen; offen für den Meilenstein bleibt die Sphinx-Referenz (Schätzung bleibt 15). Keine Funde, kein Feedback. Nachricht #90 an den Visionär ist weiter offen.

**Erledigt.** #800 (Aufgabe #608, `CHANGELOG.md` und `CREDITS.md`) angenommen: zehn Tabellenzeilen und elf Changelog-Einträge wortgleich mit der Aufgabe, Linkreferenz repariert, 116 Tests grün.

**Nächste Schritte.**

1. Nach dem Merge von #608: unter `[Unreleased]` → `### Fixed` eine Zeile für #609 ergänzen (`repr()` of a node no longer raises `TypeError`); eigene kleine Änderung des Leads, #608 durfte nichts dazuerfinden.
2. Sphinx-Referenz für 0.3.1 schneiden (Build lokal prüfbar; Veröffentlichung auf GitHub Pages braucht einen Workflow, also den Visionär).
3. #431 nach der Wiedereinreichung mit offline prüfbaren Prüffragen versehen.
4. Offen beim Visionär: Nachricht #90 (CI-Job `build`, Actions, Issues, private Sicherheitsmeldungen, #807); E11 braucht ihn auf PyPI.

## 23.11.2026, Zyklus des Lead-Dienstes (Nachricht #90, Routine)

**Lage.** Keine Einreichungen, keine Funde, kein Feedback, kein Agent aktiv; `bottleneck`: Mitwirkende. #444, #607 und #609 sind gemergt (`f9824de`, `56960e4`, `4d42f22`); auf `4d42f22` sind 116 Tests grün. Damit ist #608 (`CREDITS.md`/`CHANGELOG.md`) frei. Der Zyklus lief wegen Nachricht #90; sie ist meine eigene an den Visionär und weiter offen, zu beantworten gab es nichts.

**Nächste Schritte.**

1. Einreichung zu #608 prüfen: alle zehn übernommenen Patches mit Autor und Original-PR in `CREDITS.md`.
2. #431 nach der Wiedereinreichung mit offline prüfbaren Prüffragen versehen.
3. Offen beim Visionär: Nachricht #90 (CI-Job `build`, Actions, Issues, private Sicherheitsmeldungen, #807); E11 braucht ihn auf PyPI.

## 23.11.2026, Zyklus des Lead-Dienstes (Review #787, #446 neu geschnitten)

**Lage.** Kein Agent aktiv, `bottleneck` laut `metrics`: Mitwirkende. Antwortzeit 0,1 h. Die einzige offene Nachricht ist weiter meine eigene an den Visionär (#90).

**Erledigt.**

- #787 (Aufgabe #441, `topo_sort` ohne Rekursion) angenommen. Nachgeprüft auf `d128fa6`: `test_chain_2000_filters` ohne Fix rot (`RecursionError`), mit Fix 103 Tests grün. Alte und neue Fassung liefern auf 3000 zufälligen DAGs identische `sorted_nodes` und `outgoing_edge_maps`.
- Schnittfehler behoben: #446 war in der Pipeline rot, weil `test_probe_input.py::test_probe_signature` (aus #445) die alte Signatur von `probe()` festhält und nicht in den Pfaden stand. #446 geschlossen, ersetzt durch #607 (Pfade mit `test_probe_input.py`, genau eine Zeile `'capture_stderr',` erlaubt). #606 geschlossen, ersetzt durch #608 (gleicher Inhalt, wartet auf #607). Fund #156 damit erledigt.
- Fund #157 (`DagNode.__repr__(self, other)`, `repr()` wirft `TypeError`) nachgeprüft und als #609 (Stufe B, nach #441) geschnitten. Schätzung 0.3.1 auf 15 Aufgaben.

Lehre: Wenn eine Aufgabe eine öffentliche Signatur ändert, alle Tests, die diese Signatur festhalten, in die Pfade aufnehmen (`grep -rn "signature(ffmpeg.<name>"`).

**Nächste Schritte.**

1. Einreichungen zu #444, #607 und #609 prüfen.
2. #431 nach der Wiedereinreichung mit offline prüfbaren Prüffragen versehen.
3. Offen beim Visionär: Nachricht #90 (CI-Job `build`, Actions, Issues, private Sicherheitsmeldungen, #807); E11 braucht ihn auf PyPI.

## 23.11.2026, Zyklus des Lead-Dienstes (Review #785)

**Lage.** Ein Agent ist aktiv, zwei Aufgaben sind frei, sechs blockiert; Antwortzeit 0,1 h, `bottleneck` leer, keine Bereichslead-Empfehlung. Die einzige offene Nachricht ist meine eigene an den Visionär (#90).

**Erledigt.** #785 (Aufgabe #443, `explicit_maps`, Patch von Artem Eltyshev) angenommen. Nachgeprüft auf `831d7cb`: neue Tests ohne Fix 5 failed, 1 passed; mit Fix 107 Tests grün; Aufrufe mit Positionsargumenten unverändert. Nach dem Merge startet #444 (`popen_args`) von selbst.

**Nächste Schritte.**

1. Einreichungen zu #441, #444 und #446 prüfen.
2. #431 nach der Wiedereinreichung mit offline prüfbaren Prüffragen versehen.
3. Offen beim Visionär: Nachricht #90 (CI-Job `build`, Actions, Issues, private Sicherheitsmeldungen, #807); E11 braucht ihn auf PyPI.

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
