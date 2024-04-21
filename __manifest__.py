{
    'name': 'Projecta_Ttima',
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
        'security/ir.rule.xml',
        'views/persones_views.xml',
        'views/reserves_views.xml',
        'views/rutes_views.xml',
        'views/intermediaris_views.xml',
        'views/grups_views.xml',
        'views/cases_views.xml',
        'views/habitacions_views.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
