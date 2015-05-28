# -*- coding: utf-8 -*-

from openerp import models, fields


class sample(models.Model):
    _inherit = 'sale.order.line'
    numberOfUnits = fields.Integer()
    isGift = fields.Boolean()
