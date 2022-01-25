import pygal.maps.world

na = pygal.maps.world.World()
na.title = 'Populations of Countries in North America'
na.add('North America', {'ca': 34126000,
                         'us': 309349000,
                         'mx': 113423000})

#na.render_to_file('na_population.svg')
na.render()
