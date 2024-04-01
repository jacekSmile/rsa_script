import libnum

#生成随机素数
p=libnum.generate_prime(1024)
q=libnum.generate_prime(1024)
e=65537
m="flag{20d6e2da95dcc1fa5f5432a436c4be18}"
#字符串转数字
m=libnum.s2n(m)
n=p*q
phi_n=(p-1)*(q-1)
#求逆元
d=libnum.invmod(e,phi_n)
c=pow(m,e,n)


print("p=",p)
print("q=",q)
print ("n=",n)
print("d=",d)
print ("e=",e)
print ("c=",c) 