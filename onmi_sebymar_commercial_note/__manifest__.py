{
    'name': 'SEBYMAR Commercial note',
    'version': '18.0.0.1',
    'summary': 'Create commercial note from SO to SP.',
    'description': 'Create commercial note from SO to SP.',
    'category':  'ONMI developments',
    'author': 'ONMI Engineering',
    'license': 'LGPL-3',
    'depends': [
        'sale_stock',
        'purchase_stock',
        'onmi_sebymar_subcategories_product',
    ],
    'data': [
        'views/sale_order_views.xml',
        'views/stock_picking_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
