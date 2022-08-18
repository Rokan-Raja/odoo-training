# -*- coding: utf-8 -*-
{
    'name': "pos_combo_product",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'point_of_sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/Pos_Assets.xml',
        'views/combo_product_view.xml',
    ],
    'qweb': [
        'static/src/xml/ComboDisplay.xml',
        'static/src/xml/ComboList.xml',
        'static/src/xml/ComboPopup.xml',
        'static/src/xml/ComboOrderLine.xml',
    ],
    # only loaded in demonstration mode

    'installable': True,
    'application': True,
    'auto-install': True
}
