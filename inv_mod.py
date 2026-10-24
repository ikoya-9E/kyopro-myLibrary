#(a*x)%b=gcd(a,b)となるxを求める。
#つまり、aの逆元を求める
def extgcd(a,b):
    global extgcd_x,extgcd_y
    d=a
    if b!=0:
        d=extgcd(b,a%b)
        extgcd_x,extgcd_y=extgcd_y,extgcd_x
        extgcd_y-=(a//b)*extgcd_x
    else:
        extgcd_x,extgcd_y=1,0
    return d

def mod_inverse(a,m):
    extgcd(a,m)
    return (m+extgcd_x%m)%m

print(mod_inverse(8,5))