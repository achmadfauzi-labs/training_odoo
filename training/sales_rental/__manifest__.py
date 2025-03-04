# -*- coding: utf-8 -*-
{
    'name': "Sales Rental",

    'summary': "Sales Rental",

    'description': """
Sales Rental
    """,

    'author': "Bimo Satria",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/product_template_views.xml',
        # 'views/product_template_inherit_kanban_views.xml',
        'views/product_views.xml',
        'views/sale_order_views.xml',
        'views/rental_menu.xml',
        'views/sale_order_tree_views.xml',
        'views/sale_order_form_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True
}

