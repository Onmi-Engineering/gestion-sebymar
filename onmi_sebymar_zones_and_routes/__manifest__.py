{
    'name': 'SEBYMAR Zones & Routes',
    'version': '18.0.0.1',
    'summary': 'Allow Create zones and routes',
    'description': 'Allow Create zones and routes',
    'category':  'ONMI developments',
    'author': 'ONMI Engineering',
    'license': 'LGPL-3',
    'depends': ['contacts'],
    'data': [
        'security/ir_model_access.xml',
        'views/route_views.xml',
        'views/zone_views.xml',
        'views/res_partner_views.xml',

    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
