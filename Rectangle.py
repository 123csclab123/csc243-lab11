class Point :
    def __init__ ( self , x , y ) :
        self . x = x
        self . y = y
    def __str__ ( self ) :
        return "(" + str ( self . x ) + " , " + str ( self . y ) + ") "

class Rectangle :
    def __init__(self,p,q) :
       assert type(p) is Point and type(q) is Point and p.x >= q.x or q.y >= p.y, "Bad input!"
       self.p=p
       self.q=q
    def __str__(self):
        return "(p=" + str(self.p)+", q="+str(self.q)+")"
    def get_width(self):
        return self.q.x - self.p.x
    def get_height(self):
        return self.q.y - self.p.y
    def perimeter(self):
        return 2*(self.get_width()+self.get_height())
    def area(self):
        return (self.get_width()*self.get_height())
    def contains (self,pt):
        assert type (pt) is Point, "Bad input!"
        return (self.p.x <= pt.x <= self.q.x and self.p.y <= pt.y <= self.q.y)
        
        
    
