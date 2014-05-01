>>> class A:
...     def hello(self):
...         print "hey!"
... 
>>> A().hello()
hey!
>>> def hello2(self):
...     print "Hello Sir."
... 
>>> A().hello()
hey!
>>> A.hello = hello2
>>> A().hello()
Hello Sir.
