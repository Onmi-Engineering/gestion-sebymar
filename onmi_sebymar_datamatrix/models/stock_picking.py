from odoo import fields, models, api
import html2text


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    datamatrix_line_ids = fields.One2many('datamatrix', 'picking_id', string='Datamatrix',
                                          domain="[('picking_id', '=', id]", default=False)

    def generate_datamatrix_lines(self):
        for rec in self:
            rec.datamatrix_line_ids.unlink()
            for move in rec.move_ids_without_package.filtered(lambda mv: mv.product_id.categ_id.datamatrix == True):
                for i in range(int(move.product_uom_qty)):
                    rec.datamatrix_line_ids.create({
                        'product_id': move.product_id.id,
                        'picking_id': rec.id,
                        'move_id': move.id,
                        'qr_code': '',
                    })

    def update_old_datamatrix(self):
        for rec in self:
            rec.datamatrix_line_ids.unlink()
            note_not_html = html2text.html2text(rec.note)
            data_list = note_not_html.split('\n\n')
            new_list = []
            for a in data_list:
                if a.isspace():
                    continue
                if a == '':
                    continue
                new_list.append(a)

            if not rec.datamatrix_line_ids:
                rec.generate_datamatrix_lines()
                j = 0
                for data in rec.datamatrix_line_ids:
                    if len(new_list) >= j + 1:
                        data.qr_code = new_list[j]
                    j += 1
