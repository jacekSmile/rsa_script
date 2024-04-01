from gmpy2 import gcd, invert

e = 65537
n = [int(line.replace("n = ", "")) for line in open('n_output.txt').readlines()]
c = [int(line.replace("c = ", "")) for line in open('c_output.txt').readlines()]

for i in range(len(n)):
    for j in range(len(n)):
        if i != j:
            p = gcd(n[i], n[j])
            if p != 1:
                print(i, j, p)

p_17 = 132585806383798600305426957307612567604223562626764190211333136246643723811046149337852966828729052476725552361132437370521548707664977123165279305052971868012755509160408641100548744046621516877981864180076497524093201404558036301820216274968638825245150755772559259575544101918590311068466601618472464832499
q_17 = n[17] // p_17

phi_n = (p_17 - 1) * (q_17 - 1)
d = invert(e, phi_n)

m = pow(c[17], d, n[17])

import libnum

print(libnum.n2s(int(m)))
