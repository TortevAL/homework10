# 1 Вариант
def print_params(name):
    print((name + ' T.L. ') * 2)

print_params('Denis')
print_params('Artem')
print_params('Vova')

# 2 Вариант
def print_params(name):
    print(name + ' T.L. ')
    print(name + ' T.L. ')

print_params('Denis')
print_params('Artem')
print_params('Vova')

# 3 Вариант
def print_params(name):
    for i in range(2):
        print(name + ' T.L. ')

print_params('Denis')
print_params('Artem')
print_params('Vova')
