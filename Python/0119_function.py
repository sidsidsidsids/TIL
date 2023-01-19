# def my_magic_func(n):
#     return n * 10

# my_list = [1, 2, 3, 4, 5]

# result = map(lambda x : x * 10,(my_list))
# rlt = list(result)
# print(rlt)
# rlt = (lambda x : x * x)(4)
# my_func = lambda n : n*2
# print(my_func(2))

# def fac(n):
#     if n == 0:
#         return 1
#     return n * fac(n-1)

#print(fac(5))

#x,y = 1,2
#z = 1,2,3
#a, *b=1,2,3,4
#print(a,b)

# def my_sum(a, b, c):
#     return a + b + c

# num_list = [10, 20, 30]

# rlt = my_sum(*num_list)

# def test(*values):
#     for value in values:
#         print(value)

# test(1)
# test(1,2)
# test(4,2,3,4,24)

# def my_sum(*agrs):
#     rlt=0
#     for value in agrs:
#         rlt+=value
#     return rlt

# print(my_sum(5,3,5))

def test(**kwargs):
    print(kwargs, type(kwargs))
    print(kwargs['name'])
    return kwargs

test(name='aiden',age=21)