from odoo import fields, models, api


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    total_prices_without_taxes = fields.Float('Total without taxes', compute="_compute_total_prices")
    total_prices_with_taxes = fields.Float('Total with taxes', compute="_compute_total_prices")
    total_prices_with_taxes_final = fields.Float('Total with taxes', compute="_compute_total_prices_with_taxes")
    total_prices_with_taxes_final_backorders = fields.Float('Total with taxes', compute="_compute_total_prices_with_taxes_backorders")
    total_taxes = fields.Float('Total taxes', compute="_compute_total_prices_taxes")
    total_prices_taxes = fields.Float('Total taxes', compute="_compute_total_prices")
    total_prices_taxes_backorders = fields.Float('Total taxes backorders', compute="_compute_total_prices_backorders")
    total_prices_without_taxes_backorders = fields.Float('Total without taxes backorders', compute="_compute_total_prices_backorders")
    total_prices_with_taxes_backorders = fields.Float('Total with taxes backorders', compute="_compute_total_prices_backorders")
    total_taxes_backorders = fields.Float('Total taxes', compute="_compute_total_prices_taxes_backorders")
    total_discount = fields.Float('Total discount', compute="_compute_total_discount")
    total_discount_taxes = fields.Float('Total discount backorders', compute="_compute_total_discount_taxes")

    def _compute_total_prices_with_taxes(self):
        for rec in self:
            rec.total_prices_with_taxes_final = 0
            rec.total_prices_with_taxes_final = rec.total_prices_without_taxes + rec.total_taxes

    def _compute_total_prices_with_taxes_backorders(self):
        for rec in self:
            rec.total_prices_with_taxes_final_backorders = 0
            rec.total_prices_with_taxes_final_backorders = rec.total_prices_without_taxes_backorders + rec.total_taxes_backorders

    def _compute_total_prices_taxes(self):

        for rec in self:
            rec.total_taxes = rec.total_prices_without_taxes * 0.21

    def _compute_total_prices_taxes_backorders(self):

        for rec in self:
            rec.total_taxes_backorders = rec.total_prices_without_taxes_backorders * 0.21

    def _compute_total_discount(self):
        for rec in self:
            rec.total_discount = 0.0
            for line in rec.move_ids_without_package:
                rec.total_discount += line.discount_dif
    def _compute_total_discount_taxes(self):
        for rec in self:
            rec.total_discount_taxes = 0.0
            for line in rec.backorder_ids.move_ids_without_package:
                rec.total_discount_taxes += line.discount_dif

    def _compute_total_prices(self):
        for rec in self:
            rec.total_prices_without_taxes = 0.0
            rec.total_prices_with_taxes = 0.0
            rec.total_prices_taxes = 0.0
            for line in rec.move_ids_without_package:
                discount = line.discount or 0.0
                discounted_subtotal = line.price_subtotal - (line.price_subtotal * (discount / 100))
                rec.total_prices_without_taxes += discounted_subtotal
                rec.total_prices_taxes += line.price_subtotal_with_taxes
            rec.total_prices_with_taxes = rec.total_prices_without_taxes + rec.total_prices_taxes

    def _compute_total_prices_backorders(self):
        for rec in self:
            rec.total_prices_without_taxes_backorders = 0.0
            rec.total_prices_with_taxes_backorders = 0.0
            rec.total_prices_taxes_backorders = 0.0
            for line in rec.backorder_ids.move_ids_without_package:
                discount = line.discount or 0.0
                discounted_subtotal = line.price_subtotal - (line.price_subtotal * (discount / 100))
                rec.total_prices_without_taxes_backorders += discounted_subtotal
                rec.total_prices_taxes_backorders += line.price_subtotal_with_taxes
            rec.total_prices_with_taxes_backorders = rec.total_prices_without_taxes_backorders + rec.total_prices_taxes_backorders
