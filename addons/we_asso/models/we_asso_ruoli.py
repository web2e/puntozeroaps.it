from odoo import models, fields, api

class AssoRuoli(models.Model):
    _name = 'asso.ruoli'
    _description = 'asso.ruoli'

    name = fields.Char("Ruolo", required=True)

    tipo_ruolo = fields.Selection([('ruoli_istituzionali', 'Ruoli istituzionali'),
                             ('altri_ruoli_inquadramento', 'Altri ruoli / inquadramento')],
                            string='Tipo ruolo')
    description = fields.Text()


