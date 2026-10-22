# Project provenance and scope

Source: the user-supplied SmartFactoryProject_Final archive containing Python code, a Multisim circuit and an industrial software report.

The original application generated random readings, applied threshold rules and saved them in SQLite. Repository cleanup separates the monitoring rules from the GUI, adds a guarded entry point, closes the database when the application exits, anchors the database path to the application folder and adds automated tests. The original formula is retained within its simulated input range.

The supplied report discusses predictive maintenance and hardware/software integration as motivation. The delivered implementation is a rule-based simulator and a separate circuit. It does not implement predictive maintenance, real sensors or a connection between Multisim and Python.

The user's existing runtime database, bytecode caches and unrelated documents are intentionally excluded. No sample machine history is presented as a measured experimental dataset.
