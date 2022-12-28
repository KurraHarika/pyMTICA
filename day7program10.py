Lst=[10,15,2,25,30,3,40,4]
ans=[]
for i in Lst:
    if i*i >=50:
        ans.append(i*i)
print(ans)



Lst=[10,15,2,25,30,3,40,4]
ans=[i*i for i in Lst if i*i >=50]
print(ans)
