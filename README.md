# software-version-drift-reporter

Compare installed software versions against a baseline and list every host that has drifted, with the version it has and the version it should have.

## How to run

```sh
python3 main.py installed.csv baseline.csv
```

## Example output

```
DRIFT PC-04 EditorPro: 3.1 (baseline 3.4)
1 drifted install(s).
```

Standard library only. Run the tests with `python3 -m unittest discover`.
