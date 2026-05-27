#!/bin/bash

echo "Upgrade pip..."
python3.12 -m pip install --upgrade pip

echo "Installing dependencies..."
python3.12 -m pip install -r requirements.txt

echo "Collecting static files..."
python3.12 manage.py collectstatic  --noinput --clear