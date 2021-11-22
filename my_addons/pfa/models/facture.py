# -*- coding: utf-8 -*-


from odoo import models, fields, api, exceptions, _

class Facture(models.Model):
    _name = 'pfa.facture'
    _rec_name = 'num_fact'

    num_fact = fields.Char('Numéro facture', required=True)
    date_fact = fields.Date('Date facture')
    color = fields.Integer()
    client_id = fields.One2many('pfa.client', 'facture_id')

    state = fields.Selection([
        ('draft', "Brouillon"),
        ('saved', "Enregistrée"),
        ('in_payment', "En paiement"),
        ('paied', "Payée")
    ],default='draft', string="Etat")

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

    def action_saved(self):
        for rec in self:
            rec.state = 'saved'

    def action_in_payment(self):
        for rec in self:
            rec.state = 'in_payment'

    def action_paied(self):
        for rec in self:
            rec.state = 'paied'

    # @api.multi
    # def get_report(self):
    #     return self.env.ref('pfa.facture_report') .report_action(self)

    _sql_constraints = [
        ('num_facture_unique',
         'UNIQUE(num_fact)',
         "Le numéro de la facture devrait être UNIQUE")
    ]