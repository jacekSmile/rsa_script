from gmpy2 import *
import libnum
import hashlib
p=275127860351348928173285174381581152299
q=319576316814478949870590164193048041239
n=87924348264132406875276140514499937145050893665602592992418171647042491658461
e=2
c=45617141162985597041928941111553655146539175146765096976546144304138540198644
inv_p = invert(p, q)
inv_q = invert(q, p)
mp = pow(c, (p + 1) // 4, p)
mq = pow(c, (q + 1) // 4, q)
a = (inv_p * p * mq + inv_q * q * mp) % n
b = n - int(a)
c = (inv_p * p * mq - inv_q * q * mp) % n
d = n - int(c)
#因为rabin 加密有四种结果，全部列出。
aa=[a,b,c,d]
for i in aa:
    print(i)
    print(libnum.n2s(int(i)))