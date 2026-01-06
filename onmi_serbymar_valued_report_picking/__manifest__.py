{
    'name': 'SEBYMAR Valued Report Picking',
    'version': '18.0.0.1',
    'summary': 'Valued Report Pickings.',
    'description': 'VAlued Report Pickings.',
    'category': 'Stock',
    'author': 'ONMI Engineering',
    'license': 'LGPL-3',
    'depends': [
        'sale_stock',
        'purchase_stock',
    ],
    'data': [
        'reports/stock_picking_report.xml',
        'views/stock_picking_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
