Lst=[10,15,20,25,30,35,40,45]
ans=[]
for i in Lst:
    ans.append(i**0.5)
print(ans)



Lst=[10,15,20,25,30,35,40,45]
ans=[round(i**0.5,4) for i in Lst]
print(ans)
