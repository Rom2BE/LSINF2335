class reflect(object):
    '''
        A demo class for Python reflection
        '''
    def __init__(self):
        '''
            Constructor for reflect class
            '''
        self.name = "Hongbao Chen"
        self.gender = "Male"
        self.hobby = "Computer game"
    
    def message(self):
        print "I am ", self.name, " and my gender is ", self.gender, "I like ", self.hobby
        print "How do you do?"
    
    @classmethod
    def static_message(self):
        print "I can be called without an instance."

def introduce():
    print "I just introduce myself."