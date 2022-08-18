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
            product.combo_product = data;
            _super_Order.add_product.call(self, product, options);
        });
        }
        else{
        _super_Order.add_product.call(self, product, options);
        }
		},
	});
    var _super_orderline = models.Orderline.prototype;
    models.Orderline = models.Orderline.extend({
    initialize: function(attr,options) {
      _super_orderline.initialize.call(this,attr,options);
      this.combo_product = false;
      this.is_combo = false;
      console.log(options);
    },
    init_from_JSON: function(json){
        _super_orderline.init_from_JSON.apply(this,arguments);
        this.get_product().combo_product = json.combo_product;
        this.get_product().is_combo = json.is_combo;
    },
    export_as_JSON: function(){
        var json = _super_orderline.export_as_JSON.apply(this,arguments);
        json.combo_product = this.get_product().combo_product;
        json.is_combo = this.get_product().is_combo;
        return json;
    },
    });

})