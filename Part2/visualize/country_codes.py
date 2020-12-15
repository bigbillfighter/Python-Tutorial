from pygal_maps_world.i18n import COUNTRIES

def get_country_code(country_name):
    '''return the country based on the country's name'''
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
        # if not found, return 'None'

    return None

# print(get_country_code('China'))
# print(get_country_code('Andorra'))
# print(get_country_code('bbb'))


