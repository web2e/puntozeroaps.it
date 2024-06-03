# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AssoIscrizioni(models.Model):
    _name = 'asso.iscrizioni'
    _description = 'asso.iscrizioni'
    _order = "pagamento_date desc"

    associato_id = fields.Many2one('asso.anagrafiche', 'Associato')

    name = fields.Char(string='Codice iscrizione', store=True)
    pagamento_date = fields.Date(string='Data pagamento', required=True)

    state = fields.Selection([('bozza', 'Bozza'), ('attiva', 'Attiva'),
                              ('scaduta', 'Scaduta'), ('annullata', 'Annullata')], default='attiva',
                             string="Stato")

    currency_id = fields.Many2one(
        'res.currency', string='Currency')
    importo = fields.Monetary()


    modalita_pagamento = fields.Selection([('cash', 'Contanti'), ('bonifico', 'Bonifico'),
                              ('carta', 'Carta')], default='cash',
                             string="Modalita pagamento")
    description = fields.Text()


    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', 'New') is False:
                vals['name'] = self.env['ir.sequence'].next_by_code(
                    'sequence.iscrizione.code') or 'New'
            create_id = super().create(vals)
            return create_id
