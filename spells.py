from utilities import *

'''
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
'''

import sqlite3

class Spell:
    def __init__(self, **kwargs):
        """
        Initializes a Spell instance with attributes based on the provided dictionary.
        Each column name becomes an attribute.
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __repr__(self):
        """
        Returns a string representation of the Spell instance for debugging.
        """
        return f"Spell({', '.join(f'{k}={v}' for k, v in self.__dict__.items())})"

class Database:
    def __init__(self, db_name):
        self.db_name = db_name

    def fetch_spells(self, table_name, column_name, min_value):
        """
        Queries the database for rows where the given column has a value >= min_value.
        :param table_name: The name of the table to query.
        :param column_name: The column to filter on.
        :param min_value: The minimum value for filtering.
        :return: A list of Spell instances.
        """
        connection = sqlite3.connect(self.db_name)
        connection.row_factory = sqlite3.Row  # This enables access by column name
        cursor = connection.cursor()

        # Query to select rows
        query = f"SELECT * FROM {table_name} WHERE {column_name} >= ?"

        try:
            cursor.execute(query, (min_value,))
            rows = cursor.fetchall()

            # Instantiate Spell objects for each row
            spells = [Spell(**dict(row)) for row in rows]
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            spells = []
        finally:
            connection.close()

        return spells


# Example usage
db = Database('Database.db')

# Query for spells where 'whm' is 1 or higher
spells = db.fetch_spells('spells', 'whm', 1)

# Output the Spell instances
for spell in spells:
    variable_name = spell.name.lower()  # creates the variable using the name field from database
    globals()[variable_name] = spell
    print(spell.name)

print(dia.description)



