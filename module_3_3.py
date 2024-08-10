

#1 Функция с параметрами по умолчанию
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(a=1, c=True)
print_params(a=False)
print_params( b=25)

#2 Распаковка параметров            #args ** kwargs
def print_params(a, b, c):
   print(a, b, c)
values_list = [1, 2, 3]

print_params(*values_list)
def print_params(**kwards):
    for key, values in kwards.items():
        print(key, values)
values_dict = {'b': 2,'a': "goals", 'c': 3.98}

print_params(**values_dict)

#3 Распаковка плюс отдельные параметры
def print_params(*args):
   print(args)

values_list_2 = [54.32,'Строка']

print_params(*values_list_2, 42)

