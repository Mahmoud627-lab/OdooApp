# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _

class Client(models.Model):
    _name = 'pfa.client'
    _rec_name = 'num_client'

    num_client = fields.Char(string='Numéro client', required=True)
    nom = fields.Char('Nom', required=True)
    prenom = fields.Char('Prénom', required=True)
    cin = fields.Char('Numéro CIN', required=True)
    # gov = fields.Selection([
    #     ('ariana', "Ariana"),
    #     ('tunis', "Tunis"),
    #     ('manouba', "Manouba"),
    #     ('bana', "Ben Arous"),
    # ], string='Gouvernorat')
    tel = fields.Char('Téléphone', required=True)
    poste_code = fields.Char('Code postal', required=True)
    adresse = fields.Char('Adresse', required=True)
    num_permis = fields.Char('Numéro permis')
    date_permis = fields.Date('Date permis')
    color = fields.Integer()

    voiture_id = fields.Many2one('pfa.voiture', string="Voiture", readonly=True)
    facture_id = fields.Many2one('pfa.facture', string="Facture", readonly=True)
    contrat_id = fields.Many2one('pfa.mahmoud', string="Contrat", readonly=True)

    _sql_constraints = [
        ('num_client_unique',
         'UNIQUE(num_client)',
         "Le numéro du client devrait être UNIQUE")
    ]

    _sql_constraints = [
        ('cin_unique',
         'UNIQUE(cin)',
         "Le numéro de la CIN devrait être UNIQUE")
    ]

    @api.constrains('cin')
    def _check_cin(self):
        for record in self:
            if len(record.cin) > 8 or len(record.cin) < 8:
                raise exceptions.ValidationError("longueur  de CIN devrait être égale à 8")
            if not (record.cin.isdigit()):
                raise exceptions.ValidationError("CIN devrait être des composée de chiffres")
