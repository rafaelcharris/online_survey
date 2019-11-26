from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class BX(Page):
    form_model = 'player'
    form_fields = [
        "pol_participation",
        "belief_pol",
        "belief_norm",
        "belief_emp"
    ]

class demo(Page):
    form_model = 'player'
    form_fields = [
        "barrio_violento",
        "barrio_ayuda",
        "barrio_seguro",
        "trust"
        ]


class emotions(Page):
    form_model = 'player'
    form_fields = [
        "interesado", "afligido","Excitado", "Disgustado", "Fuerte", "Culpable", "Asustado", "Hostil", "Entusiasmado", "Orgulloso", "Irritable", "Alerta", "Avergonzado",
        "Inspirado", "Nervioso", "Atento", "Temeroso"
    ]


page_sequence = [BX, demo, emotions]
