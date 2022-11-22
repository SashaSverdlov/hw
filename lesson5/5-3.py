a = ('asdsa', 'yyyyy', 'asdfgh', 'oiuytr', 'hohhoh')
b = tuple(filter(lambda i: i == i[::-1],a))
print(b)