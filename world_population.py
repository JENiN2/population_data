import json

from country_codes import get_country_code

# Список заполняется данными.
filename = "data/population_data.json"
with open(filename) as f:
    pop_data = json.load(f)

print('World population in 2010:\n')
# Вывод населения за 2010 год.
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            print(f'{code}: {str(population)}')
        else:
            print(f'ERROR - {str(population)}')
