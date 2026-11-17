# 0003: Den PyPI-Namen `ffmpeg-python` nach PEP 541 beantragen, nach dem ersten Release

- Datum: 17.11.2026
- Entschieden von: Visionär (Empfehlung des Leads angenommen)
- Status: gilt; ergänzt Entscheidung 0002

## Zusammenhang

Nach Entscheidung 0002 erscheint die Fortführung auf PyPI als `ffmpeg-python-ng`, weil der Name `ffmpeg-python` dem Maintainer des Originals gehört. Am 17.11.2026 hat der Nutzer milahu in Issue #807 des Originals vorgeschlagen, bei PyPI die Übertragung des Namens zu beantragen.

PyPI regelt das über PEP 541 („Package Index Name Retention“): Ein Name kann übertragen werden, wenn das Projekt aufgegeben ist und der Antragsteller die Pflege nachweislich übernimmt. Die Admins versuchen selbst, den Besitzer zu erreichen. Anträge gehen als Issue an https://github.com/pypi/support und liegen erfahrungsgemäß lange.

## Entscheidung

1. Das erste Release 0.3.0 erscheint wie geplant als `ffmpeg-python-ng`. Es wartet nicht auf PyPI.
2. Der Visionär stellt den Antrag nach PEP 541 für `ffmpeg-python`, wenn beides erfüllt ist:
   - 0.3.0 ist als `ffmpeg-python-ng` auf PyPI veröffentlicht, und
   - der Maintainer hat in #807 mindestens 30 Tage nach der Ankündigung (17.11.2026) nicht geantwortet, also frühestens am 17.12.2026.
3. Der Antrag verweist auf #807, auf dieses Repository und auf das Release.
4. Wird der Name übertragen, erscheint dasselbe Paket zusätzlich unter `ffmpeg-python`. Wie die beiden Namen danach zueinander stehen, ist eine eigene Entscheidung.

## Alternativen

- Antrag sofort stellen: Die Fortführung ist einen Tag alt und hat noch kein Release; der Maintainer wurde erst am selben Tag angeschrieben. Der Antrag wäre schwächer und könnte wie Drängeln wirken.
- Auf den Namen warten und erst dann veröffentlichen: hält das Release für unbestimmte Zeit auf.
- Keinen Antrag stellen: Die meisten Nutzer installieren weiter `ffmpeg-python` mit `future` und erfahren nie von der Fortführung.

## Folgen

- Bis zur Übertragung gilt Entscheidung 0002 unverändert.
- Ein Release unter `ffmpeg-python` erreicht sehr viele Installationen, auch automatische. Bevor eines erscheint, muss die CI auf allen unterstützten Python-Versionen grün sein, und der Visionär gibt es ausdrücklich frei.
- Antwortet der Maintainer und will übergeben oder Mitmaintainer aufnehmen, entfällt der Antrag (Projektbrief, F8).
