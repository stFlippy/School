a, b = 1, 2
print('global:', a+b)

def simple():
    # Локальное пространство имен
    b = 4
    print('simple:', a + b)

simple()
print('global', a+B)
