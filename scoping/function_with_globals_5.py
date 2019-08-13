a = 1 

def my_function(a=a):
    print(a)
    a = 3
    print(a)

a = 5

my_function()
print(a)