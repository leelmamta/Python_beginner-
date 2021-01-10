# conditional statements
import turtle 
foo = turtle.Turtle()
def square():
   foo.forward(100)
   foo.right(90)
   foo.forward(100)
   foo.right(90)
   foo.forward(100)
   foo.right(90)
   foo.forward(100)
   foo.right(90)

    
elephant_weight = 3000
ant_weight = 0.1 

if elephant_weight>ant_weight: # if the statement is true 
    square() # then run this statement note:-indentation plays important role 
else: # otherwise 
    foo.forward(100)    #this will run , again indentation is important 
    
  