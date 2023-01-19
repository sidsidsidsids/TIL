# a=0
# b=1
# def enclosed():
#     a=10
#     c=3
#     def local(c):
#         print(a,b,c)
#     local(300)
#     print(a,b,c)
# enclosed()
# print(a,b)

# x=0
# def func1():
#     x=1
#     def func2():
#         nonlocal x
#         x=2
#     func2()
#     print(x)

# func1()
# print(x)