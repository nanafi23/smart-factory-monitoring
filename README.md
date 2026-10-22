# Smart Factory Monitoring Simulator

A desktop coursework project by Omar Gouda demonstrating rule-based machine monitoring with **Python, Tkinter and SQLite**, accompanied by a separate **NI Multisim alarm circuit**.

## What it does

- Generates simulated temperature (50–110 °C) and vibration (10–100, arbitrary units) readings.
- Labels readings as normal, warning or critical using explicit thresholds.
- Computes a bounded heuristic health score and records each reading in SQLite.
- Displays historical readings in a desktop table.

## Quick start

Requires Python 3.10+ with Tkinter and a graphical desktop. The application uses only Python's standard library; no pip installation is needed. Some Linux distributions package Tkinter separately.

```bash
python main.py
```

Click **Generate Reading** to simulate a sample, then **View History** to inspect saved readings. A local `factory.db` is created beside the application; it is excluded from version control.

## Decision rules

| Condition, evaluated in order | Status |
|---|---|
| Temperature > 90 or vibration > 80 | CRITICAL |
| Temperature > 75 | WARNING |
| Otherwise | NORMAL |

The score is `100 - int(0.5 * temperature + 0.3 * vibration)`, clamped to 0–100. This is an illustrative coursework formula, not a calibrated failure probability or a machine-learning model.

## Structure

| Path | Purpose |
|---|---|
| `main.py` | Tkinter interface and simulated sampling |
| `monitoring.py` | Status and score logic, independently importable |
| `database.py` | Parameterized SQLite storage and connection management |
| `circuits/alarm.ms14` | Original Multisim circuit source |
| `docs/project-notes.md` | Scope, original work and cleanup notes |
| `tests/` | Boundary, score and persistence checks |

## Circuit

Open `circuits/alarm.ms14` in a compatible NI Multisim installation. The supplied report describes an LM358 comparator, adjustable reference, LED and buzzer alarm. The circuit file is included unchanged; Multisim simulation was not rerun during cleanup.

**The Python app and Multisim circuit are separate demonstrations.** There is no live sensor, serial, DAQ or circuit-to-Python connection in this repository.

## Verification

```bash
python -m unittest discover -s tests -v
python -m py_compile main.py database.py monitoring.py
```

Three tests passed during cleanup: threshold boundaries with vibration override, score bounds and direction, and SQLite persistence/history order. Python syntax checks passed. The GUI and Multisim require their respective desktop tools and were not interactively tested in the headless verification environment.

## Limitations and possible extensions

No real machine data, trained prediction model, production safety system or timing guarantees are provided. Future work could add timestamps, CSV export, real sensor acquisition and evaluation on labelled failure data.
