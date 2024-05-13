# -*- coding: utf-8 -*-
{
    'name': "hotel_itic",
    'summary': """
        examen modul hotel_itic""",
    'description': """
        este modulo es un sistema de gestion de habitaciones de un hotel
    """,
    'author': "JS",
    'website': "http://www.modulsDAM1.edu",
    'category': 'Hotel',
    'version': '0.1',
    'application': True,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/room.xml',
        'views/menu.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
