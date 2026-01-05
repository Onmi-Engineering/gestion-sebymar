from odoo import fields, models, api


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    pricelist_id = fields.Many2one(
        'product.pricelist.purchase', string='Pricelist', check_company=True,  # Unrequired company
        readonly=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]", tracking=1,
        help="If you change the pricelist, all the line discounts could be affected.", )

    def update_discount_from_pricelist(self):
        for rec in self:
            lines = rec.order_line
            if not rec.pricelist_id:
                for line in lines:
                    line.write({'discount': 0.0})
            pricelist = rec.pricelist_id
            for item in pricelist.item_ids:
                if item.applied_on == '3_global':
                    for line in lines:
                        if line.discount != item.discount:
                            line.write({'discount': item.discount})

                if item.applied_on == '2_product_category':# Revisar los productos asociados que aparecen y buscar por ahí.
                    all_categ = item.categ_id.search([('id', 'child_of', item.categ_id.ids)])
                    for line in lines:
                        if line.product_id.categ_id.id in all_categ.ids:
                            if line.discount != item.discount:
                                line.write({'discount': item.discount})
                        else:
                            line.write({'discount': 0.0})
