a = 1 

def my_function(a=a):
    print(a)
    a = 3
    print(a)


my_function()
print(a)