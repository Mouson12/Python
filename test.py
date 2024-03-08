from oop import Dog, Bulldog, Dachshund, JackRussellTerrier

print("===============================================")

r = Dog('Reksio', 3)
b = Dog('Burek', 5)
bb = Bulldog('Bulldog',10)
jr = JackRussellTerrier('Jack', 4)
da = Dachshund('Dachshund', 2)

lista = [b/b, jr, da, r, b]

for pies in lista:
    print("_________________________")
    print(type(pies))   #😍[]
    print(pies.speak())