from odoo import models, fields, api


class GruppiLines(models.Model):
    _name = 'asso.anagrafiche.gruppi.lines'
    _description = 'Gruppi anagrafiche lines'

    gruppi_id = fields.Many2one('asso.gruppi', string='Gruppi')
    anagrafica_id = fields.Many2one('asso.anagrafiche', store=True,
                                    string='Anagrafica')


class TagLines(models.Model):
    _name = 'asso.anagrafiche.tag.lines'
    _description = 'Tag anagrafiche lines'

    tag_id = fields.Many2one('asso.tag', string='Tag')
    anagrafica_id = fields.Many2one('asso.anagrafiche', store=True,
                                    string='Anagrafica')


class RuoliAssociatoLines(models.Model):
    _name = 'asso.anagrafiche.ruoli.lines'
    _description = 'Ruoli anagrafiche lines'

    ruolo_id = fields.Many2one('asso.ruoli', string='Ruolo')

    # Data invio richiesta, Data approvazione, Data Cessazione
    data_invio_richiesta = fields.Date("Data invio richiesta")
    data_approvazione = fields.Date("Data appravazione")
    data_cessazione = fields.Date("Data cessazione")

    anagrafica_id = fields.Many2one('asso.anagrafiche', store=True,
                                    string='Anagrafica')


class DocumentiLines(models.Model):
    _name = 'asso.anagrafiche.documenti.lines'
    _description = 'Documenti anagrafiche lines'

    # documento_id = fields.Many2one('asso.documenti',string='Documento')
    name = fields.Char("Documento", required=True)

    attachment_ids = fields.Many2many('ir.attachment', 'asso_document_ir_attachments_rel',
                                      'document_id', 'attachment_id', string="Attachments",
                                      help="Documenti allegati")

    tipo_documento_id = fields.Many2one('asso.tipo_documenti', string="Tipo documento")
    anagrafica_id = fields.Many2one('asso.anagrafiche', store=True,
                                    string='Anagrafica')

    data_scadenza = fields.Date("Data scadenza")
    is_private = fields.Boolean('Privato', default=False)


class AssoAnagrafiche(models.Model):
    _name = "asso.anagrafiche"
    _description = "Asso Anagrafiche"
    _inherits = {"res.partner": "partner_id"}
    _inherit = ["mail.thread", "mail.activity.mixin"]

    partner_id = fields.Many2one(
        "res.partner", delegate=True, ondelete="cascade", required=True
    )
    ruoli_line_ids = fields.One2many('asso.anagrafiche.ruoli.lines', 'anagrafica_id', string='Ruoli')
    tag_line_ids = fields.One2many('asso.anagrafiche.tag.lines', 'anagrafica_id', string='Tag')
    gruppi_line_ids = fields.One2many('asso.anagrafiche.gruppi.lines', 'anagrafica_id', string='Gruppi')
    documenti_line_ids = fields.One2many('asso.anagrafiche.documenti.lines', 'anagrafica_id', string='Documenti')

    tipo = fields.Selection([('persona', 'Persona'), ('ente', 'Ente'), ], string='Tipo', default='persona')

    is_associato = fields.Boolean('Associato')
    is_volontario = fields.Boolean('Volontario')

    tipo_ente = fields.Selection([
        ('pubblico', 'Pubblico'),
        ('privato', 'Privato'),
        ('terzo_settore', 'Terzo settore'),
    ], string='Tipo ente')

    tipo_associato = fields.Selection([
        ('Associato speciale', 'Associato speciale'),
        ('Associato ordinario', 'Associato ordinario'),
        ('Associato benemerito', 'Associato benemerito'),
        ('Associato fondatore', 'Associato fondatore'),
    ], string='Tipo associato')

    codice_tessera = fields.Char("Codice Tessera")
    gender = fields.Selection([('male', 'Maschio'), ('female', 'Femmina'), ], string='Sesso')
    luogo_nascita = fields.Char("Luogo di nascita")
    data_nascita = fields.Date("Data di nascita")

    note = fields.Text(string='Note')
    note_operative = fields.Text(string='Note operative')

    codice_fiscale = fields.Char("Codice fiscale")
    indirizzo = fields.Char("Indirizzo")
    city = fields.Char("Città")
    provincia = fields.Char("Provincia")
    cap = fields.Char("Cap")
    nazione = fields.Char("Nazione")

    iscrizioni_count = fields.Integer(string="Iscrizioni count", compute="_compute_iscrizioni_count")

    # calcola il numero di iscrizioni per un dato customer
    def _compute_iscrizioni_count(self):
        for rec in self:
            iscrizioni_count = self.env['asso.iscrizioni'].search_count([('associato_id', "=", rec.id)])
            rec.iscrizioni_count = iscrizioni_count

    # metodo richiamato dallo smart botton Trattamenti <button name="action_open_trattamenti"
    def action_asso_iscrizioni(self):
        # ritorna l'action, ID Esterno: we_health_beauty.action_appointment
        action = self.env["ir.actions.actions"]._for_xml_id("we_asso.action_asso_iscrizioni")
        # filtro sul cliente, visualizza solo i trattamenti del cliente
        action['domain'] = [('associato_id', '=', self.id)]
        action['views'] = [(3598, 'tree'), (3599, 'form')]
        return action
