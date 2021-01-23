def myfunc(string):
    stringout = []
    for n in string:
        if len(stringout) % 2 == 0:
            stringout.append(n.upper())
        else:
            stringout.append(n)
    return ''.join(stringout)

result = myfunc('willthiswork')
print(result)