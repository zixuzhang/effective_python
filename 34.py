import json
class Serializable(object):
    def __init__(self,*args):
        self.args = args 

    def serialize(self):
        return json.dumps({'args':self.args})

class Point2D(Serializable):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.x = x
        self.y = y
    
    def __repr__(self):
        return 'Point2D(%d,%d)' %(self.x,self.y)

class Deserializable(Serializable):
    @classmethod
    def deserialize(cls,json_data):
        params = json.loads(json_data)
        return cls(*params['args'])

class BetterPoint2D(Deserializable):
    def __init__(self,x,y):
        super().__init__(x,y)

class BetterSerializable(object):
    def __init__(self,*args):
        self.args = args

    def serialize(self):
        return json.dumps({
            'class': self.__class__.__name__,
            'args': self.args
        })
    
    def __repr__(self):
        return '%s(%s)' % (self.__class__.__name__,self.args)
    
registry = {}

def register_class(target_class):
    registry[target_class.__name__] = target_class

def deserialize(data):
    params = json.loads(data)
    name = params['class']
    target_class = registry[name]
    return target_class(*params['args'])

class EvenBetterPoint2D(BetterSerializable):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.x = x 
        self.y = y

register_class(EvenBetterPoint2D)

class Meta(type):
    def __new__(meta,name,bases,class_dict):
        cls = type.__new__(meta,name,bases,class_dict)
        register_class(cls)
        return cls

class RegisteredSerializable(BetterSerializable,metaclass=Meta):

    pass    
    # def __init__():
    #     super().__init__(x,y)
    #     self.x = x 
    #     self.y = y

class Vector3D(RegisteredSerializable):
    def __init__(self,x,y,z):
        super().__init__(x,y,z)
        self.x,self.y,self.z = x,y,z
        