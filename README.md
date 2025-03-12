# Demo Great Tables - Métro de Lyon
Ce projet démontre l'utilisation de la librairie Great Tables pour créer des tableaux élégants en Python, en utilisant comme exemple les données du métro de Lyon.

## 🚇 À propos du projet
Ce projet illustre comment créer des tableaux professionnels avec Python en utilisant :
- La librairie Great Tables pour la mise en forme
- Polars pour la manipulation des données
- Les données du réseau de métro TCL de Lyon
- Exportation au format PDF (dans l'environnement Docker)

## 🛠️ Installation

### Méthode 1 : Installation classique
1. Cloner le repository :
```bash
git clone https://github.com/votre-username/demo_great_tables_metro_Lyon.git
cd demo_great_tables_metro_Lyon
```
2. Créer un environnement virtuel avec UV :
```bash
uv venv
```
3. Activer l'environnement virtuel :
```bash
# Windows
.venv/Scripts/activate
# Unix/MacOS
source .venv/bin/activate
```
4. Installer les dépendances :
```bash
uv pip install .
```

### Méthode 2 : Utilisation avec Docker 🐳
Prérequis : [Docker](https://docs.docker.com/get-docker/) et [Docker Compose](https://docs.docker.com/compose/install/)

1. Cloner le repository :
```bash
git clone https://github.com/votre-username/demo_great_tables_metro_Lyon.git
cd demo_great_tables_metro_Lyon
```

2. Lancer l'application avec Docker Compose :
```bash
docker-compose up --build
```

3. Les résultats seront générés dans le dossier `output/` à la racine du projet :
   - Un fichier PDF avec le tableau formaté (primary)
   - Un fichier HTML en solution de repli si la génération du PDF échoue

## 📊 Utilisation

### Sans Docker
Pour générer le tableau :
```bash
python lyon-metro.py
```

### Avec Docker
```bash
docker-compose up --build
```

Le script va :
1. Charger les données du métro de Lyon
2. Créer un tableau formaté avec Great Tables
3. En mode classique : ouvrir la visualisation dans votre navigateur par défaut
4. En mode Docker : générer un fichier PDF et/ou HTML dans le dossier `output/`

Le rendu est le suivant :
![](img/snapshot.png)

## 🔧 Structure du projet
```
demo_great_tables_metro_Lyon/
├── .venv/                   # Environnement virtuel
├── img/                     # Capture PNG du tableau généré
├── lyon-metro.py            # Script principal
├── pyproject.toml           # Configuration du projet
├── docker-compose.yml       # Configuration Docker Compose
├── Dockerfile               # Instructions pour construire l'image Docker
├── .dockerignore            # Fichiers à ignorer dans l'image Docker
├── output/                  # Dossier contenant les sorties générées (PDF, HTML)
└── README.md                # Documentation
```

## 📚 Dépendances principales
- Python 3.12
- great-tables[extra] (avec Selenium et Pillow pour l'export PDF)
- polars
- Chrome (installé automatiquement dans le conteneur Docker)

## 🐳 Avantages de l'utilisation avec Docker
- Environnement isolé et reproductible
- Installation automatique de toutes les dépendances (y compris Chrome)
- Pas besoin d'installer Python ou des dépendances sur votre machine
- Fonctionne de manière identique sur Windows, macOS et Linux
- Génération de PDF sans navigateur installé localement
- Installation en une seule commande pour les utilisateurs

## 🤝 Contribution
Les contributions sont les bienvenues ! N'hésitez pas à :
1. Fork le projet
2. Créer une branche pour votre fonctionnalité
3. Commiter vos changements
4. Pousser vers la branche
5. Ouvrir une Pull Request

## ✍️ Auteur
[Gael Penessot](https://www.linkedin.com/in/gael-penessot/)