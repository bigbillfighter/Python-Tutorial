from pygal_maps_world.maps import World
wm = World()
wm.title = "Populations of countries in North America"
wm.add('North America', {'ca': 34126000, 'us': 309249000, 'mx':113423000})

wm.render_to_file('na_populations.svg')