def manipulate(x, y):
    def inner_fun(x,y):
        return x + y
    
    z = inner_fun(x,y)
    return z + 'Developers'

result = manipulate('Emma', 'Kelly')
print(result)