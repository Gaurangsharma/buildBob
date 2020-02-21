# def argsExample(*args):
#     for ag in (args):
#         print(ag)
# argsExample("Hello","My","Name","Is","Gaurang")

# def kwargsExample(**kwargs):
#     for key, value in kwargs.items():
#         print((key, value))
#
#
# kwargsExample(firstName="Gaurang", LastName="Sharma")


def bothargsandkwargs(arg1, arg2, arg3):
    print(arg1)
    print(arg2)
    print(arg3)


args = ("Hello", "Name", "Gaurang")
bothargsandkwargs(*args)

kwargs = {"arg1": "Hello", "arg2": "Gaurang", "arg3": "Sharma"}
bothargsandkwargs(**kwargs)
