sosu=[]
num_size=10**6
num_check=[False]*(num_size+1)
for i in range(2,num_size+1):
    if num_check[i]==True:
        continue
    sosu.append(i)
    x=i
    while x<=num_size:
        num_check[x]=True
        x+=i
