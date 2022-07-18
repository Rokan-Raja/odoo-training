# -*- coding: utf-8 -*-
from odoo import models, fields, api

class MrpProduction(models.Model):
    
    _inherit = 'mrp.production'

    def button_mark_done(self):
        res = super(MrpProduction, self).button_mark_done()
        invoice_lines = []
        query = self.env.cr.execute("UPDATE sale_order SET invoice_status='invoiced' WHERE name='"+str(self.origin)+"'")
        print(query)
        invoice = self.env['account.move'].search([('invoice_origin', '=', self.origin)])
        if not invoice.invoice_origin:
            if self.origin:
                data1 = self.env['sale.order'].search([('name', '=', self.origin)])
                id = data1.id
                data2 = self.env['sale.order.line'].search([('order_id', '=', id)])
                vals = {
                    'name': self.origin,
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
                    'invoice_origin': self.origin,
                    'invoice_user_id': data1.user_id.id,
                    'partner_id': data1.partner_invoice_id.id,
                    'currency_id': data1.pricelist_id.currency_id.id,
                    'invoice_line_ids': invoice_lines
                })
        return res





