a = 1 # global

def my_function(a=a):
    # global a
    print(a)
    a = 3
    print(a)

a = 5

my_function()
print(a)