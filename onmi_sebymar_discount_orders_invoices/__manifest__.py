{
    'name': 'SEBYMAR discounts on orders and sales',
    'version': '18.0.0.1',
    'summary': 'Discounts on orders and sales',
    'description': 'Discounts on orders and sales',
    'category':  'ONMI developments',
    'author': 'ONMI Engineering',
    'license': 'LGPL-3',
    'depends': ['base', 'stock', 'sale'],
    'data': [
        'views/sale_order_views.xml',
        'report/sale_order_report_template.xml',
        'views/account_move_view.xml'
        ],
    'installable': True,
    'application': True,
    'auto_install': False
}
