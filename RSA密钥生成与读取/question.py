import libnum
import gmpy2
from Crypto.PublicKey import RSA

p=libnum.generate_prime(1024)
#下一个素数
q=int(gmpy2.next_prime(p))
e=65537
m="flag{a272722c1db834353ea3ce1d9c71feca}"
m=libnum.s2n(m)
n=p*q
c=pow(m,e,n)
flag_c=libnum.n2s(c)
rsa_components = (n, e)
keypair = RSA.construct(rsa_components)
with open('pubckey1.pem', 'wb') as f :
    f.write(keypair.exportKey())
with open("flag.txt","wb") as f:
    f.write(flag_c)