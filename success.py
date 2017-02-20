from __future__ import division
import math


def u(k):
    if(k==150):
        return 37906088813663586926575
    elif(k==151):
    	return 33301269355913626376693
    else:
    	return u(k-1)-2*u(k-2)
def process(a,b):
    c0=a
    c1=b
    u=[]
    i=0
    while not(c0==0 and c1==0):
        if(c0%2==1):
            u.append((int)(2-(c0-2*c1)%4))
            c0=c0-u[i]
        else:
            u.append(0)
        c0,c1=c1+c0//2,-c0//2
        i+=1

    return u


def u(k):
    if(k==150):
        return 37906088813663586926575
    elif(k==151):
        return 33301269355913626376693
    else :
        return u(k-1)-2*u(k-2)
def process(a,b):
    c0=a
    c1=b
    u=[]
    i=0
    while not(c0==0 and c1==0):
        if(c0%2==1):
            u.append((int)(2-(c0-2*c1)%4))
            c0=c0-u[i]
        else:
            u.append(0)
        c0,c1=c1+c0//2,-c0//2
        i+=1
    return u
def Round(a,b):
    f0=math.ceil(a)
    f1=math.ceil(b)
    n0=a-f0
    n1=b-f1
    h0=0
    h1=0
    n=2*n0+n1
    if(n>=1):
        if((n0-3*n1)<-1):
            h1=1
            h0=1
        else:
            if((n0+4*n1)>=2):
                h1=1
    if(n<-1):
        if((n0-3*n1)>=1):
            h1=-1
            h0=-1
        else:
            if((n0+4*n1)<-2):
                h1=-1
    q0=f0+h0
    q1=f1+h1
    u=[]
    u.append(q0)
    u.append(q1)
    return u
def tnaf(k):
    s0=2579386439110731650419537
    s1=-755360064476226375461594
    r=5846006549323611672814741753598448348329118574063
    d0=s0+s1
    m0=s0*k/r
    m1=s1*k/r
    u=Round(m0,m1)
    r0=k-d0*u[0]-2*s1*u[1]
    r1=s1*u[0]-s0*u[1]
    a=[]
    a.append(r0)
    a.append(r1)
 
    return a
a=[]
a=tnaf(1846006549323611672814741753598448348329118574063)
print(a[0])
print(a[1])
b=[]
b=process(a[0],a[1])
print(b)

