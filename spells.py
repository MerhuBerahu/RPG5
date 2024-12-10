import sqlite3

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

cure = Spell("Cure")



# Create a SQL connection to our SQLite database
conn = sqlite3.connect('Database.db')

c = conn.cursor()

def item_by_owned(owned):
    # Return all results of query
    c.execute('SELECT * FROM plots spells WHERE whm >= 1')
    return c.fetchall()

def print_inventory_names(inventory):
    for i in inventory: #print out the name(index[1] of each item in inventory
        print(i[1])   

inventory = item_by_owned()

# Return first result of query
#cur.execute('SELECT species FROM species WHERE taxa="Bird"')
#cur.fetchone()

# Be sure to close the connection
conn.close()





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