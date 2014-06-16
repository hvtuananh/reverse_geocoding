import pickle

def extract_middle_point(bbox):
    return ((bbox[0][0]+bbox[1][0])/2, (bbox[0][1]+bbox[1][1])/2)

def convert_latlng(addrs):
    results = ({}, {})
    for res in sorted(addrs):
        if res[0] % 2 == 0:
            results[1][res[0]/2] = extract_middle_point(res[1]['bbox'])
        else:
            results[0][res[0]] = extract_middle_point(res[1]['bbox'])
    return results

address_list = []
data = pickle.load(open('manhattan.bin'))
for res in data:
    address_list.append((res['street'], res['house_no'], res))

address_map = {}
last_addr = None
current_list = []
for tup in sorted(address_list):
    if last_addr != tup[0]:
        if len(current_list) > 0:
            address_map[last_addr] = convert_latlng(current_list)
            current_list = []
        last_addr = tup[0]
    current_list.append(tup[1:])
    
if len(current_list) > 0:
    address_map[last_addr] = convert_latlng(current_list)
    
pickle.dump(address_map, open('manhattan-addresses.bin','w'))