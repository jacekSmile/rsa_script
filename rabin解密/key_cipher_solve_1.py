from Crypto.PublicKey import RSA
import libnum
import gmpy2
#导入公钥
with open("pubkey.pem","rb") as f:
    key = RSA.import_key(f.read())
    n =key.n
    e =key.e
#导入密文
with open("flag","rb") as f:
    c=libnum.s2n(f.read())

print(n)
print(e)
#n 在线分解
p=275127860351348928173285174381581152299
q=319576316814478949870590164193048041239
inv_p = gmpy2.invert(p, q)
inv_q = gmpy2.invert(q, p)
mp = pow(c, (p + 1) // 4, p)
mq = pow(c, (q + 1) // 4, q)
a = (inv_p * p * mq + inv_q * q * mp) % n
b = n - int(a)
c = (inv_p * p * mq - inv_q * q * mp) % n
d = n - int(c)
#因为rabin 加密有四种结果，全部列出。
aa=[a,b,c,d]
for i in aa:
    # print(i)
    print(libnum.n2s(int(i)))