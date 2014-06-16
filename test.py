import pyproj as pp
p0 = pp.Proj(init="esri:102718")
f2m = 0.3048006096012192
loc = (300383.98, 65449.33)  # <-- this is the PLUTO coordinates
loc = p0(loc[0], loc[1], inverse=True)
print 'Lat:', loc[1], 'Long:', loc[0]