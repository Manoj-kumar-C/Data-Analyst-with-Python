class manoj:
    
    name = "manojkumar c"
    
    def speak(self):
        print("A simple name called")
        
#manoj.speak() ---> Gives a Error 
         
object1 = manoj()

object1.speak()

object2 = manoj()


# Or You can Specify Like this 

manoj.speak(object2)



# TO del a Object 

del object2

print("Deleted the object")