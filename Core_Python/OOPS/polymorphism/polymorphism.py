# Functions with same name but different parameters


class bird:
    
    def intro(self):
        print("Paravaigal Parakum")
        
    def flight(self):
        print("Paravaigalukku Parakka theriyum")
        
class sparrow(bird):    
    def flight(self):
        print("Chittu Kuruvi")

class eagle(bird):    
    def flight(self):
        print("Kalugu da ")
        
obj1 = bird();
obj1.flight()

obj2 = sparrow();
obj2.intro()
obj2.flight()