from random import randint
from odoo import fields, models, api

class CompanyContactTag(models.Model):
    _name = 'company.contact.tag'
    _description = 'Company Contact Tags'

    @api.model
    def _get_default_color(self):
        return randint(1, 11)

    name = fields.Char(string='Name', required=True)
    color = fields.Integer(string='Color Index')

class ResPartner(models.Model):
    _inherit = 'res.partner'

    route_id = fields.Many2one('route')
    zone_id = fields.Many2one('zone')
    company_contact_tag_ids = fields.Many2many(
        'company.contact.tag',
        string='Company Contact Tags'
    )

    @api.onchange('route_id')
    def clean_zone_id(self):
        for rec in self:
            rec.zone_id = False