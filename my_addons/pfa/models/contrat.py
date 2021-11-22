# -*- coding: utf-8 -*-


from odoo import models, fields, api, exceptions, _

class Contrat(models.Model):
    _name = 'pfa.contrat'
    _rec_name = 'num_contrat'


    num_contrat = fields.Char('Numéro du contrat', required=True)
    deb = fields.Date('Début date de validité')
    fin = fields.Date('Fin date de validité')
    color = fields.Integer()
    client_id = fields.One2many('pfa.client', 'contrat_id')
    state = fields.Selection([
        ('non_signe', "Non signé"),
        ('signe', "Signé")
    ],default='non_signe', string="Etat")


    def action_non_signe(self):
        for rec in self:
            rec.state = 'non_signe'

    def action_signe(self):
        for rec in self:
            rec.state = 'signe'

    _sql_constraints = [
        ('num_contrat_unique',
         'UNIQUE(num_contrat)',
         "Le numéro du contrat devrait être UNIQUE")
    ]