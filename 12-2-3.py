class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def distance(self, other):
        if not isinstance(other, Point):
        ##引数 other が Point クラスのインスタンスであることを確認します。そうでない場合は TypeError を投げます。
            raise TypeError("Argument must be of type Point")
        
        return ((other.x - self.x) ** 2 + (other.y - self.y) ** 2 + (other.z - self.z)) ** 0.5
    
    def dot_product(self, other):
        if not isinstance(other, Point):
            raise TypeError("Argument must be of type Point")
        
        return self.x * other.x + self.y * other.y + self.z * other.z


p1 = Point(1, 2, 9)
p2 = Point(3, 5, 7)
p3 = Point(10, 46, -100)

print(p1.distance(p2))  
print(p2.distance(p3))  
print(p1.dot_product(p2)) 
print(p2.dot_product(p3)) 