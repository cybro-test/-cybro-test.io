# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2023-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Ruksana P(<https://www.cybrosys.com>)
#
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
{
    'name': 'Pos Custom Tips',
    'depends': ['base', 'point_of_sale', 'pos_sale'],
    'version': '15.0.1.0.0',
    'summary': """To apply a fixed percentage of tip""",
    'description': """To apply a fixed percentage of tip to orders and
     it will update in the receipt.
    we set a tip percentage it will be applied to the orders""",
    'author': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'website': 'https://www.cybrosys.com',
    'category': 'Point Of Sale',
    'data': {
        'views/pos_config_views.xml',
    },
    'assets': {
        'point_of_sale.assets': [
            'pos_custom_percentage_tip_fixed/static/src/js/PaymentScreen.js',
        ],
        'web.assets_qweb': [
            'pos_custom_percentage_tip_fixed/static/src/xml/PaymentScreen.xml',
        ],
    },
    'images': ['static/description/banner.png'],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
