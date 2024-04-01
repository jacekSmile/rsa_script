from Crypto.PublicKey import RSA
with open("private1.pem","rb") as f:
    key = RSA.import_key(f.read())
    print('n = %d' % key.n)
    print('e = %d' % key.e)
    print('d = %d' % key.d)
    print('p = %d' % key.p)
    print('q = %d' % key.q)