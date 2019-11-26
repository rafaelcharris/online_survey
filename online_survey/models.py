from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'UEC'

doc = """
online experiment
"""


class Constants(BaseConstants):
    name_in_url = 'online_survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

def preg_likert(label):
    return models.IntegerField(
        label = label,
        min  = 1, max = 5,
        widget=widgets.Slider,
    )

class Player(BasePlayer):

    pol_participation = models.BooleanField(label = "¿Usted asistió en la marcha del Paro Nacional del 21 de noviembre pasado?",
                                             choices = [[True, "Sí"],
                                                       [False, "No"]]
                                             )
    belief_pol = models.IntegerField(label = "¿Qué porcentaje de personas, que van a responder este estudio, cree usted que asistieron en la marcha del Paro Nacional del 21 de noviembre pasado?",
                                             choices = [[1, "[0% -20%]"],
                                                       [2, "[21% - 40%]"],
                                                        [3, "[41% - 60%]"],
                                                        [4, "[61% - 80%]"],
                                                        [5, "[81% - 100%]"]]
                                     )

    belief_norm = models.BooleanField(label = "¿Cree que la gente debería asistir a las marchas y actividades relacionadas con el Paro Nacional?",
                                      choices=[[True, "Sí"],
                                               [False, "No"]]
                                      )

    belief_emp = models.IntegerField(label = "¿Qué porcentaje de personas, que van a responder este estudio, cree usted que respondieron sí ea la pregunta anterior?",
                                     choices = [[1, "[0% -20%]"],
                                                       [2, "[21% - 40%]"],
                                                        [3, "[41% - 60%]"],
                                                        [4, "[61% - 80%]"],
                                                        [5, "[81% - 100%]"]]
                                     )

    barrio_violento = preg_likert(
        label='¿Está de acuerdo con la afirmación “el barrio donde vivo es violento”? '
              'Por favor, conteste usando la siguiente escala de uno a cinco, donde uno indica “estoy totalmente en desacuerdo” y 5 indica “estoy totalmente de acuerdo”.'
    )
    barrio_ayuda = models.BooleanField(
        label='Si usted llegara a necesitar ayuda, ¿acudiría a alguien desconocido de su mismo barrio?'
    )
    barrio_seguro = models.BooleanField(
        label='¿Se siente seguro mientras camina en la tarde en su barrio?'
    )

    trust = models.IntegerField(labels = "¿Cómo se ve a usted mismo?"
                                          "Mientras no me convenzan de lo contrario, asumo que las personas tienen las mejores intenciones. "
                                          "Por favor, use la escala de 0 a 10 que aparece abajo, donde 0 significa \"No me describe en absoluto\" y 10 significa \"Me describe perfectamente\". "
                                          "También puede usar los valores intermedios para indicar dónde se encuentra en la escala.",
                                min = 1,
                                max =10,
                                widget = widgets.Slider)

    #Emotion

    interesado = models.IntegerField(choices= [1,2,3,4,5])
    afligido = models.IntegerField(choices= [1,2,3,4,5])
    Excitado = models.IntegerField(choices=[1, 2, 3, 4, 5])
    Disgustado = models.IntegerField(choices=[1, 2, 3, 4, 5])
    Fuerte = models.IntegerField(choices=[1, 2, 3, 4, 5])
    Culpable = models.IntegerField(choices=[1, 2, 3, 4, 5])
    Asustado = models.IntegerField(choices=[1, 2, 3, 4, 5])
    Hostil = models.IntegerField(choices=[1, 2, 3, 4, 5])
    Entusiasmado = models.IntegerField(choices=[1, 2, 3, 4, 5])
    Orgulloso = models.IntegerField(choices=[1, 2, 3, 4, 5])
    Irritable = models.IntegerField(choices=[1, 2, 3, 4, 5])
    Alerta = models.IntegerField(choices=[1, 2, 3, 4, 5])
    Avergonzado = models.IntegerField(choices=[1, 2, 3, 4, 5])
    Inspirado = models.IntegerField(choices=[1, 2, 3, 4, 5])
    Nervioso = models.IntegerField(choices=[1, 2, 3, 4, 5])
    Atento = models.IntegerField(choices=[1, 2, 3, 4, 5])
    Temeroso = models.IntegerField(choices=[1, 2, 3, 4, 5])