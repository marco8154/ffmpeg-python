# Credits
ffmpeg-python-ng is the continuation of ffmpeg-python (<https://github.com/kkroening/ffmpeg-python>).

## Original author and maintainer
Karl Kroening

## Contributors to the original project
The names below are as they appear in the Git history of the original project up to commit `df129c7`.

- 372046933
- Andrey Kolpakov
- Arne de Laat
- Christian Clauss
- Christophe Mehay
- Davide Depau
- Dim
- Harshna Patel
- Iulian Onofrei
- Jacotsu
- Jim DeLaHunt
- Karthikeyan Singaravelan
- Kyle McDonald
- Michal Trybus
- Nitay Megides
- Noah Stier
- Raul
- Stephen Chen
- Tercio Gaudencio Filho
- apatsekin
- laurentalacoque
- lcjh
- magnusvmt
- raulpy271

## Carried-over patches
Patches carried over from the original keep their author.

| Patch | Author | Source | Released in |
| --- | --- | --- | --- |
| `view()` uses `tempfile.mkstemp` instead of `mktemp` | Sarthak Munshi | grantnegri/ffmpeg-python commit `c1ef452` | 0.3.0 |
| Stream selector with index 0 | Artem Eltyshev | kkroening/ffmpeg-python#490 (`7da1f6a`) | 0.3.1 |
| `explicit_maps` for `get_args()` and `compile()` | Artem Eltyshev | kkroening/ffmpeg-python#403 (`8e9fc34`) | 0.3.1 |
| `popen_args` for `run_async()` | Michael Litvin | kkroening/ffmpeg-python#675 (`81ffd22`) | 0.3.1 |
| Pipe input for `probe()` | Rocky Cai | kkroening/ffmpeg-python#588 (`463aa0a`) | 0.3.1 |
| `capture_stderr` for `probe()` | Ezequiel Ramos | kkroening/ffmpeg-python#609 (`6916ab2`) | 0.3.1 |
| Path-like objects as filenames | Brian Hou | kkroening/ffmpeg-python#700 (`59c504c`, `51e4d22`) | 0.3.1 |
| `get_hash` on FIPS systems | Zachary Berry | kkroening/ffmpeg-python#766 (`f693ea6`) | 0.3.1 |
| Relative import in `_view.py` | Shimpei Yamaguchi | kkroening/ffmpeg-python#772 (`5007aa5`) | 0.3.1 |
| `atrim` filter | Jason Cordial | kkroening/ffmpeg-python#449 (`84da93f`) | 0.3.1 |

## Continuation
The continuation is coordinated on swarvex.ai and contributions are listed in the changelog.
