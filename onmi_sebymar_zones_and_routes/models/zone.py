from odoo import fields, models, api


class Zone(models.Model):
    _name = 'zone'
    _description = 'Zones'

    name = fields.Char('Name')
    partner_ids = fields.One2many('res.partner', 'zone_id')
    route_id = fields.Many2one('route')
