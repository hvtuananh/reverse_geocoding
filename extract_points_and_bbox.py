import pyproj as pp
import shapefile
import pickle

p0 = pp.Proj(init="esri:102718")
f2m = 0.3048006096012192

def convert_latlng(loc):
    locx = p0(loc[0]*f2m, loc[1]*f2m, inverse=True)
    return (locx[1], locx[0])
    
sf = shapefile.Reader("Manhattan/MNMapPLUTO")
records = sf.records()
shapes = sf.shapes()

total = len(records)
results = []
for i in range(total):
    r = records[i]
    s = shapes[i]
    
    bbl = int(float(r[68]))
    addr = r[11].strip()
    zipcode = r[8]
    bbox = (convert_latlng(s.bbox[:2]), convert_latlng(s.bbox[2:]))
    points = []
    for loc in s.points:
        points.append(convert_latlng(loc))
        
    pos = addr.find(' ')
    if pos == -1:
        continue
    
    try:
        house_no = int(addr[:pos])
    except:
        #print bbl
        continue    
    
    street = addr[pos+1:].strip()
    
    #special case for 1/2 address
    if street[:3] == '1/2':
        street = street[4:]
        
    #special case for * address and Y address (only one)
    street = street.strip('*')
    if street == '':
        continue
    if street[:2] == 'Y ':
        street = street[2:]
        
    res = {}
    res['bbl'] = bbl
    res['addr'] = addr
    res['house_no'] = house_no
    res['street'] = street
    res['zipcode'] = zipcode
    res['bbox'] = bbox
    res['points'] = points
    
    results.append(res)
    
pickle.dump(results, open('manhattan.bin', 'w'))