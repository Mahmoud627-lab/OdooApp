# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _

class Voiture(models.Model):
    _name = 'pfa.voiture'
    _rec_name = 'immatriculation'

    immatriculation = fields.Char('Immatriculation', required=True)
    marque = fields.Char('Marque', required=True)
    model = fields.Char('Modèle', required=True)
    couleur = fields.Char('Couleur', required=True)
    power = fields.Char('Puissance')
    km_parcouru = fields.Char('Nombre Km parcouru')

    nb_jour_location = fields.Integer('Nombre de jours de location',  required=True)
    prix = fields.Float('Prix de location par jour', required=True)

    @api.depends('prix', 'nb_jour_location')
    def _calculer_prix_location(self):
            self.prix_location = self.prix * self.nb_jour_location

    prix_location = fields.Char(string='Prix de location', compute='_calculer_prix_location')


    state = fields.Selection([
        ('non_louee', "Non louée"),
        ('louee', "Louée")
    ], default='non_louee', string="Etat")
    image_voiture = fields.Binary()
    color = fields.Integer()
    client_id = fields.One2many('pfa.client', 'voiture_id')


    def action_non_louee(self):
        for rec in self:
            rec.state = 'non_louee'

    def action_louee(self):
        for rec in self:
            rec.state = 'louee'

    _sql_constraints = [
        ('immatriculation_unique',
         'UNIQUE(immatriculation)',
         "l'immatriculation de la voiture devrait être UNIQUE")
    ]