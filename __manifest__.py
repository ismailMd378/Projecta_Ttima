# -*- coding: utf-8 -*-
{
    'name': 'Rutas de Bicicleta',
    'version': '1.0',
    'category': 'Uncategorized',
    'summary': 'Administra rutas de bicicleta',
    'author': 'Ismail & Hicham',
    'license': 'AGPL-3',
    'website': 'https://www.ejemplo.com',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.cvs',
        'views/reserves.xml',
        'views/grups.xml',
        'views/persones.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
