odoo.define('pos_combo_product.ComboCheck', function (require) {
  "use strict";

    const Registries = require('point_of_sale.Registries');
    const PosComponent = require('point_of_sale.PosComponent');
    const {Gui} = require('point_of_sale.Gui');

	var models = require('point_of_sale.models');
	var rpc = require('web.rpc')
    models.load_fields("product.product", ['is_combo', 'combo_product_id', 'combo_price']);
    var _super_Order = models.Order.prototype;
	models.Order = models.Order.extend({
		add_product: function(product, options){
		var self = this;
		if(product.is_combo)
		{
		product.lst_price = product.combo_price;
        var res = rpc.query({
            model: 'pos_combo_product.pos_combo_product',
            method: 'combo_data',
            args: [[], [product.product_tmpl_id]],
            }).then(function(data){
            product.combo_product_id = data;
            _super_Order.add_product.call(self, product, options);
        });
        }
        else{
        _super_Order.add_product.call(self, product, options);
        }
		},
	});
	var _super_Product = models.Product.prototype;
	models.Product = models.Product.extend({
    initialize: function(attr, options){
        if(options.is_combo)
        {
        var res = rpc.query({
            model: 'pos_combo_product.pos_combo_product',
            method: 'combo_data',
            args: [[], options.product_tmpl_id],
            }).then(function(data){
            options.combo_product_id = data;
        });
        options.lst_price = options.combo_price;
        }
        _.extend(this, options);
    },
    });
})