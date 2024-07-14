a = 'test1.test2.'
a += str(input())+'.'
print(a)

a = a.split('.')
a = list(filter(None, a))
print(a)