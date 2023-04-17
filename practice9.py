class MyClass:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myDef(self):
        return self.age

object = MyClass("Nikita", 20)
object.myDef()
print(dir(object))
print(vars(object))
print(object.__dict__)

method = getattr(object, "myDef")

result = method()

print(result)


def get_inheritance(myClass):
    print(myClass.mro())

get_inheritance(object)