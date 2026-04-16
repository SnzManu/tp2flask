FROM python:3.9-slim

# On évite le cache pip pour réduire la taille et les risques
WORKDIR /app
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

# Utilisation de la notation JSON pour le CMD
CMD ["python", "app.py"]
