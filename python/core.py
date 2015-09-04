
class Robot():
    
    def __init__(self, x, y):   
        self._x = x;
        self._y = y;
        self.moves = 0; 
    
    def walk(self, x, y):
        self._x += x;
        self._y += y;
        self.moves += 1;
    
    def get_position(self):
        return self._x, self._y
    
    def print_mood(self):
        if self.moves < 2:
            print 'Brand new';
        else:
            print 'Tried Already';
            
