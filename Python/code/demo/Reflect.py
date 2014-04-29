class reflect(object):
    '''Documentation of this demo class for Python reflection'''
    def __init__(self):
        '''
            Constructor for reflect class
        '''
        self.name = "Romain Capron"
        self.hobby = "Comic books"
    
    def message(self):
        print "I am", self.name, "and I like", self.hobby
    
    @classmethod
    def static_message(self):
        print "I can be called without an instance."

def introduce():
    print "I just introduce myself."