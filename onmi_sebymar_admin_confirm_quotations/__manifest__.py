{
    'name': 'SEBYMAR Admin confirm quotations',
    'version': '15.0.0.1',
    'summary': 'Only Admin can confirm sale & purchase quotations.',
    'description': 'Only Admin can confirm sale & purchase quotations.',
    'category':  'ONMI developments',
    'author': 'ONMI Engineering',
    'license': 'LGPL-3',
    'depends': ['sale', 'purchase'],
    'data': [
        'views/sale_order_views.xml',
        'views/purchase_order_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
