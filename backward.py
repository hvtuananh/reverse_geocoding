import pickle
from kdtree import KdNode

root = pickle.load(open('manhattan-kdtree.bin'))

#Test search function
print root.search((((40.768999663535894+40.76916799224432)/2, (-73.952623762616696-73.952331846439463)/2)))