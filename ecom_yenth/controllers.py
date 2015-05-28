# -*- coding: utf-8 -*-
from openerp import http
from openerp.http import request
from openerp.addons.website_sale.controllers.main import website_sale


class website_yenth(website_sale):

    @http.route(['/shop/extra'], type='http', auth="public", website=True)
    def extra(self, **post):
        order = request.website.sale_get_order()

        if post:
            for line in order.order_line:
                line.write({
                    'height': int(post.get('%s-%s' % (line.id, 'height'))),
                    'width': int(post.get('%s-%s' % (line.id, 'width'))),
                    'numberOfUnits': int(post.get('%s-%s' % (line.id, 'qty')))
                })
            request.session['extra_info_done'] = True
            return request.redirect("/shop/checkout")

        values = dict(order=order)
        return request.website.render("ecom_yenth.extra", values)

    @http.route(['/shop/confirm_order'], type='http', auth="public", website=True)
    def confirm_order(self, **post):
        if not request.session.get('extra_info_done'):
            return request.redirect("/shop/extra")
        return super(website_yenth, self).confirm_order(**post)
