'''Demonstration class for Python reflection'''
class reflect(object):
    '''Documentation of this reflect class'''
    def __init__(self):
        '''Constructor'''
        self.firstname = "Romain"
        self.surname = "Capron"
    
    def message(self):
        print   "My firstname is", self.firstname,"and my surname is", self.surname

def welcome():
    print "Welcome my friend!"