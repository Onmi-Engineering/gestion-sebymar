{
    'name': 'SEBYMAR Pricelist Purchase',
    'version': '18.0.0.1',
    'summary': 'Pricelist Purchase',
    'description': 'Pricelist Purchase',
    'category': 'ONMI developments',
    'author': 'ONMI Engineering',
    'license': 'LGPL-3',
    'depends': [
        'purchase',
    ],
    'data': [
        'security/product_pricelist_purchase_access.xml',
        'views/product_pricelist_purchase_views.xml',
        'views/purchase_order_views.xml',
        # 'views/res_partner_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
