class Room:
    def __init__(self, nm, ar):
        self.name = nm
        self.area = ar

    def compare(self, val):
        if self.area > val:
            print('{0} >= {1}'.format(self.name,val))
        else:
           print('{0} < {1}'.format(self.name,val)) 
        
room = Room("aaaaaaaaaaaa", 35000000000000000)
print(room.compare(30)) 
print(room.compare(700)) 
print(room.area)