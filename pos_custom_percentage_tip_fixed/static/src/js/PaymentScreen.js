odoo.define('pos_custom_percentage_tip_fixed.tips', function (require) {
    'use strict';

   const Registries = require('point_of_sale.Registries');
   var { PosGlobalState } = require('point_of_sale.models');
   const PaymentScreen = require('point_of_sale.PaymentScreen');
   const { parse } = require('web.field_utils');

    const CustomButtonPaymentScreen = (PaymentScreen) =>
       class extends PaymentScreen {
           setup() {
               super.setup(...arguments);
           }
           /* Click function of custom tip button */
           async CustomTipButton(){
                // It is used to update the tip to payment
                var custom_tip_percentage = this.env.pos.config.custom_tip_percentage
                if(custom_tip_percentage){
                    this.env.pos.tips = true;
                    this.env.pos.custom_tip = custom_tip_percentage
                    var cust_tip = ((this.currentOrder.get_total_with_tax() + this.currentOrder.get_rounding_applied() ) * parseInt(custom_tip_percentage) /100);
                    let value = cust_tip === 0 && change > 0 ? change : cust_tip;
                    const { confirmed, payload } = await this.showPopup('NumberPopup', {
                        title: cust_tip ? this.env._t('Change Tip') : this.env._t('Add Tip'),
                        startingValue: value,
                        isInputSelected: true,
                    });
                    if (confirmed) {
                        this.currentOrder.set_tip(parse.float(payload.toString()));
                    }
                    }
           }
           get Tips() {
           // calculates the tips and return to the template
                var custom_tip_percentage = this.env.pos.config.custom_tip_percentage
                if(custom_tip_percentage){
                    this.env.pos.tips = true;
                    this.env.pos.custom_tip = custom_tip_percentage
                    }
                else{
                    this.env.pos.tips = false;
                }
                return {
                        tip:custom_tip_percentage,
                        tip_enable:this.env.pos.tips,
                };
           }
       };
   Registries.Component.extend(PaymentScreen, CustomButtonPaymentScreen);
   return CustomButtonPaymentScreen;
});