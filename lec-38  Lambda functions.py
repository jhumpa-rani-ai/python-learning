def double(x):
    return x*2 

print(double(5))

def appl(fx,value):
    return 6 + fx(value)

cube = lambda x:x*x*x
avg = lambda x,y,z:(x+y+z) /3

print(cube(5))
print(avg(3,5,10))
print(appl(lambda x: x*x ,2))




    #  Lambda ka syntax
    # for ex:
add = lambda a, b: a + b

print(add(10, 20))
print(add(5, 7))
 