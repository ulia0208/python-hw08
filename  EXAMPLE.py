info=['qw', 'er', 'ty', 'ui', 'op', 'as']

# for i in range(len(info)):
#     print(info[i])
info[1]='mnbvxc'
x= input('Введите ')

for i in range(len(info)):
    if x in info[i]:
        print(info[i])
        info.pop(i)

print(info)