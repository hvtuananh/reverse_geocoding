import pickle

data = pickle.load(open('manhattan-addresses.bin'))

def geocoder(addr):
    addr = addr.strip().upper()
    pos = addr.find(' ')
    if pos == -1:
        print 'Wrong address format.'
        return
    house_no = int(addr[:pos])
    street = addr[pos+1:].strip()
    
    if street not in data:
        print 'Address not found.'
        return
        
    addr_data = data[street]
    
    if house_no % 2 == 0:
        addr_data = addr_data[1]
        house_no /= 2
    else:
        addr_data = addr_data[0]
        
    if house_no in addr_data:
        return addr_data[house_no]
    else:
        min_no = house_no
        while(1):
            if min_no not in addr_data:
                min_no -= 1
                if min_no == -1:
                    min_no += 1
                    break
            else:
                break
                
        max_no = house_no
        while(1):
            if max_no not in addr_data:
                max_no -= 1
                if max_no == len(addr_data):
                    max_no -= 1
                    break
            else:
                break
            
        min_pos = addr_data[min_no]
        max_pos = addr_data[max_no]
    
        #will need proper assignment tomorrow
        print min_no, max_no
        return ((min_pos[0]+max_pos[0])/2, (min_pos[1]+max_pos[1])/2) 
    
print geocoder('58 STONE STREET')
#print geocoder('11 STONE STREET')