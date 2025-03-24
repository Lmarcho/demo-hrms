# -*- coding: utf-8 -*-
{
    'name': 'Remove Odoo Branding',
    'version': '1.0',
    'summary': 'Hide Odoo branding from the admin interface',
    'description': """
        This module removes Odoo branding elements from the admin interface:
        - Removes Odoo logo from login page
        - Hides Odoo from the title
        - Removes references in the footer
        - Customizes the favicon
    """,
    'category': 'Tools',
    'author': 'Lakshitha',
    'website': 'https://lmarcho.com',
    'depends': ['web', 'mail'],
    'assets': {
        'web.assets_backend': [
            'remove_odoo_branding/static/src/css/remove_branding.css',
            'remove_odoo_branding/static/src/js/window_title.js',
        ],
        'web.assets_frontend': [
            'remove_odoo_branding/static/src/css/remove_branding.css',
        ],
    },
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}