import libnum
import gmpy2
#生成素数
p=libnum.generate_prime(1024)
q=libnum.generate_prime(1024)
e1=2333
e2=23333
m="flag{6ed4c74e022cb18c8039e96de93aa9ce}"
m=libnum.s2n(m)
n=p*q
c1=pow(m,e1,n)
c2=pow(m,e2,n)
print("n1=",n)
print("e1=",e1)
print("c1=",c1)
print("n2=",n)
print("e2=",e2)
print("c2=",c2)