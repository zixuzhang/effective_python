class Field(object):
    def __init__(self,name):
        self.name = name 
        self.internal_name = '_' + self.name

    def __get__(self,instance,isinstance_type):
        if instance is None : return self
        return getattr(instance,self.internal_name,'')
    
    def __set__(self,instance,value):
        setattr(instance,self.internal_name,value)

class Customer(object):
    first_name = Field('first_name')
    last_name = Field('last_name')
    prefix = Field('prefix')
    suffix = Field('suffix')