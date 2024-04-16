# -*- coding: utf-8 -*-
{
    'name': "library",

    'summary': """
        Books, ISBN, Author, Library.""",

    'description': """
        Aplicació per emmagatzemar llibres
    """,

    'author': "Jose Salinas",
    'website': "http://www.modulsDAM1.edu",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Books',
    'application': True,
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/member.xml',
        'views/loan.xml',
        'views/book.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
