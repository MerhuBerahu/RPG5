class Job:

    def __init__(self, name, description, hp, mp,spell_list,ability_list):
        self.name = name
        self.description = description
        self.hp = hp
        self.mp = mp
        self.spell_list = spell_list
        self.ability_list = ability_list


whm = Job("White Mage", "Healer", 7, 8,["cure", "Dia"],["Dual Wield","Run"])

#print(whm.description)


"""
#White Mage
white_mage = {'name': 'White Mage', 'description': 'Healer','hp':7 ,'mp':8 ,'spelllist': {
'cure': {'name': 'Cure','description': 'Restore\'s HP','level': 1, 'effect': 'healing','amount':2, 'mp_cost': 8, 'cast_time': 3,'modifier':'playerMind','modifier_amount':10,'element': 'lightsday'},
'dia': {'name': 'Dia','description' : 'Lowers an enemy\'s defense and gradually deals Light elemental damage.','level': 3, 'effect': 'enfeebling','amount':2, 'mp_cost': 7, 'cast_time': 3,'modifier':'enemyMind','modifier_amount':10,'element': 'lightsday'},
'paralyze': {'name': 'Paralyze','description': 'Paralyzes an enemy.','level': 4, 'effect': 'enfeebling','amount':2, 'mp_cost': 6, 'cast_time': 3,'modifier':'enemyMind','modifier_amount':10,'element': 'lightsday'},
'banish': {'name': 'Banish','description': 'Deals Light elemental damage to an enemy.','level': 5, 'effect': 'damage','amount':2, 'mp_cost': 15, 'cast_time': 3,'modifier':'playerMind','modifier_amount':10,'element': 'lightsday'},
'barstonra': {'name': 'Barstonra','description': 'Increases resistance against Earth.','level': 5, 'effect': 'enhancing','amount':2, 'mp_cost': 12, 'cast_time': 1,'modifier':'playerMind','modifier_amount':10,'element': 'windsday'}},
'abilities': {'rage':{'level': 1, 'effect': 'Damage x2, Defense halved', 'tp_cost': 100, 'cast_time':3,'modifier':'playerStrength'}}, 
'armourtype': 'robes'}
"""