from Reflect import reflect
from Reflect import introduce
if __name__ == '__main__':
    ref = reflect()
    
    print ref.__class__                #<class 'Reflect.reflect'>

    print ref.__dict__                 #{'name': 'Romain Capron', 'hobby': 'Comic Books'}

    print ref.__doc__                  #Documentation of this demo class for Python reflection

    print ref.__sizeof__()             #32
    
    print ref.__getattribute__('name') #Romain Capron
    
    ref.__setattr__('name', 'Antoine Marchal')
    ref.__setattr__('hobby', 'Internet')
    print ref.name                     #Antoine Marchal
    
    introduce()                        #I just introduce myself.

    ref.intro = introduce;             #
    ref.intro()                        #I just introduce myself.
    
    ref.message()                      #I am Antoine Marchal and I like Internet

    ref.message = introduce            #
    ref.message()                      #I just introduce myself.
    
    reflect.static_message();          #I can be called without an instance.