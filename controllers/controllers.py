# -*- coding: utf-8 -*-
from odoo import http


class AutoInvoice(http.Controller):
    @http.route('/auto_invoice/auto_invoice/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/auto_invoice/auto_invoice/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('auto_invoice.listing', {
            'root': '/auto_invoice/auto_invoice',
            'objects': http.request.env['auto_invoice.auto_invoice'].search([]),
        })

    @http.route('/auto_invoice/auto_invoice/objects/<model("auto_invoice.auto_invoice"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('auto_invoice.object', {
            'object': obj
        })
