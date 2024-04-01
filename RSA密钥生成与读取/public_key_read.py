from Crypto.PublicKey import RSA
with open("pubckey.pem","rb") as f:
    key = RSA.import_key(f.read())
    print('n = %d' % key.n)
    print('e = %d' % key.e)