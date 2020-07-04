#!/bin/bash
python3 -m venv env
source env/bin/activate
PYTHONUNBUFFERED=1 python zombie_runner.py -f boo.json
