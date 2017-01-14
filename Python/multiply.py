# a = [2,4,10,16]

# def multiply(a,b):
#     for val in a:
#         val = val * b
#     return a

# c = multiply([2,4,10,16], 5)
# print c

def multiply(a,b):
    arr = []
    for val in a:
        arr.append(val * b)
    return arr

c = multiply([2,4,10,16], 5)
print c
