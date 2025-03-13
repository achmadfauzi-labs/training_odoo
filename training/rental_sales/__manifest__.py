# -*- coding: utf-8 -*-
{
    'name': "rental_sales",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",


    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base', 'product', 'sale_management'],

    # always loaded
    'data': [
        'security/res_group.xml',
        'security/ir.model.access.csv',
        'views/product_template_view_inherit.xml',
        'views/sale_order_view_inherit.xml',
        'views/rental_sales_menu.xml',
    ],

    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'assets': {
        'web.assets_backend': [
            'rental_sales/static/src/scss/custom_style.scss',
        ],
    },
}

