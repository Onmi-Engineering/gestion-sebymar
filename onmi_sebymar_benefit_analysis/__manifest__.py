{
    'name': 'SEBYMAR Benefits analysis',
    'version': '15.0.0.1',
    'summary': 'Benefits analysis',
    'description': 'Benefits analysis',
    'category': 'ONMI developments',
    'author': 'ONMI Engineering',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'account',
        'stock',
        'onmi_sebymar_subcategories_product',
    ],
    'data': [
        'views/account_move_line_view.xml',
        'views/account_move_view.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
