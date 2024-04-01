# p, q 接近，很快就能分解

import libnum
import gmpy2

p=libnum.generate_prime(1024)
#下一个素数
q=gmpy2.next_prime(p)
print(p)
print(q)
print(gmpy2.is_prime(q))
e=65537
m="flag{20d6e2da95dcc1fa5f5432a436c4be18}"
m=libnum.s2n(m)
n=p*q
phi_n=(p-1)*(q-1)
d=libnum.invmod(e,phi_n)
c=pow(m,e,n)

print("n=",n)
print ("e=",e)
print ("c=",c)