'''
Created on Aug 13, 2018

@author: sunkumar2
'''

class MyClass(object):
    '''
    classdocs
    '''
    print(object)


    def __init__(self, params):
        '''
        Constructor
        '''
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyClass("ssss")
myiter = iter(myclass)

print(next(myiter))  