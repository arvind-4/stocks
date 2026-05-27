#!/bin/bash

echo "Installing packages..."
uv sync --locked --no-dev

echo "Collecting static files..."
uv run python manage.py collectstatic  --noinput --clear
