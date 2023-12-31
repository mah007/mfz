# -*- coding: utf-8 -*-
{
    'name': "School System",

    'summary': """
        School system to manage student Data""",

    'description': """
        School system to manage student Data
    """,

    'author': "Mahmoud",
    'website': "http://www.mah007.net",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'School',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail','website','web'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',

        'views/rejection.xml',
        'views/student.xml',
        'views/level.xml',
        'views/menus.xml',
        'reports/student_report.xml',
        'views/templates.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
