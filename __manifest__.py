{
    'name': 'projecta_ttima',
    'version': '1.0',
    'category': 'Uncategorized',
    'summary': 'Breve descripción del módulo',
    'description': """
        Descripción detallada del módulo.
    """,
    'author': 'Ismail & Hicham',
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
        #'views/passa_per.xml',
        #'views/reserves_habitacions.xml',
        'views/factura_serveis.xml'
    ],
    'demo': [
        'demo/demo.xml'
        ],
    'installable': True,
    'auto_install': True,
    'application': True,
}
