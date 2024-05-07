# -*- coding: utf-8 -*-
{
    'name': "infomusicplus",
    'summary': """
        infomusic plus""",
    'description': """
        este modulo extiende el modulo infomusic
    """,
    'author': "JS",
    'website': "http://www.modulsDAM1.edu",
    'category': 'Songs',
    'version': '0.1',
    'application': True,
    'depends': ['base', 'infomusic'],
    'data': [
        'security/ir.model.access.csv',
        'views/disk.xml',
        'views/singer.xml',
        'views/tour.xml',
        'views/tour_city.xml',
        'views/new_menu.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
