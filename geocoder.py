import pickle
import csv

class Geocoder:
    def __init__(self, address_filename, location_filename):
        self.addresses = pickle.load(open(address_filename))
        self.locations = pickle.load(open(location_filename))
        
        prefixes = list(csv.reader(open('address_prefix_standardization.txt')))
        self.prefixes = {}
        for p in prefixes:
            self.prefixes[p[0]] = p[1]
            
        suffixes = list(csv.reader(open('address_suffix_standardization.txt')))
        self.suffixes = {}
        for p in suffixes:
            self.suffixes[p[0]] = p[1]
        
    def address_to_latlng(self, str_addr):
        addr = str_addr.strip().upper()
        
        #standardize
        addrs = addr.split()
        new_addrs = []
        for w in addrs:
            if w in self.prefixes:
                w = self.prefixes[w]
            elif w in self.suffixes:    
                w = self.suffixes[w]
            new_addrs.append(w)
        addr = ' '.join(new_addrs)
        
        pos = addr.find(' ')
        if pos == -1:
            return None
        house_no = int(addr[:pos])
        street = addr[pos+1:].strip()
    
        if street not in self.addresses:
            return None
        
        addr_data = self.addresses[street]
    
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
    
    def latlng_to_address(self, tuple_loc):
        return self.locations.search(tuple_loc)