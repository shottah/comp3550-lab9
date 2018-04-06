import json
from pokelist.models import Pokemon


with open('pokedata.json') as data_file:
    data = json.load(data_file)

for poke in data:
    obj = poke['fields']
    if 'type_2' in obj:
        p = Pokemon(name=obj['name'], hp=obj['hp'], type_1=obj['type_1'], type_2=obj['type_2'], attack=obj['attack'], defense=obj['defense'], sp_atk=obj['sp_atk'], sp_def = obj['sp_def'], total=obj['total'], speed=obj['speed'])
    else:
        p = Pokemon(name=obj['name'], hp=obj['hp'], type_1=obj['type_1'], attack=obj['attack'], defense=obj['defense'], sp_atk=obj['sp_atk'], sp_def = obj['sp_def'], total=obj['total'], speed=obj['speed'])
    p.save()


# to run type in shell: exec(open('import.py').read()) or python manage.py shell < import.py from cmd