#!/bin/bash
# filepath: backend/startup.sh

echo "Starting application..."

# Warte auf die Datenbank (optional)
echo "Waiting for database..."
sleep 5

# Führe das Demo-Script aus
echo "Creating demo content..."
python -m src.content.create_content

# Starte die Anwendung
echo "Starting uvicorn server..."
exec uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload