class KdNode:
    def __init__(self):
        self.data = None
        self.depth = 0
        self.pivot = 0
        self.left = None
        self.right = None
        pass
        
    def find_candidate(self, loc, depth = 0):
        if self.left is None or self.right is None:
            return self.data
            
        if self.pivot > loc[depth%2]:
            return self.left.find_candidate(loc, depth+1)
        elif self.pivot < loc[depth%2]:
            return self.right.find_candidate(loc, depth+1)
        else:
            return self.left.find_candidate(loc, depth+1)+self.right.find_candidate(loc, depth+1)
            
    def search(self, loc):
        candidates = self.find_candidate(loc)
        for res in candidates:
            if self.point_inside_polygon(loc, res['points']):
                return res['addr']
                
        return None
                
    def point_inside_polygon(self, loc, poly):
        x, y = loc
        n = len(poly)
        inside = False

        p1x, p1y = poly[0]
        for i in range(n+1):
            p2x, p2y = poly[i % n]
            if y > min(p1y, p2y):
                if y <= max(p1y, p2y):
                    if x <= max(p1x, p2x):
                        if p1y != p2y:
                            xinters = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                        if p1x == p2x or x <= xinters:
                            inside = not inside
            p1x, p1y = p2x, p2y

        return inside