a = (1, 3, 4, 6, 7, 9)
b = ('cat', 'dog', 'hueg', 'bird', 'mice', 'shalavik')
tmp = {1 : '15cat', 2 : 'dog', 3 : 'hueg', 4 : 'bird', 5 : 'mice', 6 : '0shalavik'}
tmp1 = sorted(tmp.items())
print(tmp)
print(tmp1)
res = {}
for ref_key in tmp1:
    for test in tmp:
        if ref_key == tmp[test]:
            res[test] = tmp[test]
            tmp.pop(test)
            break
print(res)
