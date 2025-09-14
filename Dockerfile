# Multi-stage build for production
FROM node:18-alpine AS frontend-build

WORKDIR /app/frontend
COPY frontend/package*.json ./
RUN npm ci --only=production
COPY frontend/ ./
RUN npm run build

# Python base image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
        gcc \
        python3-dev \
        musl-dev \
        nodejs \
        npm \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Copy built frontend
COPY --from=frontend-build /app/frontend/build ./static/

# Install Node.js dependencies for services
WORKDIR /app/express-server
COPY express-server/package*.json ./
RUN npm ci --only=production

WORKDIR /app/sentiment-analyzer
COPY sentiment-analyzer/package*.json ./
RUN npm ci --only=production

WORKDIR /app

# Collect static files
RUN python manage.py collectstatic --noinput

# Create non-root user
RUN adduser --disabled-password --gecos '' appuser
RUN chown -R appuser:appuser /app
USER appuser

# Expose ports
EXPOSE 8000 3030 5000

# Start script
COPY start.sh .
RUN chmod +x start.sh

CMD ["./start.sh"]