from Reflect import reflect
from Reflect import introduce
if __name__ == '__main__':
    ref = reflect()
    
    print ref.__class__                         #1
    print ref.__dict__                          #2
    print ref.__doc__                           #3
    print ref.__sizeof__()                      #4
    print ref.__getattribute__('name')          #5
    
    ref.__setattr__('name', 'Antoine Marchal')
    ref.__setattr__('hobby', 'Internet')
    print ref.name                              #6
    
    introduce()                                 #7
    ref.intro = introduce;
    ref.intro()                                 #8
    
    ref.message()                               #9
    ref.message = introduce
    ref.message()                               #10
    
    reflect.static_message();                   #11