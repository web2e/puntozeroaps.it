from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale

class AssoAnagrafiche(http.Controller):

    @http.route('/associato_webform', type="http", auth="public", website=True)
    def associato_webform(self, **kw):
        print("Execution Here.........................")
        return http.request.render('we_asso.create_associato', {})

    @http.route('/create/associato', type="http", auth="public", website=True)
    def create_associato(self, **kw):
        print("Data Received.....", kw)
        request.env['asso.anagrafiche'].sudo().create(kw)
        # doctor_val = {
        #     'name': kw.get('patient_name')
        # }
        # request.env['hospital.doctor'].sudo().create(doctor_val)
        return request.render("we_asso.associato_thanks", {})