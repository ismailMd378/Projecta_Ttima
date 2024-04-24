{
    'name': 'projecta_ttima',
    'version': '1.0',
    'category': 'Uncategorized',
    'summary': 'Breve descripción del módulo',
    'description': """
        Descripción detallada del módulo.
    """,
    'author': 'Autor del Módulo',
    'website': 'URL del Sitio Web',
    'depends': ['base'],
    'data': [
        # Lista de archivos de datos
        'security/ir.model.access.csv',
        'views/persones.xml',
        'views/reserves.xml',
        'views/rutes.xml',
        'views/intermediaris.xml',
        'views/grups.xml',
        'views/cases.xml',
        'views/habitacions.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': True,
    'application': True,
}
