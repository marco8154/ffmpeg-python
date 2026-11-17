# Architektur

Stand: 17.11.2026, Commit `df129c7` des Originals. Die Architektur wird übernommen, nicht umgebaut.

## Was die Bibliothek tut

Der Nutzer baut mit Python-Aufrufen einen Graphen aus Eingaben, Filtern und Ausgaben. Die Bibliothek übersetzt ihn in eine Argumentliste für das Programm `ffmpeg` und startet es auf Wunsch. Sie verarbeitet selbst keine Medien.

```
ffmpeg.input(...)  ->  .filter(...) / .hflip() ...  ->  .output(...)  ->  .get_args() / .run()
     InputNode             FilterNode                    OutputNode        Argumentliste / Prozess
```

## Modulkarte

| Modul | Zeilen | Aufgabe | Öffentliche Namen |
|---|---|---|---|
| `ffmpeg/__init__.py` | 22 | sammelt die öffentliche API in `__all__` | – |
| `ffmpeg/dag.py` | 240 | allgemeiner gerichteter Graph: `DagNode`, `DagEdge`, `KwargReprNode`, Kanten und topologische Sortierung | intern |
| `ffmpeg/nodes.py` | 380 | Knoten und Datenströme: `Stream`, `InputNode`, `FilterNode`, `OutputNode`, `GlobalNode`, `MergeOutputsNode`; Dekoratoren `filter_operator`, `output_operator` | `Stream` |
| `ffmpeg/_ffmpeg.py` | 95 | Einstieg und Ausgang des Graphen | `input`, `output`, `merge_outputs`, `overwrite_output` |
| `ffmpeg/_filters.py` | 510 | je Filter eine Funktion, die einen `FilterNode` anlegt | `filter`, `filter_`, `filter_multi_output`, `concat`, `crop`, `drawbox`, `drawtext`, `hflip`, `hue`, `overlay`, `setpts`, `colorchannelmixer` und weitere, siehe `__all__` |
| `ffmpeg/_run.py` | 347 | Graph in Argumentliste übersetzen, Prozess starten | `get_args`, `compile`, `run`, `run_async`, `Error` |
| `ffmpeg/_probe.py` | 30 | `ffprobe` aufrufen, JSON zurückgeben | `probe` |
| `ffmpeg/_view.py` | 108 | Graph mit graphviz zeichnen (graphviz ist optional) | `view` |
| `ffmpeg/_utils.py` | 108 | Helfer: `basestring`, `escape_chars`, `convert_kwargs_to_cmd_line_args`, `get_hash` | intern |
| `ffmpeg/tests/test_ffmpeg.py` | 828 | die Tests des Originals | – |

Abhängigkeiten zwischen den Modulen: `dag` ← `nodes` ← `_ffmpeg`, `_filters`, `_run`, `_view`; `_run` benutzt zusätzlich `_ffmpeg`, `_view` benutzt `_run`. `_utils` wird von allen außer `_view` benutzt. `_probe` braucht nur `_run.Error` und `_utils`.

## Erweiterungspunkt: Filter

Ein neuer Filter ist eine Funktion in `ffmpeg/_filters.py` mit dem Dekorator `@filter_operator()`, die `FilterNode(stream, name, args=..., kwargs=...).stream()` zurückgibt, und ein Eintrag in `__all__`. Vorbild: `hflip` (ohne Parameter) und `crop` (mit Parametern). Der zugehörige Test prüft die Argumentliste, Vorbild: `test__get_args__simple` in `ffmpeg/tests/test_ffmpeg.py`.

Jeder Filter, den es nicht als eigene Funktion gibt, ist schon heute über `stream.filter('name', ...)` erreichbar.

## Verträge

- Die öffentliche API ist `ffmpeg.__all__`. Alles mit führendem Unterstrich und `dag.py` ist intern.
- Die Tests des Originals sind der Vertrag für das Verhalten. Ihre erwarteten Argumentlisten ändern sich nicht.
- `ffmpeg` und `ffprobe` werden über den Suchpfad gefunden (`cmd='ffmpeg'`), immer als Argumentliste ohne Shell.

## Umgebung und Testvertrag

- `.devcontainer/Dockerfile`: Python 3.13 (Debian 13), ffmpeg 7.1 aus Debian, pytest 9.2.0, pytest-mock 3.17.0, `future` 1.0.0 (bis die Abhängigkeit entfernt ist).
- `swarvex.yaml`: `python -m pytest -q`, ohne Netzwerk.
- `.github/workflows/ci.yml`: dieselben Tests auf Python 3.10 bis 3.15 unter Linux, dazu die jeweils neueste stabile Version (`3.x`) unter Linux, Windows und macOS und die nächste Version als Vorabversion (heute 3.16, Fehler blockieren nicht). Läuft bei jedem Push und wöchentlich.
