from random import randint

n = 5

matris1= [[randint(1,50) for j in range(n)] for i in range(n)]
a = [[randint(1,50) for j in range(n)] for i in range(n)]
print("Primera matris:")
print(matris1)
  
print("segunda matris:")
print(a)

result = [[0 for j in range(n)] for i in range(n)]


for x in range(len(matris1)):
    for y in range(len(a[0])):
        for z in range(len(a)):
            result[x][y] += matris1[x][z] * a[z][y]

print("Resultado de la multiplicacion")
for r in result:
   print(r)