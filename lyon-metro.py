import polars as pl
from great_tables import GT, md, html, loc, style

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
        '<img src="//upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Lyon_tcl_metro-a.svg/20px-Lyon_tcl_metro-a.svg.png">',
        '<img src="//upload.wikimedia.org/wikipedia/commons/thumb/9/94/Lyon_tcl_metro-b.svg/20px-Lyon_tcl_metro-b.svg.png">',
        '<img src="//upload.wikimedia.org/wikipedia/commons/thumb/4/40/Lyon_tcl_metro-c.svg/20px-Lyon_tcl_metro-c.svg.png">',
        '<img src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Lyon_tcl_metro-d.svg/20px-Lyon_tcl_metro-d.svg.png">'
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

lyon_metro.show()