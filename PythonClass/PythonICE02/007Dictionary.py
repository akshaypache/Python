# Dictionary  - {key:value}
a = {1:"ONE", 2: "TWO", 3:"THREE"}
print(a)
# print(a.keys())
# print(a.values())
print(a[2])

a.update({4:"FOUR"})
print(a)

a.pop(2)
print(a)

print(dir(a))
print(a.items())

# 'clear', 'copy', 'fromkeys', 'get'
# b = a.copy()
# print(b)

# print(a)
# a[3] = "Tushar"
# print(a)

# a = (1,2,3,4,5,6,7,8,9)
# b = "Hello","world"
# dic = dict.fromkeys(a,b)
# print(dic)