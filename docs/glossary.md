# Glossar

Ein Begriff pro Sache. Aufgaben und Reviews verwenden die Begriffe wörtlich.

| Begriff | Bedeutung |
|---|---|
| **Original** | das Projekt `kkroening/ffmpeg-python`, letzter Commit `df129c7`, letztes Release 0.2.0 |
| **Fortführung** | dieses Projekt, `ffmpeg-python-ng` |
| **öffentliche API** | alle Namen in `ffmpeg.__all__` mit ihren Signaturen |
| **Argumentliste** | die Liste von Zeichenketten, die `get_args()` liefert und die an das Programm `ffmpeg` geht |
| **Graph** | die Verkettung aus Eingaben, Filtern und Ausgaben, die der Nutzer aufbaut |
| **Knoten** | ein Element des Graphen: `InputNode`, `FilterNode`, `OutputNode`, `GlobalNode`, `MergeOutputsNode` |
| **Datenstrom** | ein Objekt der Klasse `Stream`: der Ausgang eines Knotens, auf dem der Nutzer weiterarbeitet |
| **Filter** | eine Funktion aus `ffmpeg/_filters.py`, die einen `FilterNode` anlegt |
| **übernommener Patch** | eine Änderung aus einem Pull Request des Originals oder aus einem Fork, die mit ihrem Autor in die Fortführung kommt |
| **Testvertrag** | `swarvex.yaml` zusammen mit `.devcontainer/`: die Umgebung und das Kommando, die jede Einreichung bestehen muss |
| **Vorauswahl** | die Pull Requests aus dem Fork `grantnegri/ffmpeg-python`, die der Visionär zur Übernahme ausgewählt hat |
