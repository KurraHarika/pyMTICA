#matrix=[[1,2],[3,4],[5,6],[7,8]]
#ans=[]
#ans=[ [row[i] for row in matrix]
 #     for i in range(len(matrix[0]))]
#print(ans)


'''m=[[1,2],[3,4],[5,6],[7,8]]
ans=[]
for row in range(len(m[0])):
    temp=[]
    for col in range(len(m)):
        temp.append(m[col][row])
    ans.append(temp)
print(ans)'''
        



'''m=[[1,2],[3,4],[5,6],[7,8]]
ans=[]
for row in range(len(m[0])):
     ans.append([m[col][row]for col in range(len(m))])
print(ans)'''


m=[[1,2],[3,4],[5,6],[7,8]]
ans=[[m[col][row]for col in range(len(m))]for row in range(len(m[0]))]
print(ans)
