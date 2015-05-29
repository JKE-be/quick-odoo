# -*- coding: utf-8 -*-

from openerp import models, fields


class sample(models.Model):
    _inherit = 'sale.order.line'
    numberOfUnits = fields.Integer()
    isGift = fields.Boolean()


# TODO: access rule to do...
class sale_colorpicker(models.Model):
    _name = 'sale.colorpicker'
    _description = 'dropdown for order/quotation (pick colors)'
    name = fields.Char('Name', required=True)
    website_publish = fields.Boolean('Published')


class sale_order(models.Model):
    _inherit = 'sale.order'
    color = fields.Many2one('sale.colorpicker', 'Color')
