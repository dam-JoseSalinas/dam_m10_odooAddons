# -*- coding: utf-8 -*-
{
    'name': "infomusic",
    'summary': """
        addon de musica""",
    'description': """
        addon que permet guardar discs de cantants i relacionar la seva informació
    """,
    'author': "JS",
    'website': "http://www.modulsDAM1.edu",
    'category': 'Songs',
    'version': '0.1',
    'application': True,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/disk.xml',
        'views/song.xml',
        'views/singer.xml',
        'views/menu.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
