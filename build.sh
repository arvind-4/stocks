#!/bin/bash

echo "Installing packages..."
uv sync --locked

echo "Collecting static files..."
uv run python manage.py collectstatic  --noinput --clear
