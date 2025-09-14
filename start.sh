#!/bin/bash

# Wait for database to be ready
echo "Waiting for database..."
while ! python manage.py migrate --check; do
  sleep 1
done

# Apply database migrations
echo "Applying database migrations..."
python manage.py makemigrations
python manage.py migrate

# Create superuser if it doesn't exist
echo "Creating superuser..."
python create_superuser.py

# Create sample data
echo "Creating sample data..."
python create_sample_data.py

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Start services in background
echo "Starting Express API..."
cd express-server && node server.js &

echo "Starting Sentiment Analyzer..."
cd ../sentiment-analyzer && node app.js &

# Start Django application
echo "Starting Django application..."
cd ..
exec python manage.py runserver 0.0.0.0:8000