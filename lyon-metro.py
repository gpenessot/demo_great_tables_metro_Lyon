import polars as pl
import os
import tempfile
from great_tables import GT, md, html, loc, style
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# Création du dossier output s'il n'existe pas
os.makedirs('output', exist_ok=True)

# Création du DataFrame avec les données du métro de Lyon
data = {
    'Line': ['A', 'B', 'C', 'D'],
    'Opening_date': ['1978', '1978', '1974', '1991'],
    'Length_km': [9.2, 10.1, 2.5, 12.6],
    'Stations': [14, 12, 5, 15],
    'Termini': [
        'Perrache - Vaulx-en-Velin–La Soie',
        'Charpennes–Charles Hernu - Saint-Genis-Laval',
        'Hôtel de Ville–Louis Pradel - Cuire',
        'Gare de Vaise - Gare de Vénissieux'
    ],
    'Rolling_stock': ['MPL 75', 'MPL 16', 'MCL 80', 'MPL 85'],
    'icon': [
        '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Lyon_tcl_metro-a.svg/20px-Lyon_tcl_metro-a.svg.png">',
        '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Lyon_tcl_metro-b.svg/20px-Lyon_tcl_metro-b.svg.png">',
        '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/Lyon_tcl_metro-c.svg/20px-Lyon_tcl_metro-c.svg.png">',
        '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Lyon_tcl_metro-d.svg/20px-Lyon_tcl_metro-d.svg.png">'
    ]
}
df = pl.DataFrame(data)

# Création du tableau avec great-tables
lyon_metro = (
    GT(df)
    .tab_header(
        title=md("### Lignes du Métro de Lyon"),
        subtitle=html('''<h4 align="left">
        Le métro de Lyon, géré par TCL, comprend 4 lignes desservant 
        46 stations sur un réseau de 34.4 km.</h4>''')
    )
    .cols_align(align='center', columns=['icon', 'Opening_date', 'Stations', 'Length_km'])
    .cols_label(
        icon="Ligne",
        Line="Numéro",
        Opening_date="Ouverture",
        Length_km="Longueur (km)",
        Stations="Stations",
        Termini="Terminus",
        Rolling_stock="Matériel Roulant"
    )
    .fmt_number(
        columns=['Length_km'],
        decimals=1
    )
    .tab_source_note(
        source_note=md('''**Source:** TCL (Transports en Commun Lyonnais)<br>
        Données mises à jour en 2024''')
    )
    .tab_options(
        table_width="600px",
        container_width="100%",
        container_overflow_x="auto",
        container_overflow_y="auto"
    )
)

# Utiliser save() pour exporter en PDF
output_pdf_path = 'output/metro_lyon_table.pdf'
output_html_path = 'output/metro_lyon_table.html'

try:
    # Configurer Chrome pour qu'il fonctionne dans Docker
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    
    # Créer un répertoire temporaire unique pour les données utilisateur
    temp_dir = tempfile.mkdtemp()
    chrome_options.add_argument(f'--user-data-dir={temp_dir}')
    
    # Créer un driver Chrome configurer pour Docker
    driver = webdriver.Chrome(options=chrome_options)
    
    # Essayer d'utiliser la méthode save() avec notre driver personnalisé
    lyon_metro.save(
        file=output_pdf_path,
        scale=1.0,
        web_driver=driver
    )
    print(f"Le tableau a été généré et sauvegardé comme PDF dans {output_pdf_path}")
    
    # Fermer le driver
    driver.quit()
    
except Exception as e:
    print(f"Erreur lors de la génération du PDF: {str(e)}")
    
    # Fallback - exporter en HTML si le PDF échoue
    with open(output_html_path, 'w', encoding='utf-8') as f:
        f.write(lyon_metro._render_as_html())
    print(f"Solution de repli: le tableau a été sauvegardé comme HTML dans {output_html_path}")

# Afficher le tableau dans la console seulement si on n'est pas dans Docker
if os.environ.get('DOCKER_CONTAINER') != 'true':
    lyon_metro.show()