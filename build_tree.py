import pickle
from kdtree import KdNode

def build_kdtree(data, depth):
    print depth
    #depth: even = lat, odd = lng (start from 0)
    root = KdNode()
    total = len(data)
    
    print "Total:", total
    
    if total < 2:
        #need to attach value into KdNode
        print data[0]['bbox']
    else:
        data = sorted(data, key=lambda res: res['bbox'][0][depth%2])
        pivot_index = total/2
        root.pivot = data[pivot_index]['bbox'][0][depth%2]
        
        #if total == 3
        if total == 3:
            print data[0]['bbox']
            print data[1]['bbox']
            print data[2]['bbox']
        
        #handle boundary case: total = 2
        if total == 2:
            print "Total = 2!"
            root.left = build_kdtree(data[:1], depth+1)
            root.right = build_kdtree(data[1:], depth+1)
        else:
            print "Pivot:", pivot_index
            print "Root Pivot:", root.pivot
        
            #build the left tree
            left_pivot = pivot_index
            while left_pivot < total and data[left_pivot]['bbox'][0][depth%2] == data[pivot_index]['bbox'][0][depth%2]:
                left_pivot += 1
            
            data_left = data[:left_pivot]
        
            #the right tree is more tricky since we also need some of items from left tree
            data_right = data[left_pivot:]
            data_candidate = sorted(data[:left_pivot], key=lambda res:res['bbox'][1][depth%2], reverse=True)
            for res in data_candidate:
                if res['bbox'][1][depth%2] < data[pivot_index]['bbox'][0][depth%2]:
                    break
                data_right.append(res)
                
            #avoid infinitive loop
            if len(data_left) == total or len(data_right) == total:
                #employ slow function
                idx_l = 0
                idx_r = total - 1
                data_left = []
                data_right = []
                #ensure at least 1 item in both list
                if data[idx_l]['bbox'][1][depth%2] < data[idx_r]['bbox'][0][depth%2]:
                    data_left.append(data[idx_l])
                    data_right.append(data[idx_r])
                    root.pivot = (data[idx_l]['bbox'][1][depth%2] + data[idx_r]['bbox'][0][depth%2]) / 2
                    print "Root Pivot:", root.pivot
                    for i in range(idx_l+1, idx_r):
                        print data[i]['bbox'][0][depth%2]
                        print (data[i]['bbox'][0][depth%2] < root.pivot)
                        if data[i]['bbox'][0][depth%2] < root.pivot:
                            data_left.append(data[i])
                        if data[i]['bbox'][1][depth%2] > root.pivot:
                            data_right.append(data[i])
                else:
                    
            
            print "Left"
            root.left = build_kdtree(data_left, depth+1)
            
            print "Right"
            root.right = build_kdtree(data_right, depth+1)
        

data = pickle.load(open('manhattan.bin'))
root = build_kdtree(data, 0)
