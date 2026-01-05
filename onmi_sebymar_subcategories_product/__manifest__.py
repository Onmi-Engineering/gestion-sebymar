{
    'name': 'SEBYMAR Subcategories product',
    'version': '15.0.0.1',
    'summary': 'Create new subcategories',
    'description': 'Create new subcategories',
    'category':  'ONMI developments',
    'author': 'ONMI Engineering',
    'license': 'LGPL-3',
    'depends': [
        'product',
        'stock',
    ],
    'data': [
        'security/collection_model_access.xml',
        'security/product_template_type_model_access.xml',
        'views/product_template_views.xml',
        'views/collection_views.xml',
        'views/product_template_type_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
