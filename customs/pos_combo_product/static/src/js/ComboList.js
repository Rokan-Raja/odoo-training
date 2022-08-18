odoo.define('pos_combo_product.ComboList', function(require) {
    'use strict';

    const PosComponent = require('point_of_sale.PosComponent');
    const Registries = require('point_of_sale.Registries');

    class ComboList extends PosComponent {

        get imageUrl() {
            const product = this.props.product;
            return `/web/image?model=product.product&field=image_128&id=${product.id}&write_date=${product.write_date}&unique=1`;
        }
    }
    ComboList.template = 'ComboList';

    Registries.Component.add(ComboList);

    return ComboList;
});
