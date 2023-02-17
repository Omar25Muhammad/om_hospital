# -*- coding: utf-8 -*-
{
    'name': 'Hospital Management',
    'version': '1.03',
    'author': 'Eng.Omar M Shehada',
    'summary': 'Hospital Managament App',
    'sequence': 1,
    'description': """An app for managing hosptial services""",
    'category': 'Services',
    'website': 'https:/www.c8ke.com/omar_awards',
    'images': [],
    'depends': [
        'mail'
    ],
    'data':
        [
            'security/ir.model.access.csv',
            'data/data.xml',
            'views/view_patient.xml',
            'views/view_kids.xml',
            'views/view_gender.xml',
        ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': True,
    'license': 'LGPL-3',
}
