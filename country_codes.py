from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    """Возвращает для заданной страны ее код Pygal, состоящий из 2х букв."""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    """Возвращает None, если ничего не найдено."""
    return None
