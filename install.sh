#!/bin/bash
python -m venv venv && source venv/bin/activate
[ -f requirements.txt ] && pip install -r requirements.txt