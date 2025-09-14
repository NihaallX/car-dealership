#!/usr/bin/env bash
# Build script for Render deployment

set -o errexit  # exit on error

pip install --upgrade pip
pip install -r requirements.txt

# Run Django setup
python manage.py collectstatic --no-input
python manage.py migrate