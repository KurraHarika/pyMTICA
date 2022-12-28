#remove empty strings
lst1=["sedan", "SUV", "", "", "Pickup", '', '     ']

ans=[]

for i in lst1:
    if i:
        ans.append(i)



print(ans)




ans=[i for i in lst1 if i]
print(ans)
