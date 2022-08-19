from odoo import api, models, fields, _
from odoo.exceptions import UserError

class PosComboProduct(models.Model):
    _name = "pos_combo_product.pos_combo_product"

    product_template_id = fields.Many2one('product.template', 'Combo Product', required=True)
    product_quantity = fields.Float('Quantity', default='1', required=True)
    product_id = fields.Many2one('product.product', 'Product', required=True)
    uom_id = fields.Many2one('uom.uom', related='product_id.uom_id')
    require = fields.Boolean('Require', default=True)

    @api.onchange('product_template_id', 'product_id')
    def change(self):
        if self.product_id.name == self.product_template_id.name:
            raise UserError(_('Not Allow to Same Product'))

    def combo_data(self,id):
        res = self.env['pos_combo_product.pos_combo_product'].search([('product_template_id', '=', id[0])])
        data = []
        for val in res:
            value = {
                'name': val.product_id.name,
                'quantity': val.product_quantity
            }
            data.append(value)
        return data
    def combo_id(self,ids):
        data = []
        if ids:
            res = self.env['pos_combo_product.pos_combo_product'].search([('id', '=', ids)])
            for val in res:
                value = val.product_id.id
                data.append(value)
        return data


class ComboProductTemplate(models.Model):

    _inherit = 'product.template'

    combo_product_id = fields.One2many('pos_combo_product.pos_combo_product', 'product_template_id', 'Combo')
    is_combo = fields.Boolean('Combo Product', default=False)
    combo_price = fields.Float('Combo Price', required=True)
    combo_product = fields.Boolean(default=False)

class PosOrderLine(models.Model):
    _inherit = 'pos.order.line'
    is_combo = fields.Boolean(default=False)
    combo_product =fields.Boolean(default=False)


