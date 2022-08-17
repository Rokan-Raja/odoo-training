# -*- coding: utf-8 -*-
from odoo import http


class PosComboProduct(http.Controller):
    @http.route('/pos_combo_product/pos_combo_product/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/pos_combo_product/pos_combo_product/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('pos_combo_product.listing', {
            'root': '/pos_combo_product/pos_combo_product',
            'objects': http.request.env['pos_combo_product.pos_combo_product'].search([]),
        })

    @http.route('/pos_combo_product/pos_combo_product/objects/<model("pos_combo_product.pos_combo_product"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('pos_combo_product.object', {
            'object': obj
        })
