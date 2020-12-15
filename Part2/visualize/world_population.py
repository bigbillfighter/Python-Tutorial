import json
from country_codes import get_country_code
from pygal_maps_world.maps import World

# load the file to a list(pop_data)
filename = 'population_data.json'
with open(filename) as f_obj:
    pop_data = json.load(f_obj)

cc_populations = {}
# print the population of every country in 2010
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        code = get_country_code(country_name)
        population = int(float(pop_dict['Value']))
        if code:
            print(code+': '+ "{:,}".format(population)) # output as this format
            cc_populations[code] = population

cc_pop_1, cc_pop_2, cc_pop_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop <10000000:
        cc_pop_1[cc] = pop
    elif pop <100000000:
        cc_pop_2[cc] = pop
    else:
        cc_pop_3[cc] = pop

print(len(cc_pop_1), len(cc_pop_2), len(cc_pop_3))


wm = World()
wm.title = "World Population in 2010, by Country"
wm.add('0-10m', cc_pop_1)
wm.add('10m-100m', cc_pop_2)
wm.add('>100m', cc_pop_3)
wm.render_to_file('world_population.svg')




