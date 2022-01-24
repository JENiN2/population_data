from pygal.maps.world import COUNTRIES

for country_code in sorted(COUNTRIES):
    print(country_code, COUNTRIES[country_code])