FROM python:3.12-slim

WORKDIR /app

# Installation des dépendances système nécessaires
# - build-essential pour compiler certaines dépendances Python 
# - wget pour télécharger Chrome
# - gnupg pour vérifier les signatures
# - Dépendances pour Chrome
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    wget \
    gnupg \
    ca-certificates \
    fonts-liberation \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libatspi2.0-0 \
    libcups2 \
    libdbus-1-3 \
    libdrm2 \
    libgbm1 \
    libgtk-3-0 \
    libnspr4 \
    libnss3 \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    libxkbcommon0 \
    libxrandr2 \
    xdg-utils \
    && rm -rf /var/lib/apt/lists/*

# Installation de Chrome (nécessaire pour selenium)
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

# Définir la variable d'environnement pour signaler qu'on est dans Docker
ENV DOCKER_CONTAINER=true

# Création du répertoire pour les sorties
RUN mkdir -p /app/output

# Copie des fichiers du projet
COPY . /app/

# Installation des dépendances Python
RUN pip install --no-cache-dir polars 'great-tables[extra]' selenium pillow

# Commande par défaut
CMD ["python", "lyon-metro.py"]