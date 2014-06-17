import pickle
import time

data = pickle.load(open('manhattan-addresses.bin'))

def geocoder(addr):
    addr = addr.strip().upper()
    pos = addr.find(' ')
    if pos == -1:
        return None
    house_no = int(addr[:pos])
    street = addr[pos+1:].strip()
    
    if street not in data:
        return None
        
    addr_data = data[street]
    
    if house_no % 2 == 0:
        addr_data = addr_data[1]
        house_no /= 2
    else:
        addr_data = addr_data[0]
        
    if house_no > max(addr_data.keys()) or house_no < min(addr_data.keys()):
        return None
        
    if house_no in addr_data:
        return addr_data[house_no]
    else:
        min_no = house_no
        while(1):
            if min_no not in addr_data:
                min_no -= 1
                if min_no <= -1:
                    min_no = min(addr_data.keys())
                    break
            else:
                break
                
        max_no = house_no
        while(1):
            if max_no not in addr_data:
                max_no += 1
                if max_no >= len(addr_data):
                    max_no = max(addr_data.keys())
                    break
            else:
                break
            
        min_pos = addr_data[min_no]
        max_pos = addr_data[max_no]
        
        if min_no == max_no:
            return None
    
        return (min_pos[0]+(max_pos[0]-min_pos[0])*(house_no-min_no)/(max_no-min_no),
                min_pos[1]+(max_pos[1]-min_pos[1])*(house_no-min_no)/(max_no-min_no))

def query(addr):
    start = time.clock()
    loc = geocoder(addr)
    exec_time = time.clock() - start
    return {'result':loc, 'time':exec_time}
    
print query('58 STONE STREET')
print query('11 STONE STREET')
print query('59 STONE STREET')
print query('550 BROADWAY')
print query('600 BROADWAY')
print query('2000 BROADWAY')
print query('1555 BRADWAY')
print query('99 BROADWAY')