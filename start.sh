#!/bin/bash
set -e
pip install --upgrade pip
pip install -r requirements.txt
export PORT="${PORT:-3000}"
python -m uvicorn main:app --host 0.0.0.0 --port $PORT
