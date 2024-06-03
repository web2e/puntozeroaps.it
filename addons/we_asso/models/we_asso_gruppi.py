from odoo import models, fields, api

class AssoGruppi(models.Model):
    _name = 'asso.gruppi'
    _description = 'asso.gruppi'

    name = fields.Char("Gruppo", required=True)
    description = fields.Text()

