odoo.define("pos_combo_product.ProductScreen", function (require) {
    "use strict";
    const ProductScreen = require("point_of_sale.ProductScreen");
    const Registries = require("point_of_sale.Registries");
    var rpc = require('web.rpc');
    const pos_combo_product = (ProductScreen) =>
        class extends ProductScreen {
            async _getAddProductOptions(product)
            {
                var self = this;
                return rpc.query({
                    model: 'pos_combo_product.pos_combo_product',
                    method: 'combo_id',
                    args: [[],event.detail.combo_product_id],
                    }).then(function(data){
                    var combo_id = data;
                    var combo_product = [];
                    for(var i=0;i<combo_id.length;i++)
                    {
                    combo_product.push(self.env.pos.db.get_product_by_id(combo_id[i]));
                    }
                    return combo_product;
                });
            }
            async _clickProduct(event) {
                const product = event.detail;
                if(event.detail.is_combo)
                {
                const options = await this._getAddProductOptions(product);
                console.log(options);
                var self = this;
                const { confirmed } =await this.showPopup('ComboPopup', {
                title: this.env._t('Combo Product'),
                body: this.env._t(
                    'Are you sure purchase the product'
                ),
                product:options,
                });
                if(confirmed)
                {
                return super._clickProduct(event);
                }
                }
                else
                {
                return super._clickProduct(event);
                }
            }
        };

    Registries.Component.extend(ProductScreen, pos_combo_product);
    return ProductScreen;
});