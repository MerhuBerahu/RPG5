

class Spell:

    def __init__(self, name, description, jobs, level, effect, effect_amount,mp_cost, cooldown, cast_time, modifier, modifier_amount, element_affinity):
        self.name = name
        self.description = description
        self.jobs = jobs
        self.level = level
        self.effect  = effect
        self.effect_amount = effect_amount
        self.mp_cost = mp_cost
        self.cooldown = cooldown
        self.cast_time =cast_time
        self.modifier = modifier
        self.modifier_amount = modifier_amount
        self.element_affinity = element_affinity


