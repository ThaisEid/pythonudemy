list = []
list.append(input("Digite um número: "))
list.append(input("Digite um número: "))
list.append(input("Digite um número: "))
list2 = [int(n) for n in list]

x = int(list[1])
y = int(list[2])

print(list)
print(list[0])
print(x*y)