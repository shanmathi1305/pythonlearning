# my_list=[1,3,4,5]
# def double(n):
#     return n**2
# result=map(double,my_list)
# print(list(result))

# my_list = ["shanmathi"]

# def uppercase(s):
#     return s.upper()

# result = map(uppercase, my_list)
# print(list(result))

# my_list = [1, 3, 4, 5]

# def add(n):
#     return n + 10

# result = map(add, my_list)
# print(list(result))

# my_list = [1, 3, 4, 5]

# result = map(lambda n: n * 2, my_list)
# print(list(result))

# my_list = ["shanmathi"]

# result = map(lambda n: n.capitalize(), my_list)
# print(list(result))

# my_list=[1,2,4,5,6,8,9]

# result=filter(lambda n: n%2==0,my_list)
# print(list(result))

# my_list=[11,2,4,15,6,8,19]

# result=filter(lambda n:n>10,my_list)
# print(list(result))

# my_list = ['cat', 'dog', 'elephant', 'fish', 'horse']

# result = filter(lambda word: len(word) >= 4, my_list)
# print(list(result))


# my_list = ['apple', 'cherry', 'fig']

# result = filter(lambda word: 'a' not in word, my_list)
# print(list(result))

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# result = filter(lambda n: n % 3 == 0, my_list)
# print(list(result))

# my_list = [-1, 2, 3, 4, -5, 6, 7, 8, 9, 10, -11, 12]
# result=filter ( lambda n:n <0,my_list)
# print(list(result))


from functools import reduce 

my_list = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, my_list)

print(product)

# my_list = ['Hello', 'world', 'this', 'is', 'a', 'book']

# result = ' '.join(my_list)
# print(result)


# from functools import reduce 

# my_list = [1, 3, 5, 7, 9, 2, 8]

# def add(x, y):
#     return x + y
# result = reduce(add, my_list)
# print(result)

