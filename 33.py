#coding=utf-8

class Meta(type):
    def __new__(meta,name,bases,class_dict):
        print((meta,name,bases,class_dict))
        return type.__new__(meta,name,bases,class_dict)

class MyClass(object,metaclass=Meta):
    stuff = 123

    def foo(self):
        pass

class ValidatePolygon(type):
    def __new__(meta,name,bases,class_dict):
        if bases != (object,):
            if class_dict['sides'] < 3:
                raise ValueError('Polygons need 3+ sides')
        return type.__new__(meta,name,bases,class_dict)

class Polygons(object,metaclass=ValidatePolygon):
    sides = None

    @classmethod
    def interior_angles(cls):
        return (cls.sides - 2) * 180

