odoo.define("pos_combo_product.ProductScreen", function (require) {
    "use strict";
    const ProductScreen = require("point_of_sale.ProductScreen");
    const Registries = require("point_of_sale.Registries");
    const pos_combo_product = (ProductScreen) =>
        class extends ProductScreen {
            async _clickProduct(event) {
                console.log(event.detail.combo_product_id);
                if(event.detail.is_combo)
                {
                const { confirmed } = await this.showPopup('ComboPopup', {
                title: this.env._t('Combo Product'),
                body: this.env._t(
                    'Are you sure purchase the product'
                ),
                product: event.detail,
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