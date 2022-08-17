odoo.define('pos_combo_product.ComboPopup', function(require) {
    'use strict';

    const AbstractAwaitablePopup = require('point_of_sale.AbstractAwaitablePopup');
    const Registries = require('point_of_sale.Registries');

    class ComboPopup extends AbstractAwaitablePopup {}
    ComboPopup.template = 'ComboPopup';
    ComboPopup.defaultProps = {
        confirmText: 'Ok',
        cancelText: 'Cancel',
        title: 'Combo Product',
        body: '',
    };

    Registries.Component.add(ComboPopup);

    return ComboPopup;
});
