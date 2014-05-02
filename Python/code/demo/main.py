from Reflect import reflect
from Reflect import welcome
if __name__ == '__main__':
    i = reflect()
    
    print i.__class__                         #1
    print i.__dict__                          #2
    print i.__doc__                           #3
    print i.__sizeof__()                      #4
    
    print i.__getattribute__('firstname')     #5
    i.__setattr__('firstname', 'Antoine')
    i.__setattr__('surname', 'Marchal')
    print i.firstname                         #6
    
    welcome()                                 #7
    i.hello = welcome;
    i.hello()                                 #8
    
    i.message()                               #9
    i.message = welcome
    i.message()                               #10