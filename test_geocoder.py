import timeit

print timeit.timeit("""g.address_to_latlng('99 BROADWAY')""",setup="""from geocoder import Geocoder
g = Geocoder('manhattan-addresses.bin', 'manhattan-kdtree.bin')""")
print timeit.timeit("""g.latlng_to_address((40.769083827890107,-73.952477804528087))""",setup="""from geocoder import Geocoder
g = Geocoder('manhattan-addresses.bin', 'manhattan-kdtree.bin')""")