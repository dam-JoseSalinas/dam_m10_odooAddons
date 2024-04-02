# -*- coding: utf-8 -*-
{
    'name': "library",
    'summary': """
        Books, ISBN, Author, Library.""",

    'description': """
        Aplicació per emmagatzemar llibres""",
    'author': "Jose Daniel Salinas",
    'website': "http://www.modulsDAM1.edu",
    'category': 'Books',
    'applicaction': True,

    'version': '0.1',
    'depends': ['base'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
