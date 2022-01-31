import sys
import json
import argparse

import pygal.maps.world
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS

from country_codes import get_country_code


def get_year():
    parser = argparse.ArgumentParser(description='Creating of an interactive map, showing population by country.')
    parser.add_argument(
        '--year', type=str, required=True, help='Enter year, from 1960 to 2010.'
    )
    args = parser.parse_args()
    year = args.year
    print(f'You choose {year}')
    return year


def check_year(year):
    if int(year) > 2010 or int(year) < 1960:
        print('Wrong year')
        sys.exit()


def get_population_data():
    # Список заполняется данными.
    filename = "data/population_data.json"
    with open(filename) as f:
        pop_data = json.load(f)
    return pop_data


class PopDataProcessing:
    """Класс для обработки данных о численности населения"""
    def pop_data_processing(self, data, year):
        # Построение словаря с данными численности населения.
        cc_populations = {}
        for pop_dict in data:
            if pop_dict['Year'] == year:
                country_name = pop_dict['Country Name']
                population = int(float(pop_dict['Value']))
                code = get_country_code(country_name)
                if code:
                    cc_populations[code] = population
        return cc_populations

    def group_countries(self, cc_populations):
        # Круппировка стран по 3 уровням населения.
        cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
        for cc, pop in cc_populations.items():
            if pop < 10000000:
                cc_pops_1[cc] = pop
            elif pop < 1000000000:
                cc_pops_2[cc] = pop
            elif pop > 1000000000:
                cc_pops_3[cc] = pop
        cc_pop_list = cc_pops_1, cc_pops_2, cc_pops_3
        return cc_pop_list


def create_map(cc_pop_list, year):
    # Отрисовка карты.
    cc_pops_1, cc_pops_2, cc_pops_3 = cc_pop_list
    wm_style = RS('#336699', base_style=LCS)
    wm = pygal.maps.world.World(style=wm_style)
    wm.title = f'World Population in {year}, by Country'
    wm.add('0-10m', cc_pops_1)
    wm.add('10m1-1bn', cc_pops_2)
    wm.add('>1bn', cc_pops_3)
    wm.render_to_file(f'world_population_in_{year}.svg')


if __name__ == '__main__':
    year = get_year()
    check_year(year)
    get_data = get_population_data()
    processing = PopDataProcessing()
    population = processing.pop_data_processing(get_data, year)
    cc_pop_list = processing.group_countries(population)
    create_map(cc_pop_list, year)
