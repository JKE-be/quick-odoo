# -*- coding: utf-8 -*-

from openerp import models, fields


class sample(models.Model):
    _inherit = 'sale.order.line'
    height = fields.Integer()
    width = fields.Integer()
    numberOfUnits = fields.Integer()
