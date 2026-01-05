from odoo import fields, models, api


class Route(models.Model):
    _name = 'route'
    _description = 'Routes'

    name = fields.Char('Name')
    partner_ids = fields.One2many('res.partner', 'route_id')
    zone_ids = fields.One2many('zone', 'route_id')
