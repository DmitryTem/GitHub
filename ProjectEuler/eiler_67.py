f = open('triangle_67.txt','r')

data = f.readlines()

Tree = []
graph = {}

for line in data:
    Tree.append(line.strip().split(' '))

for i in range(len(Tree)):
    for j in range(len(Tree[i])):
        Tree[i][j] = int(Tree[i][j])


for x in range(len(Tree) - 1, -1, -1):
    for y in range(0, x):
        Tree[x - 1][y] += max(Tree[x][y], Tree[x][y + 1])
print(Tree[0][0])


f.close()