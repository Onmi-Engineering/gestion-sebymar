from odoo import fields, models, api


class ResUsers(models.Model):
    _inherit = 'res.users'

    onmi_login_date = fields.Datetime('Last Authentication', default=lambda u: u.login_date)
