{
    'name': 'SEBYMAR Datamatrix',
    'version': '15.0.0.1',
    'summary': 'Create datamatrix registers',
    'description': 'Create datamatrix registers',
    'category':  'ONMI developments',
    'author': 'ONMI Engineering',
    'license': 'LGPL-3',
    'depends': [
        'stock',
        'sale',
    ],
    'data': [
        'security/datamatrix_model_access.xml',
        'views/stock_picking_views.xml',
        'views/product_category_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
