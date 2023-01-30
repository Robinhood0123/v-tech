import random
name=[]
for i in range(4):
    i=input("adj meg egy nevet")
    name.append(i)

hp=[]
for x in range(4):
    i=random.randint(1,100)
    hp.append(i)

for y in range(4):
    print(name[y] , hp[y])

print("a legnagyobb hp",max(hp) )
print("a legkissebb hp",min(hp) )
print("átlag", sum(hp)/len(hp))
    
    





