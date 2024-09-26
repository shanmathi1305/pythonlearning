# def myfunction(*argument):
#     return sum(argument)
# x=myfunction(1,3,5)
# print(x)

# def multiply(*argument):
#     product = 1
#     for i in argument:
#         product *= i
# print(multiply(2, 3, 4))  
    
# def myfunc(**mydict):
#     for i,j in mydict.items():
#         print(i,":" ,j)
# myfunc(name="sruthi",age=23,course="python")

# def myfunc(**mydict):
#     for i,j in mydict.items():
#         print(i,":" ,j)
# myfunc(name="sruthi",age=23,course="python")

# def myfunction(*argument):
#     print(argument)
# myfunction("I"+"love"+"my"+"country") 
def concatenate(*args, +):
    return (args)
x = concatenate("Hello", "world")
print(x) 