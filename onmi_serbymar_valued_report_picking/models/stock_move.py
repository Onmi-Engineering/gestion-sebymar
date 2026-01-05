from odoo import fields, models, api, _


class StockMove(models.Model):
    _inherit = 'stock.move'

    currency_id = fields.Many2one("res.currency", string="Currency")
    price_unit = fields.Float('Unit Price', default=0.0, compute="_compute_valued_prices")
    taxes_id = fields.Many2many('account.tax', help="Default taxes used when selling/purchasing the product.",
                                string='Taxes', compute="_compute_valued_prices")
    price_subtotal = fields.Monetary('Price Subtotal', digits='Product Price', related='sale_line_id.price_subtotal', readonly=True)
    price_subtotal_with_taxes = fields.Float('Price Taxes Subtotal', digits='Product Price', default=0.0,
                                             compute="_compute_valued_prices")
    price_subtotal_without_desc = fields.Monetary('Price Subtotal', digits='Product Price', related='sale_line_id.price_subtotal', readonly=True)
    discount = fields.Float(
        related='sale_line_id.discount',
        string='Desc.%',
        readonly=True
    )

    discount_dif = fields.Float(
        string='Total discount', compute="_compute_total_discount",
        digits='Product Price', readonly=True)

    discounted_subtotal = fields.Float('Total discount', compute="_compute_total_discount2")

    bo_total_discounted = fields.Float('Backorders Total discount', compute="_compute_bo_total_discounted")

    def _compute_total_discount2(self):
        for line in self:
            line.discounted_subtotal = line.price_subtotal - (line.price_subtotal * (line.discount / 100))

    def _compute_bo_total_discounted(self):
        # bo_discounted = 0
        # TODO: Esto huele. Se están actualizando registros que no están en self.
        for bo_line in self.picking_id.backorder_ids.move_ids.filtered(lambda x: x.product_uom_qty):
            bo_line.bo_total_discounted = bo_line.price_subtotal - (bo_line.price_subtotal * (bo_line.discount / 100))

    def _compute_total_discount(self):
        for rec in self:
            # rec.discount_dif = 0
            rec.discount_dif = (rec.product_uom_qty * rec.price_unit) - rec.discounted_subtotal

    def compute_subtotal(self):
        for rec in self:
            # rec.price_subtotal = 0
            rec.price_subtotal = rec.price_subtotal_without_desc - rec.discount_dif

    @api.depends('sale_line_id', 'purchase_line_id')
    def _compute_valued_prices(self):
        for rec in self:
            rec.price_unit = 0.0
            rec.taxes_id = False
            rec.price_subtotal = 0.0
            rec.price_subtotal_with_taxes = 0.0
            if rec.sale_line_id:
                rec.price_unit = rec.sale_line_id.price_unit
                rec.taxes_id = rec.sale_line_id.tax_id
                rec.price_subtotal = rec.price_unit * rec.product_uom_qty
                amount_percentaje = 1
                if rec.taxes_id:
                    for tax in rec.taxes_id:
                        amount_percentaje = amount_percentaje * (tax.amount / 100)
                    rec.price_subtotal_with_taxes = amount_percentaje * rec.price_subtotal
            if rec.purchase_line_id:
                rec.price_unit = rec.purchase_line_id.price_unit
                rec.taxes_id = rec.purchase_line_id.taxes_id
                rec.price_subtotal = rec.price_unit * rec.product_uom_qty
                amount_percentaje = 1
                if rec.taxes_id:
                    for tax in rec.taxes_id:
                        amount_percentaje = amount_percentaje * (tax.amount / 100)
                    rec.price_subtotal_with_taxes = amount_percentaje * rec.price_subtotal


class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    def _get_aggregated_product_quantities(self, **kwargs):
        """
        Inherit _get_aggregated_product_quantities in order to include values from stock picking report valued
        """
        aggregated_move_lines = super()._get_aggregated_product_quantities(**kwargs)
        for aggregated_move_line in aggregated_move_lines:
            move_line = self.env['stock.move.line'].search([
                ('product_id', '=', aggregated_move_lines[aggregated_move_line]['product'].id),
                ('picking_id', '=', self.picking_id.id),
            ], limit=1)
            if move_line:
                price_unit = move_line.move_id.price_unit
                taxes = ', '.join(f"{amount}%" for amount in move_line.move_id.taxes_id.mapped('amount'))

                discount_dif = move_line.move_id.discount_dif
                price_subtotal = move_line.move_id.price_subtotal
                aggregated_move_lines[aggregated_move_line]['price_unit'] = price_unit
                aggregated_move_lines[aggregated_move_line]['taxes'] = str(taxes) + ' %'
                aggregated_move_lines[aggregated_move_line]['discount_dif'] = discount_dif
                aggregated_move_lines[aggregated_move_line]['price_subtotal'] = price_subtotal
        return aggregated_move_lines
