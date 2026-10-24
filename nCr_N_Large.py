#https://algo-logic.info/combination/#にO(r)で前処理ができる考え方がある

mod=998244353

def npr(n,r):
  res=1
  for i in range(r):
    res*=n-i
    res%=mod
  return res

def gyakugen(x):
  num=[x]
  for i in range(29):
    num.append((num[i]*num[i])%mod)
  res=1
  for i in range(30):
    if ((mod-2)>>i)&1==1:
      res*=num[i]
      res%=mod
  return res
  
fact_inv=[1]
f=1
for i in range(1,10**6+1):	#rの最大値によって変える
  f*=i
  f%=mod
  fact_inv.append(gyakugen(f))
  
def ncr(n,r):
  res=npr(n,r)*fact_inv[r]
  res%=mod
  return res