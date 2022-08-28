# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Payment Acquirer Cash Free 01',
    'version': '15.0.0',
    'category': 'Accounting/Payment Acquirers',
    'sequence': 377,
    'summary': 'Payment Acquirer: Payment Cash Free Implementation',
    'description': """
Cash Free Payment Acquirer for India.

Cash Free payment gateway supports only INR currency.
""",
    'depends': ['payment'],
    'data': [
        'views/payment_views.xml',
        'views/payment_cash_free_templates.xml',
        'data/payment_acquirer_data.xml',
    ],
    'application': True,
    'pre_init_hook':'pre_init_hook',
    'uninstall_hook': 'uninstall_hook',
    'license': 'LGPL-3',

}
