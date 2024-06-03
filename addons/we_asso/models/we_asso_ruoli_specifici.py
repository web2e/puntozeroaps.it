from odoo import models, fields, api

class AssoRuoliSpecifici(models.Model):
    _name = 'asso.ruoli_specifici'
    _description = 'asso.ruoli_specifici'

    name = fields.Char("Ruolo Specifico", required=True)
    ruolo = fields.Many2one('asso.ruoli', string='Ruolo')
    ordinamento = fields.Integer(string='Ordinamento')
    description = fields.Text()


