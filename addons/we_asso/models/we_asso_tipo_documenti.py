from odoo import models, fields, api

class AssoTipoDocumenti(models.Model):
    _name = 'asso.tipo_documenti'
    _description = 'asso.tipo_documenti'

    name = fields.Char("Tipo documento", required=True)
    description = fields.Text()

