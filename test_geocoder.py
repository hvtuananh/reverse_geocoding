import timeit
from geocoder import Geocoder
g = Geocoder('manhattan-addresses.bin', 'manhattan-kdtree.bin')

print g.address_to_latlng('10 WEST 49 STREET')
print g.address_to_latlng('10 WEST 49 ST')
print g.address_to_latlng('10 W 49 ST')


print timeit.timeit("""g.address_to_latlng('99 BROADWAY')""",setup="""from geocoder import Geocoder
g = Geocoder('manhattan-addresses.bin', 'manhattan-kdtree.bin')""")

'''
print timeit.timeit("""g.latlng_to_address((40.769083827890107,-73.952477804528087))""",setup="""from geocoder import Geocoder
g = Geocoder('manhattan-addresses.bin', 'manhattan-kdtree.bin')""")
'''