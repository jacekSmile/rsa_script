import libnum
import gmpy2
#生成随机素数
p=libnum.generate_prime(32)
q=libnum.generate_prime(32)
r=libnum.generate_prime(512)
e=65537
m="flag{20d6e2da95dcc1fa5f5432a436c4be18}"
#字符串转数字
m=libnum.s2n(m)
n=p*q*r
phi_n=(p-1)*(q-1)*(r-1)
#求逆元
d=libnum.invmod(e,phi_n)
c=pow(m,e,n)
print ("n=",n)
print ("e=",e)
print ("c=",c)