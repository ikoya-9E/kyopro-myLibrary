#ax+by=gcd(a,b)となるx,yをもとめる
def extgcd(a,b):
    global extgcd_x,extgcd_y
    d=0
    if b!=0:
        d=extgcd(b,a%b)
        extgcd_x,extgcd_y=extgcd_x,extgcd_y
        extgcd_y-=(a//b)*extgcd_x
    else:
        extgcd_x,extgcd_y=1,0
    return d

#extgcd(4,11)
#print(exdgcd_x,exdgcd_y)