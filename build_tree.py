import pickle
from kdtree import KdNode

def build_kdtree(data, depth):
    #depth: even = lat, odd = lng (start from 0)
    root = KdNode()
    total = len(data)
    
    if total < 2:
        root.data = data
    else:
        data = sorted(data, key=lambda res: res['bbox'][0][depth%2])
        pivot_index = total/2
        root.pivot = data[pivot_index]['bbox'][0][depth%2]
        
        #handle boundary case: total = 2
        if total == 2:
            root.left = build_kdtree(data[:1], depth+1)
            root.right = build_kdtree(data[1:], depth+1)
        else:
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
                
            #if data is not separable 
            if len(data_left) == total or len(data_right) == total:
                root.data = data
            else:
                root.left = build_kdtree(data_left, depth+1)
                root.right = build_kdtree(data_right, depth+1)
                
    return root
    
data = pickle.load(open('manhattan.bin'))
root = build_kdtree(data, 0)

pickle.dump(root, open('manhattan-kdtree.bin', 'w'))

#Test search function
root.search((40.7, -73.9))