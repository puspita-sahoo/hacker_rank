arr = [[1,1,1,0,0,0], [0,1,0,0,0,0], [1,1,1,0,0,0],[0,0,2,4,4,0],[0,0,0,2,0,0],[0,0,1,2,4,0]]
maximum = []

for i in range(4):
    for j in range(4):
        add = []
        add.extend(arr[i][j:j+3])
        add.append(arr[i+1][j+1])
        add.extend(arr[i+2][j:j+3])
        
        maximum.append(sum(add))
print(max(maximum))







