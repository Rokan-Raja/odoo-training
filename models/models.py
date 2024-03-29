# -*- coding: utf-8 -*-
from odoo import models, fields, api

class MrpProduction(models.Model):
    
    _inherit = 'mrp.production'

    def button_mark_done(self):
        res = super(MrpProduction, self).button_mark_done()
        invoice_lines = []
        origin = self.origin
        print(origin)
        res2 = self.env['mrp.production'].search([('origin', '=', origin)])
        count2 = len(res2)
        count = 0
        for res1 in res2:
            if res1.state == 'done':
                count = count + 1
        print(count)
        if count == count2:
            invoice = self.env['account.move'].search([('invoice_origin', '=', origin)])
            if not invoice.invoice_origin:
                if origin:
                    data1 = self.env['sale.order'].search([('name', '=', origin)])
                    id = data1.id
                    data = self.env['sale.order.line'].search([('order_id', '=', id)])
                    for data2 in data:
                        vals = {
                            'name': origin,
                            'price_unit': data2.price_unit,
                            'quantity': data2.product_uom_qty,
                            'product_id': data2.product_id.id,
                            'product_uom_id': data2.product_uom.id,
                            'tax_ids': [(6, 0, data2.tax_id.ids)],
                            'sale_line_ids': [(6, 0, [data2.id])],
                        }
                        invoice_lines.append((0, 0, vals))
                    self.env['account.move'].create({
                        'ref': data1.client_order_ref,
                        'move_type': 'out_invoice',
                        'invoice_origin': origin,
                        'invoice_user_id': data1.user_id.id,
                        'partner_id': data1.partner_invoice_id.id,
                        'currency_id': data1.pricelist_id.currency_id.id,
                        'invoice_line_ids': invoice_lines
                    })
                    data1.write({'invoice_status' : 'invoiced'})
        return res





