lst=["1","2","3","4","5"]
for i in range(len(lst)//2):
    lst[i],lst[-i-1]=lst[-i-1],lst[i]
print(lst)
