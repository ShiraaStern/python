
def inventory_summary(dict):
    count = 0
    for key,value in dict.items():
      count = count+ value[0]
    return count

my_dict={'milk':(23,4),
         'apple':(45,2)}

print(inventory_summary(my_dict))

def print_args_kwargs(*args,**kwargs):
    print(args)
    for key,value in kwargs.items():
        print(key,value)

print_args_kwargs(1,2,3,4, name='shira', age=13)